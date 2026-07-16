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



## Day 18

### Configuration Management

Created:

app/core/config.py

Features:

- Centralized settings
- Single source of truth
- Environment variable management
- Production-ready configuration

Benefits:

- Easier maintenance
- Cleaner imports
- Better scalability
- Simplified deployment


## Day 19

### Global Exception Handling

Created:

- custom_exceptions.py
- handlers.py

Implemented:

- UserAlreadyExistsException
- UserNotFoundException
- InvalidCredentialsException
- InvalidTokenException
- NoteNotFoundException

Benefits:

- Cleaner code
- Centralized error handling
- Consistent API responses
- Production-ready architecture

## Day 20 - Dockerization

### Completed
- Created Dockerfile
- Containerized FastAPI application
- Connected FastAPI container to PostgreSQL
- Configured environment variables
- Built Docker image
- Ran application inside Docker

### Run

docker build -t notes-api .

docker run -d -p 8000:8000 notes-api

### Swagger

http://localhost:8000/docs


## Running Tests

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_auth.py -v
```

## Day 24 – Role-Based Access Control (RBAC)

### Features
- Added role column to users
- Admin/User roles
- Authorization dependency
- Protected admin endpoint
- RBAC tests


# Day 27 – Background Tasks

## Features

- FastAPI BackgroundTasks
- Non-blocking Email Simulation
- Activity Logging
- Async Processing

## Workflow

Client

↓

POST /register

↓

User Created

↓

Response Returned

↓

Background Tasks

↓

Email

↓

Logs

# Day 28 – API Security

## Features

- Login Rate Limiting
- Registration Rate Limiting
- CORS Configuration
- Trusted Host Middleware
- Security Headers

## Protection

- Brute Force Prevention
- Spam Registration Prevention
- Browser Security


# Day 29 – Logging & Monitoring

## Features

- Console Logging
- File Logging
- Authentication Logs
- Notes Activity Logs
- Exception Logs
- Request Logging Middleware

## Log Levels

- DEBUG
- INFO
- WARNING
- ERROR


# AI Engineering Journey

A production-style FastAPI backend built while learning AI Engineering.

---

## Features

- JWT Authentication
- User Registration & Login
- Notes CRUD API
- Role-Based Authorization
- Redis Caching
- Background Tasks
- Email Notifications
- Logging
- Rate Limiting
- API Documentation
- Local AI Integration using Ollama
- Prompt Engineering

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis
- Docker
- JWT
- Ollama
- OpenAI SDK

---

## AI Features

The project integrates a local Large Language Model using Ollama.

Supported AI Modes:

- general
- backend
- python
- interviewer

---

## Install Ollama

Download:

https://ollama.com

Pull model

```bash
ollama pull llama3.2:3b
```

Run

```bash
ollama run llama3.2:3b
```

---

## Run Backend

```bash
uvicorn main:app --reload
```

---

## AI Endpoint

POST

```
/ai/chat
```

Request

```json
{
    "prompt":"Explain JWT",
    "mode":"backend"
}
```

Response

```json
{
    "mode":"backend",
    "response":"JWT stands for JSON Web Token..."
}
```

---

## Project Structure

```
app
│
├── ai
│   ├── client.py
│   ├── prompts.py
│
├── services
│   ├── ai_service.py
│   ├── auth_service.py
│   └── note_service.py
│
├── routers
│   ├── ai_routes.py
│   ├── auth_routes.py
│   └── note_routes.py
│
├── core
├── exceptions
├── models.py
├── schemas.py
└── main.py
```

---

## Future Work

- Conversation Memory
- RAG
- ChromaDB
- FAISS
- LangChain
- AI Agents
- Tool Calling
- MCP
- Multi-Agent Systems


## day 33

## Conversation Memory

The AI supports multi-turn conversations.

Each conversation is identified by a unique `session_id`.

Conversation history is stored in Redis and automatically loaded before sending requests to the AI model.

## AI APIs

### Chat

POST

```
/ai/chat
```

Request

```json
{
    "session_id":"chat1",
    "prompt":"Explain JWT",
    "mode":"backend"
}
```

---

### Get History

GET

```
/ai/history/{session_id}
```

---

### Delete History

DELETE

```
/ai/history/{session_id}
```

## Redis

Redis is used for:

- Notes caching
- Conversation memory

## AI Modes

- general
- backend
- python
- interviewer

# AI Engineering Journey - FastAPI Notes API with AI Assistant

## Project Overview

This project is a production-style FastAPI backend developed as part of my AI Engineering Journey.

It began as a Notes Management API and has evolved into an AI-powered backend supporting:

- JWT Authentication
- Role-Based Authorization
- PostgreSQL Database
- Redis Caching
- AI Chat Assistant
- Persistent Conversation Memory
- Background Tasks
- Logging
- Rate Limiting
- Docker Integration

---

# Features

## Authentication

- User Registration
- User Login
- JWT Token Authentication
- Password Hashing using bcrypt

---

## Notes Module

- Create Note
- Get Notes
- Update Note
- Delete Note

Redis is used to cache notes for improved response times.

---

## AI Assistant

Supports multiple AI modes:

- General Assistant
- Backend Development
- Python Programming
- Technical Interview Preparation

The AI is powered by a locally hosted Ollama model.

---

## Persistent Conversation Memory

Conversation history is permanently stored in PostgreSQL while Redis acts as a high-speed cache.

Architecture:

```
User

