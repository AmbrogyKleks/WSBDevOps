# 🩺 wsbapp – Health Check API

Minimalna aplikacja **Health Check API**, stworzona jako **aplikacja ćwiczeniowa** do nauki:
- Git & GitHub workflow
- Dockera i Docker Compose
- podstaw CI/CD
- dobrych praktyk DevOps

Projekt celowo jest prosty funkcjonalnie, ale **poprawny architektonicznie** – dokładnie tak, jak w realnych środowiskach produkcyjnych.

---

## 🎯 Cel projektu

`wsbapp` służy jako **laboratorium szkoleniowe** do:
- pracy na branchach i Pull Requestach,
- budowania i uruchamiania aplikacji w kontenerach,
- testowania health checków (liveness / readiness),
- przygotowania pod CI/CD oraz Kubernetes.

---

## 🖼️ Architektura (uproszczona)

```text
┌─────────────┐
│   Client    │
└──────┬──────┘
       │ HTTP
       ▼
┌──────────────────┐
│  Flask App       │
│  /health         │
│  /live (future)  │
│  /ready (future) │
└────────┬─────────┘
         ▼
   Docker Container