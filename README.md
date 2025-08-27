# LLM-RAG Telemetry Dashboard

End-to-end template to **monitor and improve reliability** of an LLM/RAG chatbot using **OpenTelemetry (optional), Prometheus, Grafana, and alerting**. Tracks latency, error rate, throughput, token usage, and SLA breach alerts.

## ✨ What you get
- RAG API (FastAPI) with simple in-memory retriever (drop-in your FAISS/Pinecone later)
- `/chat` endpoint instrumented with **Prometheus metrics**
- **SLA-aware alerts** (p95 latency + error budget burn)
- **Grafana dashboard** (import JSON) + pre-provisioned Prometheus datasource
- Docker Compose for one-command spin-up

## 📊 Tracked Metrics
- `llm_requests_total{status}` – request count by success/error
- `llm_request_latency_seconds` – histogram + p95/p99 latency
- `llm_tokens_total{type=prompt|completion}` – token counters (mocked; wire to real provider)
- `rag_hits_total` – retrieval hits
- `rag_cache_hits_total` – cache hits (if you add a cache)
- `llm_sla_violations_total` – SLA breach counter

## 🧰 Stack
- FastAPI (Python) • `prometheus_client`
- Prometheus • Alertmanager
- Grafana (pre-provisioned)
- (Optional) OpenTelemetry SDK + Collector

## 🚀 Quickstart
```bash
# 1) clone your repo and cd into it
# 2) create the files from this README (see below)
cp .env.example .env
docker compose up -d --build

# open:
# - API: http://localhost:8000/docs
# - Metrics: http://localhost:8000/metrics
# - Prometheus: http://localhost:9090
# - Grafana: http://localhost:3000  (admin / admin)
