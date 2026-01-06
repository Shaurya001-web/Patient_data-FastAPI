🏥 Patient Management API (FastAPI)
📌 Overview

This project is a Patient Management REST API built using FastAPI.
It allows you to create, view, update, and sort patient records with strong data validation and automatic calculations like BMI and health verdict.

The API uses:

FastAPI for building high-performance APIs

Pydantic (v2) for data validation and computed fields

JSON file storage (patient.json) as a lightweight database

This project demonstrates real-world FastAPI best practices, including:

Proper request/response validation

Computed fields

CRUD operations

Clean API documentation (Swagger)

🚀 Features (What This API Does)
✅ Patient Data Management

Add new patients

View all patients

View a single patient by ID

Update existing patient details

✅ Automatic Health Calculations

BMI is calculated automatically

Health verdict is derived from BMI:

Underweight

Normal

Obese

✅ Sorting & Filtering

Sort patients by:

Height

Weight

BMI

Supports ascending and descending order

✅ Strong Validation

Age restricted to 0–18

Gender restricted to male / female / others

Height & weight must be positive

Duplicate patient IDs are rejected

🛠️ Tech Stack

Python 3.9+

FastAPI

Pydantic v2

Uvicorn

JSON file storage
