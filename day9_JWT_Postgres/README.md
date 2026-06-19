# Day 9 - PostgreSQL Authentication

## Concepts Learned

* User Registration
* Password Hashing
* PostgreSQL Storage
* Authentication Flow
* Login Validation

## APIs

POST /register

POST /login

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Passlib
* Docker

## Outcome

Built a real authentication system storing users in PostgreSQL with securely hashed passwords.


# Day 12 - JWT Protected Notes API

## Features

- User Registration
- User Login
- Password Hashing
- JWT Authentication
- Protected Routes
- PostgreSQL Database
- User Specific Notes

## Endpoints

POST /register
POST /login
POST /notes
GET /notes

# Day 13 - FastAPI Notes API with JWT Authentication & CRUD

## Overview

A secure Notes Management API built using FastAPI, PostgreSQL, SQLAlchemy, and JWT Authentication.

Users can:

* Register
* Login
* Generate JWT Tokens
* Create Notes
* View Their Own Notes
* Update Their Own Notes
* Delete Their Own Notes

The API implements Authentication and Authorization to ensure users can only access their own data.

---

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT (python-jose)
* Passlib (bcrypt)
* Docker

---

## Features

### Authentication

* User Registration
* User Login
* Password Hashing using bcrypt
* JWT Token Generation
* JWT Token Verification
* Protected Routes using HTTPBearer

### Notes CRUD

* Create Note
* Get Notes
* Update Note
* Delete Note

### Authorization

* User-specific notes
* Ownership validation
* Users cannot access other users' notes
* Users cannot update other users' notes
* Users cannot delete other users' notes

---

## API Endpoints

### User Endpoints

#### Register User

POST /register

```json
{
  "username": "akhil",
  "password": "akhil123"
}
```

#### Login User

POST /login

```json
{
  "username": "akhil",
  "password": "akhil123"
}
```

Response:

```json
{
  "access_token": "<jwt_token>"
}
```

---

### Notes Endpoints

#### Create Note

POST /notes

```json
{
  "title": "My Note",
  "content": "Hello World"
}
```

#### Get Notes

GET /notes

Returns all notes belonging to the authenticated user.

#### Update Note

PUT /notes/{note_id}

```json
{
  "title": "Updated Title",
  "content": "Updated Content"
}
```

#### Delete Note

DELETE /notes/{note_id}

---

## Database Schema

### Users Table

| Column   | Type    |
| -------- | ------- |
| id       | Integer |
| username | String  |
| password | String  |

### Notes Table

| Column  | Type    |
| ------- | ------- |
| id      | Integer |
| title   | String  |
| content | String  |
| user_id | Integer |

---

## Learning Outcomes

* FastAPI Routing
* Dependency Injection
* PostgreSQL Integration
* SQLAlchemy ORM
* Password Hashing
* JWT Authentication
* Protected APIs
* CRUD Operations
* Authorization & Ownership Validation
* Dockerized Database Setup

---

## Project Status

Completed Day 13 of AI Engineering Journey.

Current Features:

* JWT Authentication
* PostgreSQL Database
* User-Specific Notes
* Full CRUD Operations
* Ownership Validation

## Day 14 Improvements

### Database Relationships

Implemented:

- ForeignKey
- relationship()
- One-to-Many Mapping

User
|
|----> Notes

### Response Models

Added Pydantic response models for:

- Better Swagger Documentation
- API Validation
- Consistent Responses

### Refactoring

Created reusable helper function:

get_db_user()

to eliminate duplicate code.

## Day 15

### Router Refactoring

Implemented:
- auth_routes.py
- note_routes.py
- APIRouter
- Modular FastAPI structure

Benefits:
- Cleaner architecture
- Easier maintenance
- Scalable project structure

# Day 16 – Service Layer Architecture

## Objective

Refactor the application to separate business logic from API routes by introducing a Service Layer architecture.

---

## What Was Implemented

### Service Layer

Created a dedicated services package:

```text
app/
├── routers/
│   ├── auth_routes.py
│   └── note_routes.py
│
├── services/
│   ├── auth_service.py
│   └── note_service.py
```

---

### Authentication Service

Created `auth_service.py` containing:

* `register_user()`
* `login_user()`

Responsibilities:

* User registration
* User validation
* Password verification
* JWT token generation

---

### Notes Service

Created `note_service.py` containing:

* `create_note_service()`
* `get_notes_service()`

Responsibilities:

* Note creation
* User-specific note retrieval
* Database operations for notes

---

### Router Refactoring

#### auth_routes.py

Routes now only:

* Receive requests
* Call service functions
* Return responses

Business logic moved to:

```python
auth_service.py
```

---

#### note_routes.py

Routes now only:

* Authenticate users
* Call note service functions
* Return results

Database logic moved to:

```python
note_service.py
```

---

## Benefits of Service Layer Architecture

### Separation of Concerns

Before:

```text
Router
 └── Business Logic
      └── Database Queries
```

After:

```text
Router
 └── Service Layer
      └── Database Queries
```

---

### Improved Maintainability

* Cleaner route files
* Easier debugging
* Easier testing
* Easier feature additions

---

### Industry Standard Design

This architecture follows common FastAPI backend patterns used in:

* Production APIs
* SaaS Applications
* Enterprise Backend Systems
* AI Microservices

---

## Technologies Used

* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* JWT Authentication
* Passlib/Bcrypt
* APIRouter
* Service Layer Pattern

---

## Features Working

### Authentication

* User Registration
* User Login
* JWT Token Generation
* Protected Routes

### Notes

* Create Note
* Get User Notes
* Update Note
* Delete Note
* Ownership Validation

### Documentation

* Swagger UI
* Request Validation
* Response Models

---

## Git Commit

```bash
git commit -m "Day16 service layer architecture completed"
```

---

## Status

Day 16 Completed Successfully

Current Architecture:

```text
Client
  ↓
Router
  ↓
Service
  ↓
Database
```

Ready for:

* Day 17: Environment Variables (.env)
* Day 18: Configuration Management
* Day 19: Exception Handling
* Day 20: Dockerizing FastAPI

```
```
## Day 17

### Environment Variables

Implemented:

- python-dotenv
- .env file
- Secret management
- Database URL configuration

### Files Updated

- database.py
- jwt_handler.py
- .gitignore

### Benefits

- Secure credentials
- Production readiness
- Easier deployment
