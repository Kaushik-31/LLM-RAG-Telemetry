from prometheus_client import Counter, Histogram

REQUESTS = Counter(
    "llm_requests_total", "Total LLM requests", ["status"]
)
LATENCY = Histogram(
    "llm_request_latency_seconds",
    "LLM request latency seconds",
    buckets=(0.2, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0),
)
TOKENS = Counter(
    "llm_tokens_total", "Token counts", ["type"]  # type=prompt|completion
)
RAG_HITS = Counter(
    "rag_hits_total", "RAG retrieval document hits"
)
SLA_VIOLATIONS = Counter(
    "llm_sla_violations_total", "SLA p95 latency violations"
)
