# 🏥 Patient Management API (FastAPI)

A high-performance **REST API** built using FastAPI to manage patient records with **robust validation, computed health metrics, and clean architecture**.

---

## 📌 Overview

This project demonstrates how to build a **production-style backend API** using FastAPI and Pydantic.

It supports complete patient lifecycle management along with **automatic BMI calculation and health classification**, making it a practical example of real-world backend development.

---

## 🚀 Features

### 🧾 Patient Management
- Create new patient records  
- View all patients  
- Retrieve patient by ID  
- Update existing patient details  

---

### 📊 Smart Health Metrics
- Automatic **BMI calculation**  
- Health classification:
  - Underweight  
  - Normal  
  - Obese  

---

### 🔎 Sorting & Querying
- Sort patients by:
  - Height  
  - Weight  
  - BMI  
- Supports:
  - Ascending (`asc`)  
  - Descending (`desc`)  

---

### ✅ Data Validation
- Age: **0–18 only**  
- Gender: `male | female | others`  
- Height & Weight: must be positive  
- Prevents duplicate patient IDs  

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **FastAPI**
- **Pydantic v2**
- **Uvicorn**
- **JSON (File-based storage)**

---

## 📂 Project Structure