↓

FastAPI

↓

Redis Cache

↓

PostgreSQL

↓

Ollama
```

Benefits:

- Multi-turn conversations
- Persistent chat history
- Automatic Redis cache refresh
- Faster repeated requests

---

# Conversation APIs

## Chat with AI

POST

```
/ai/chat
```

Example Request

```json
{
    "session_id": "chat1",
    "prompt": "Explain JWT Authentication",
    "mode": "backend"
}
```

---

## Get Cached Conversation

GET

```
/ai/history/{session_id}
```

Returns the conversation currently stored in Redis.

---

## Clear Cached Conversation

DELETE

```
/ai/history/{session_id}
```

Deletes the Redis cache for the session.

---

## List All Conversations

GET

```
/ai/conversations
```

Returns every conversation stored in PostgreSQL.

---

## Get Conversation

GET

```
/ai/conversation/{session_id}
```

Returns the complete conversation history from PostgreSQL.

---

## Delete Conversation

DELETE

```
/ai/conversation/{session_id}
```

Deletes conversation from:

- PostgreSQL
- Redis Cache

---

# Redis Usage

Redis is used for:

- Notes Cache
- Conversation Cache

Cache Strategy:

```
Redis

↓

Cache Miss

↓

PostgreSQL

↓

Refresh Redis

↓

Return Response
```

---

# PostgreSQL Tables

Current tables:

- users
- notes
- conversations
- chat_messages

Relationship:

```
Conversation

↓

1

↓

Many

↓

ChatMessage
```

---

# AI Modes

Supported AI modes:

- general
- backend
- python
- interviewer

Each mode uses a different system prompt.

---

# Logging

Application logs include:

- User Authentication
- Notes Operations
- Redis Cache Hits
- Redis Cache Misses
- PostgreSQL Reads
- PostgreSQL Writes
- AI Requests
- AI Responses
- Conversation Creation
- Conversation Deletion

---

# Tech Stack

Backend

- FastAPI
- Python

Database

- PostgreSQL
- SQLAlchemy

Cache

- Redis

Authentication

- JWT
- bcrypt

AI

- Ollama
- OpenAI Compatible API

Documentation

- Swagger UI
- OpenAPI

Deployment

- Docker

---

# Project Structure

```
app
│
├── ai
│   ├── client.py
│   ├── prompts.py
│
├── core
│   ├── logging_config.py
│   ├── redis.py
│   ├── limiter.py
│   ├── roles.py
│
├── routers
│   ├── auth_routes.py
│   ├── note_routes.py
│   ├── admin_routes.py
│   ├── ai_routes.py
│
├── services
│   ├── auth_service.py
│   ├── note_service.py
│   ├── ai_service.py
│   ├── memory_service.py
│   ├── conversation_db_service.py
│
├── exceptions
│
├── models.py
├── schemas.py
├── database.py
├── config.py
│
main.py
```

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Docker

```bash
docker compose up -d
```

---

## Start Ollama

```bash
ollama serve
```

Run your preferred model:

```bash
ollama run gemma2:2b
```

---

## Start FastAPI

```bash
uvicorn main:app --reload
```

---

# API Documentation

Swagger UI

```
http://localhost:8000/docs
```

OpenAPI JSON

```
http://localhost:8000/openapi.json
```

---

# Current Progress

Completed Features:

- JWT Authentication
- Notes CRUD
- PostgreSQL Integration
- Redis Caching
- Background Tasks
- Logging
- Role-Based Authorization
- AI Chat
- Prompt Engineering
- Conversation Memory
- Persistent Conversation Storage

---

# Upcoming Features

- Retrieval Augmented Generation (RAG)
- PDF Chat
- Vector Database
- Embeddings
- Semantic Search
- AI Agents
- Multi-Agent Workflows
- Model Context Protocol (MCP)