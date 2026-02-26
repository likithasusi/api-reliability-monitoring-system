# API Reliability & Monitoring System

A Python-based backend system that continuously monitors the availability and performance of external APIs, logs their health status, and sends real-time Slack alerts when failures occur.

---

## 📌 Project Overview
Modern applications depend heavily on third-party APIs (payments, weather, authentication, data services).  
This project helps detect API downtime, slow responses, and network failures early by automatically monitoring API health and alerting teams in real time.

---

## 🚀 Features
- Dynamic API registration via REST endpoints
- Automatic background health checks (runs periodically)
- Response time measurement
- Detection of HTTP errors and network/DNS failures
- Real-time Slack alerts using Incoming Webhooks
- Persistent logging of API health history using SQLite
- Interactive API testing via Swagger UI

---

## 🛠 Tech Stack
- **Python**
- **FastAPI**
- **httpx** (async HTTP requests)
- **SQLite**
- **SQLAlchemy**
- **Slack Incoming Webhooks**

---

## ⚙️ How It Works
1. APIs are added dynamically using a POST endpoint
2. A background scheduler periodically checks all registered APIs
3. Each API response is validated and timed
4. Health status is stored in a database
5. Slack alerts are triggered when an API goes DOWN

---

## 🌍 Real-World Use Cases
- Monitoring third-party APIs used in applications
- Detecting downtime, DNS issues, and slow responses
- Alerting teams before users are impacted
- Observing unstable or flapping APIs

---

## 🚨 Failure Handling
- APIs are marked **DOWN** when:
  - They return unexpected HTTP status codes
  - They are unreachable due to network/DNS issues
- Slack alerts include the API name and failure reason
- All failures are logged for analysis

---

## ▶️ Run the Project Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt