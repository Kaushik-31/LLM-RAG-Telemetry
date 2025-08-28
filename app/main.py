from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from pydantic import BaseModel
from time import perf_counter

from .metrics import REQUESTS, LATENCY, RAG_HITS, SLA_VIOLATIONS
from .rag import retrieve
from .llm import generate
from .settings import settings

app = FastAPI(title=settings.app_name)

class ChatRequest(BaseModel):
    query: str

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.post("/chat")
def chat(body: ChatRequest):
    start = perf_counter()
    try:
        docs = retrieve(body.query)
        RAG_HITS.inc(len(docs))
        prompt = f"Query: {body.query}\nContext: {' | '.join(docs)}"
        output = generate(prompt)
        status = "success"
        return {"answer": output, "context_docs": docs}
    except Exception as e:
        status = "error"
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        elapsed = perf_counter() - start
        LATENCY.observe(elapsed)
        REQUESTS.labels(status).inc()
        if elapsed > settings.sla_p95_seconds:
            SLA_VIOLATIONS.inc()
