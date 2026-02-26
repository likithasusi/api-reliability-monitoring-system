from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal
from app.models import MonitoredAPI, APIHealthLog
from app.monitor import check_api
import asyncio
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="API Monitoring System")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/add-api")
def add_api(api_name: str, url: str, expected_status: int = 200, db: Session = Depends(get_db)):
    api = MonitoredAPI(
        api_name=api_name,
        url=url,
        expected_status=expected_status
    )
    db.add(api)
    db.commit()
    return {"message": "API added successfully"}


@app.get("/list-apis")
def list_apis(db: Session = Depends(get_db)):
    return db.query(MonitoredAPI).all()


@app.get("/run-health-check")
async def run_health_check(db: Session = Depends(get_db)):
    apis = db.query(MonitoredAPI).all()
    for api in apis:
        await check_api(api, db)
    return {"message": "Health check completed"}


@app.get("/health-report")
def health_report(db: Session = Depends(get_db)):
    logs = db.query(APIHealthLog).order_by(APIHealthLog.checked_at.desc()).all()
    return logs
async def auto_health_check():
    from app.database import SessionLocal
    from app.models import MonitoredAPI
    from app.monitor import check_api

    while True:
        db = SessionLocal()
        apis = db.query(MonitoredAPI).all()

        for api in apis:
            await check_api(api, db)

        db.close()
        await asyncio.sleep(300)  # runs every 5 minutes

    @app.on_event("startup")
    async def start_scheduler():
        asyncio.create_task(auto_health_check())