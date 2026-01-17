# 🩺 wsbapp – Health Check API

[![CI](https://github.com/AmbrogyKleks/wsbapp/actions/workflows/docker-build.yml/badge.svg)](
https://github.com/AmbrogyKleks/wsbapp/actions/workflows/docker-build.yml
)
![Docker Image](https://img.shields.io/docker/v/m1cm0l/wsbapp?label=docker%20image)
![Docker Pulls](https://img.shields.io/docker/pulls/m1cm0l/wsbapp)
![Docker Image Size](https://img.shields.io/docker/image-size/m1cm0l/wsbapp/latest)

---

## 📌 Opis projektu

**wsbapp** to **ćwiczeniowa aplikacja Health Check API**, stworzona w celu nauki i demonstracji:
- pracy z **Git i GitHub** (branching, PR, workflow),
- konteneryzacji aplikacji przy użyciu **Docker** i **Docker Compose**,
- publikacji obrazów w **Docker Hub**,
- podstaw **CI/CD** i dobrych praktyk DevOps.

Projekt jest celowo prosty funkcjonalnie, ale **zrobiony poprawnie technicznie** – dokładnie tak, jak w realnych projektach produkcyjnych.

---

## 🎯 Cel edukacyjny

Repozytorium służy jako **laboratorium ćwiczeniowe**, w którym można trenować:

- pełny cykl: code → build → image → registry → run,
- debugowanie aplikacji w kontenerze,
- health checki aplikacyjne i kontenerowe,
- przygotowanie projektu pod CI/CD i Kubernetes.

---

## 🧱 Architektura (uproszczona)

```text
┌─────────────┐
│   Client    │
└──────┬──────┘
       │ HTTP
       ▼
┌──────────────────────┐
│  Flask Application   │
│  ├─ /health          │
│  ├─ /live (planned)  │
│  └─ /ready (planned) │
└────────┬─────────────┘
         ▼
   Docker Container