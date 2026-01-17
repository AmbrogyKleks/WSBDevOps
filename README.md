# wsbapp – Health Check API

Minimalna aplikacja Health Check do ćwiczeń z GitHub, CI/CD i Dockera.
Aplikacja wykonana podczas ćwiczeń na kursie DevOps w WSB-NLU 2025/2026.

## Endpoint
GET /health

## Przykładowa odpowiedź
```json
{
  "status": "UP",
  "service": "wsbapp-health-api",
  "version": "1.0.0"
}

---