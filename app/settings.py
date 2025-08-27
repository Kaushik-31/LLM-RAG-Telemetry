from pydantic import BaseModel
import os

class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "llm-rag-telemetry-dashboard")
    sla_p95_seconds: float = float(os.getenv("SLA_P95_SECONDS", "1.5"))

settings = Settings()
