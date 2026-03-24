# Connectly Django API
Connectly is a backend REST API built with Django and Django REST Framework for managing users and posts. 

It demonstrates core backend concepts such as CRUD operations, validation, relational data handling, API security, and scalable design patterns. The system also includes social features like likes, comments, Google OAuth authentication, and a personalized news feed with sorting, pagination, caching, and access control. All endpoints were tested using Postman.

## Project Branch
The **final and latest tested version** of this project is located in the branch:
**main**

All features for Terminal Assessment (RBAC, Privacy Setiings, Pagination and Cache) were consolidated, merged, committed, and pushed to this branch.

To use the latest version of the project:
```bash
Switch to the main branch and pull the latest version

git checkout main
git pull origin main
```
## AI Disclosure Statement
AI tools (such as ChatGPT) were used to assist with documentation formatting, explanation of concepts, and guidance for testing API endpoints.  

All system design, implementation, testing, and integration of features (CRUD operations, validation, relationships, security, design patterns, likes, comments, Google OAuth, and news feed functionality) were implemented and verified by the project team.


## Project Overview

Connectly is a simplified social media backend API that allows users to create posts, interact through likes and comments, authenticate using Google OAuth, and view a personalized news feed.

The project demonstrates key backend engineering concepts including REST API design, database relationships, authentication, security, pagination, and scalable architecture patterns.


## Features
### Core API Features
- CRUD operations for Users and Posts
- Input validation for API requests
- Relational data integrity using Django models
- Secure authentication
- Password encryption
- HTTPS support
### Access Control & Security
- Role-Based Access Control (RBAC)
   Admin and authors can delete posts
   Regular users are restricted from unauthorized actions
- Privacy Settings
   Private posts are only visible to their owners
   Unauthorized access returns 403 Forbidden
### Social Interaction Features
- Users can like posts
- Users can comment on posts
- Retrieve comments per post
- Post details include:
   like count
   comment count
### Authentication
- JWT Token Authentication
- Google OAuth integration
### News Feed System
- Personalized feed endpoint
- Sorting by date (latest/oldest)
- Pagination support
### Design Patterns
- Singleton Pattern
    Used for shared configuration and logging
- Factory Pattern
    Used for modular object creation (posts/comments)



## Tech Stack
Backend Framework
- Django

API Framework
- Django REST Framework

Authentication
- JWT + Google OAuth (django-allauth)
  
Database
- SQLite (development)

Testing Tool
- Postman Postman (API testing)


## Setup & Run
1. Clone the repo
   ```
   git clone https://github.com/Laizeu/IPT-TA.git
   ```

2. Navigate to the folder
   ```
   cd IPT-TA
   ```

3. Switch to the Final Project Branch
   ```
   git checkout main
   git pull origin main
   ```

4. Create and activate virtual environment

   **Mac/Linux**
   ```
   python3 -m venv env
   source env/bin/activate
   ```
   **Windows**
   > Install Python and create the virtual environment:
   > ```
   > uv python install 3.12
   > uv venv env
   > env\Scripts\activate
   > ```

5. Install dependencies

   **Mac/Linux**
   ```
   pip install -r requirements.txt
   ```
   **Windows (with uv)**
   ```
   uv pip install -r requirements.txt
   ```

6. Run migrations
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Create a Superuser (for authentication testing)
   ```
   python manage.py createsuperuser
   ```

8. Start server

   Standard server
   ```
   python manage.py runserver
   ```
   HTTPS server
   ```
   python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
   ```
   Server will run at:
   `http://127.0.0.1:8000/`


## API Endpoints

### Base URL
`http://127.0.0.1:8000`

### Users
```text
- GET /posts/users/            # Retrieve all users
- POST /posts/users/create/    # Create a new user
```
Sample Request Body
```json
{
  "username": "laizallanto",
  "email": "laiza@email.com",
  "password": "laiza123!"
}
```
Sample Response
```json
{
    "id": 1,
    "username": "Laiza",
    "email": "laiza@email.com",
    "is_staff": true
}
```
### Posts
```text
- GET /posts/posts/                         # Retrieve all posts
- POST /posts/posts/create                  # Create a new post
- PUT /posts/{id}/update/ – Update post     # Update post 
- DELETE /posts/{id}/delete/ – Delete post  # Delete post
```
Sample Request Body
```json
{
  "title": "This is Laiza and this is my private post",
  "content": "This post is from User A.",
  "post_type": "text",
  "privacy": "private"
}
```
Sample Response
```json
{
    "id": 48,
    "title": "This is Laiza and this is my private post",
    "content": "This post is from User A.",
    "post_type": "text",
    "metadata": {},
    "image": null,
    "video": null,
    "author": "Laiza",
    "created_at": "2026-03-22T14:08:00.418342Z",
    "comments": [],
    "like_count": 0,
    "comment_count": 0,
    "privacy": "private"
}
```
### Likes
```text
- POST  /posts/{id}/like/          # Like a post
```
Sample Response
```json
{
  "message": "Post liked successfully"
}
```
### Comments
```text
- POST /posts/{id}/comment/         # Add comment to a post
- GET /posts/{id}/comments/         # Retrieve comments for a post
```
Sample Request Body
```json
{
  "id": 12,
  "content": "This is comment by User A.",
  "comment_type": "text"
}
```
Sample Response
```json
{
    "id": 1,
    "content": "This is comment by User A",
    "comment_type": "text",
    "metadata": {},
    "image": null,
    "video": null,
    "author": "Laiza",
    "post": 12,
    "created_at": "2026-03-19T14:01:47.897324Z",
    "like_count": 0
}
```
### Authentication
```text
- POST  /api/token/                          # Request authentication token
- POST  /auth/google/login/                  # Google OAuth login
- GET   /accounts/google/login/              # Start Google OAuth login
- GET   /accounts/google/login/callback/     # Google OAuth callback
```
### Example Token Request
POST /api/token/

