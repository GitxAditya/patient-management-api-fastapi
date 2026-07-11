# patient-management-api-fastapi
A RESTful Patient Management API built with FastAPI demonstrating CRUD operations, request validation, computed fields, query parameters, and automatic API documentation.
# Patient Management API

A RESTful Patient Management System built with **FastAPI** as part of my backend development learning journey.

This project demonstrates how to build APIs using FastAPI, perform CRUD operations, validate user input using Pydantic, calculate BMI automatically, and manage patient records stored in a JSON file.

---

## Features

- Create a new patient
- View all patients
- Get patient by ID
- Update existing patient
- Sort patients by height, weight, or BMI
- Automatic BMI calculation
- Health verdict based on BMI
- Input validation using Pydantic
- Interactive Swagger UI
- JSON-based data storage

---

## Tech Stack

- Python 3
- FastAPI
- Pydantic
- Uvicorn
- JSON

---

## Project Structure

```
.
├── main.py
├── patients.json
└── README.md
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/about` | API information |
| GET | `/view` | View all patients |
| GET | `/patients/{patient_id}` | Get patient by ID |
| GET | `/sort` | Sort patients |
| POST | `/create` | Create a new patient |
| PUT | `/edit/{patient_id}` | Update patient |

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-patient-management-api.git
```

Move into the project

```bash
cd fastapi-patient-management-api
```

Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

Run the server

```bash
uvicorn main:app --reload
```

---

## API Documentation

After running the server:

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## Learning Objectives

This project helped me learn:

- FastAPI fundamentals
- REST API development
- CRUD operations
- Path Parameters
- Query Parameters
- Request validation
- Response handling
- HTTP status codes
- Pydantic models
- Computed fields
- JSON data handling

---

## Future Improvements

- Database integration (MySQL/PostgreSQL)
- JWT Authentication
- Delete endpoint
- Pagination
- Search & filtering
- Docker support
- Unit testing

---

## Author

**Aditya**

Aspiring AI Engineer, Data Scientist, and Startup Builder.

Currently learning backend development, data science, and AI application development.
