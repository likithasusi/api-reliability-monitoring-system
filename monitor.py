import time
import httpx
from datetime import datetime
from sqlalchemy.orm import Session
from app.models import APIHealthLog
from app.alerts import send_alert

async def check_api(api, db: Session):
    start_time = time.time()
    status = "UP"

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(api.url)

        response_time = round((time.time() - start_time) * 1000, 2)

        if response.status_code != api.expected_status:
            status = "DOWN"
            send_alert(api.api_name, f"Unexpected status {response.status_code}")

    except Exception as e:
        response_time = 0
        status = "DOWN"
        send_alert(api.api_name, str(e))

    log = APIHealthLog(
        api_name=api.api_name,
        status=status,
        response_time=response_time,
        checked_at=datetime.utcnow()
    )

    db.add(log)
    db.commit()