Request Body
```json
{
  "username": "laiza",
  "password": "yourpassword"
}
```
Response
```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```
Authenticated requests must include the token in the header:
Authorization: Bearer <access_token>

### News Feed
```text
- GET   /posts/feed/                         # Retrieve personalized news feed
- GET   /posts/feed/?ordering=-created_at    # Sort posts by newest
- GET   /posts/feed/?page=1                  # Pagination (page 1)
- GET   /posts/feed/?page=2                  # Pagination (page 2)
```
### Example News Feed Request
`GET /posts/feed/?page=1&ordering=-created_at`
Returns a paginated list of posts ordered by newest first.

Example Feed Response
```json
{
    "count": 17,
    "next": "http://127.0.0.1:8000/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 48,
            "title": "This is Adrian and this is my public post",
            "content": "This post is from User A.",
            "post_type": "text",
            "metadata": {},
            "image": null,
            "video": null,
            "author": "adriansanjuan",
            "created_at": "2026-03-22T14:08:00.418342Z",
            "comments": [],
            "like_count": 0,
            "comment_count": 0,
            "privacy": "public"
        }
    ]
}
```
### Access Control Example
Regular user deletes another user's post → 403 Forbidden
Author deletes own post → Allowed
Admin deletes any post → Allowed

### Error Handling
400 Bad Request – Invalid input
401 Unauthorized – Missing/invalid token
403 Forbidden – Permission denied
404 Not Found – Resource not found

## Testing

All API endpoints were thoroughly tested using **Postman**, covering authentication, access control, privacy logic, pagination, and performance optimization.

The following features were tested:
### Authentication & Token Handling
- Successful token request (Admin, User A, User B)
- Failed requests with invalid or missing tokens

### Role-Based Access Control (RBAC)
- Successful post deletion by Admin
- Failed post deletion by regular user
- Failed post deletion without authentication
- Successful comment deletion by Admin
- Failed comment deletion by regular user

### Privacy & Access Control
- Successful retrieval of public posts
- Successful retrieval of private posts by owner
- Failed retrieval of private posts by other users
- Failed retrieval of private posts without authentication

### News Feed Behavior
- Feed returns only public posts for other users
- Feed includes private posts of the owner
- Feed excludes private posts of other users

### Post Creation & Privacy Settings
- Successful post creation (public and private)
- Failed post creation with invalid privacy value
- Successful privacy update by owner
- Failed privacy update by non-owner

### Pagination & Sorting (Homework 9)
- Successful feed retrieval across multiple pages (Page 1, Page 2)
- Correct pagination size
- No duplicate posts across pages
- Sorting by date remains consistent with pagination
- Invalid page parameter handling
- Non-existent page handling

### Caching & Performance Optimization
- Cache miss verification
- Cache hit verification
- Cache invalidation after:
  - Post creation
  - Post update
  - Post deletion
- Response time comparison (before vs after caching)

### Error Handling
- Invalid token requests
- Requests for non-existent resources
- Proper HTTP status codes (400, 401, 403, 404)

Both successful and error scenarios were verified.

### Test Evidence

Screenshots and exported Postman collections for the tests can be found here:

Testing Documentation:
`https://drive.google.com/drive/folders/1Ph3LuYumNyb9kFcHDuTRMb7iYCR0VeXH?usp=sharing`

Contents include:
- Postman API request/response screenshots
- Exported JSON Postman Collection file

## File Structure
```text
connectly_project/
├── connectly_project/        # Django project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── posts/                    # Core API logic (posts, likes, comments, feed)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── factories/                # Factory Design Pattern for creating objects
│   ├── __init__.py
│   ├── comment_factory.py
│   └── post_factory.py
│
├── singletons/               # Singleton Design Pattern implementations
│   ├── config_manager.py
│   └── logger_singleton.py
│
├── tests/                    # Unit tests for design patterns
│   ├── __init__.py
│   ├── test_post_factory.py
│   └── test_singleton.py
│
├── manage.py                 # Django management script
├── requirements.txt          # Python project dependencies
└── .gitignore                # Ignored files and folders
```
## Updated Diagrams
`https://drive.google.com/drive/folders/1PBhcYlST7C8tglbjHCMsY2x0ng30EL3h?usp=sharing`

## Requirements

- Python 3.10+
- Django
- Django REST Framework
- django-allauth (Google OAuth)
- SQLite (development database)

## Project Status

Terminal Assessment - Completed
Includes:
- RBAC
- Privacy Settings
- Pagination
- Caching

### Author
```md
IPT Group 10
```
