# FastAPI CRUD Demo

A simple, self-contained CRUD API built for learning and demonstration purposes.

The project focuses on clarity, minimal infrastructure, and clean architecture using modern Python tooling.

---

## Overview

This API exposes a basic CRUD interface for managing `items`.  
It is designed to be:

- Easy to run locally
- Easy to understand
- Easy to extend
- Fully containerized

Interactive API documentation is automatically generated via Swagger.

---

## Tech Stack

- **FastAPI** – API framework
- **SQLite** – Embedded database
- **SQLite WAL mode** – Improved concurrency
- **SQLModel** – ORM + validation
- **Docker & Docker Compose** – Containerization and runtime
- **Uvicorn** – ASGI server

---

## Project Structure

```text
crud-api/
├── app/
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   └── schemas.py
├── data/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

Running the API
Prerequisites

Docker Desktop

Start the application
docker compose up --build


The API will be available at:

http://localhost:8000

API Documentation

Interactive Swagger documentation is available at:

http://localhost:8000/docs

Available Endpoints

POST /items

GET /items

GET /items/{id}

PUT /items/{id}

PATCH /items/{id}

DELETE /items/{id}

Database

SQLite file-based database stored at ./data/app.db

Write-Ahead Logging (WAL) enabled

Database files are not committed to version control

Development Notes

Database tables are created automatically on startup

No external services required

Authentication and HTTPS intentionally omitted for simplicity

License

This project is provided for educational and demonstration purposes