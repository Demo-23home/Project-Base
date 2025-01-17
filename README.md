# Project Base

## Table of Contents

- [Overview](#overview)
- [Features](#features)
  - [Authentication](#authentication)
  - [Infrastructure](#infrastructure)
  - [Development Utilities](#development-utilities)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Project Setup](#project-setup)
  - [Docker Setup](#docker-setup)
- [API Documentation](#api-documentation)

## Overview

**Project Base** is a foundational setup designed to serve as a starting point for building scalable and production-ready web applications. It includes essential tools, libraries, and configurations for backend and full-stack projects, facilitating rapid development and deployment. The project is organized into two branches:

- `backend_base`: For backend-only projects.
- `client_base`: For full-stack projects with integrated frontend and backend setups. This branch includes everything in `backend_base` plus a **Next.js** frontend for building modern, server-rendered, and static websites.

## Features

### Authentication

- **Djoser Integration:** Token-based authentication and user management.
- **Social Authentication:** Integration with social login providers.
- **Secure Authentication:** Support for JWT tokens with refresh and access tokens.

### Infrastructure

- **Dockerized Environment:** Includes Docker Compose for multi-container orchestration.
- **Celery and Redis:** Asynchronous task handling and real-time processing.
- **PostgreSQL:** Relational database for scalable data storage.
- **Mailpit:** Email testing and debugging tool.
- **Nginx:** Reverse proxy and load balancing.

### Development Utilities

- **Timestamped Model:** Pre-built timestamped model for database records.
- **Logger:** Comprehensive logging setup for debugging and monitoring.
- **Pre-configured Settings:** Sensible defaults for development and production environments.

## Technologies Used

### Backend

- **Django:** Web framework for building scalable applications.
- **Django REST Framework (DRF):** Toolkit for building Web APIs.
- **Djoser:** Simplifies authentication workflows.
- **Celery & Redis:** Task queue and message broker.
- **PostgreSQL:** Relational database.
- **Mailpit:** Email debugging tool.
- **JWT:** JSON Web Tokens for secure authentication.

### Frontend (Fullstack Base)

- **Next.js:** Framework for building server-side rendered and static websites.
- **React:** Library for building user interfaces.
- **Axios:** HTTP client for API requests.

### DevOps

- **Docker:** Containerization of the application.
- **Docker Compose:** Orchestration of multi-container setups.

## Architecture

The project follows a **modular architecture** to ensure scalability and maintainability. It includes the following layers:

- **Backend API:** Built using Django and DRF for robust API management.
- **Task Queue:** Celery for handling background tasks like sending emails.
- **Database:** PostgreSQL for data persistence.
- **Caching and Messaging:** Redis for in-memory caching and Celery messaging.
- **Reverse Proxy:** Nginx for load balancing and security.
- **Frontend:** Next.js for creating dynamic and static web pages.

## Installation

### Prerequisites

- **Docker & Docker Compose:** Ensure Docker is installed on your machine. [Install Docker](https://docs.docker.com/get-docker/).

### Project Setup

1. **Clone the Repository:**

   ```bash
   git clonehttps://github.com/Demo-23home/Project-Base
   cd Project-Base

2. **Environment Variables:**
Create a .env file in the root directory and add the following variables:
   ```js
    SITE_NAME=""
    ADMIN_URL=""
    DJANGO_SECRET_KEY=""
    EMAIL_PORT="1025"
    EMAIL_HOST="mailpit"
    DEFAULT_FROM_EMAIL=""
    CELERY_FLOWER_USER=""
    CELERY_FLOWER_PASSWORD=""
    CELERY_BROKER_URL="redis://redis:6379/0"
    CELERY_RESULT_BACKEND="redis://redis:6379/0"
    POSTGRES_HOST="postgres"
    POSTGRES_PASSWORD=""
    POSTGRES_DB=""
    POSTGRES_USER=""
    POSTGRES_PORT="5432"
    SIGNING_KEY=""
    COOKIE_SECURE=""
    CLOUDINARY_CLOUD_NAME=""
    CLOUDINARY_API_KEY=""
    CLOUDINARY_API_SECRET=""
    GOOGLE_CLIENT_SECRET=""
    GOOGLE_CLIENT_ID=""
   REDIRECT_URIS="http://localhost:8080/api/v1/auth/google"    
    ```

### Docker Setup

1. **Build and Start Containers:**

   ```bash
   make build
   ```
2. **Access Services:**

    - **Backend API:** http://localhost:8000/api/v1/.
    - **Mailpit UI:** http://localhost:8025/.
    - **Frontend (Fullstack Base):** http://localhost:5000/.
    - **Flower (Celery Tasks UI):** http://localhost:5555/.

### API Documentation

The project includes Swagger and DRF-YASG for API documentation. Access the API docs at:

- Swagger UI: http://localhost:8000/api/v1/redoc/
- Postman : https://documenter.getpostman.com/view/29368996/2sAYQakAss

This base project provides a comprehensive setup to jumpstart your application development with core configuration. Feel free to customize it further to suit your specific requirements.




