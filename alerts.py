import httpx

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_alert(api_name: str, message: str):
    payload = {
        "text": f"🚨 API ALERT 🚨\nAPI: {api_name}\nIssue: {message}"
    }

    try:
        httpx.post(SLACK_WEBHOOK_URL, json=payload, timeout=5)
    except Exception as e:
        print("Slack alert failed:", e)