Hospital Management System API
A REST API built using FastAPI and PostgreSQL for managing patient records.

Features
Add Patient
Update Patient
View Patient Details
Delete Patient
Technologies Used
Python
FastAPI
PostgreSQL
psycopg2
API Endpoints
Add Patient
POST /addpatients

Update Patient
PUT /update

Get All Patients
GET /readdata

Delete Patient
DELETE /delete

Run the Project
pip install -r requirements.txt
uvicorn main:app --reload