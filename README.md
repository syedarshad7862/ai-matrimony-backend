# AI-Powered Muslim Matrimonial Matchmaking System

An AI-powered backend for a Muslim matrimonial matchmaking platform, built with **FastAPI, MongoDB, Qdrant, LangChain, Google Gemini, and Hugging Face embeddings**.

The system combines matrimonial profile data, vector-based semantic search, and LLM-based matchmaking to retrieve and process potentially compatible profiles.

---

## 🚀 Project Overview

This project provides the backend APIs for an AI-powered Muslim matrimonial matchmaking system.

The backend is responsible for:

- User authentication and authorization
- Matrimonial profile management
- Profile data storage using MongoDB
- Profile vector generation
- Semantic profile search using Qdrant
- AI-powered matchmaking using Google Gemini
- Structured matchmaking responses
- Dashboard statistics
- Admin operations
- Profile image/media handling using Cloudinary
- Docker-based deployment

The application is built using **FastAPI** and follows a modular backend structure with separate authentication, database, model, function, and route modules.

---

## ✨ Key Features

### 🔐 Authentication & Authorization

- JWT-based authentication
- Protected API endpoints
- Authenticated database access
- User/session handling
- Role-based backend access

### 👤 Matrimonial Profile Management

- Create matrimonial profiles
- Retrieve profile information
- Manage profile data
- Store profile information in MongoDB
- Profile image/media management

### 🤖 AI-Powered Matchmaking

The matchmaking system combines:

- Profile preprocessing
- Text chunk generation
- Embeddings
- Qdrant vector search
- Semantic profile retrieval
- Google Gemini / LLM processing
- Structured AI output

### 🔎 Semantic Vector Search

Profile information is converted into vector representations and stored/searchable through **Qdrant**.

This allows the system to retrieve profiles based on semantic similarity rather than depending only on exact keyword matching.

### 📊 Dashboard

The backend provides dashboard-related functionality for profile statistics and platform information.

### 👨‍💼 Admin APIs

Dedicated admin routes are included for administrative operations.

### ☁️ Cloudinary Integration

Cloudinary is used for profile/media management.

---

# 🧠 AI Matchmaking Architecture

```text
                    User Profile
                         │
                         ▼
                ┌─────────────────┐
                │    MongoDB      │
                │ Profile Storage │
                └────────┬────────┘
                         │
                         ▼
                Profile Processing
                         │
                         ▼
                ┌─────────────────┐
                │ Text / Chunks   │
                │ Generation      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Embeddings    │
                │   Generation    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     Qdrant      │
                │ Vector Database │
                └────────┬────────┘
                         │
                         ▼
                Relevant Profiles
                         │
                         ▼
                ┌─────────────────┐
                │ LangChain +     │
                │ Google Gemini   │
                └────────┬────────┘
                         │
                         ▼
                AI Matchmaking
                         │
                         ▼
                Structured Output
                         │
                         ▼
                    API Response
```

---

# 🔄 Matchmaking Workflow

The main matchmaking process is implemented through:

```text
POST /match/show-matches
```

The backend performs the following steps:

```text
1. Authenticate the user
        ↓
2. Select the matrimonial profile
        ↓
3. Retrieve the selected profile from MongoDB
        ↓
4. Create profile text chunks
        ↓
5. Perform semantic search using Qdrant
        ↓
6. Retrieve relevant candidate profiles
        ↓
7. Send retrieved profiles to the LLM matchmaking layer
        ↓
8. Process the LLM response
        ↓
9. Transform the response into structured match profiles
        ↓
10. Return the matches through the API
```

The implementation separates these responsibilities into dedicated functions for:

- Chunk generation
- Vector generation
- Vector search
- AI matchmaking
- Response structuring

---

# 🔍 Vector Search with Qdrant

This project uses **Qdrant** as the vector database for semantic profile search.

The vector-search pipeline is:

```text
Matrimonial Profiles
        ↓
Profile Text
        ↓
Embeddings
        ↓
Qdrant
        ↓
Similarity Search
        ↓
Relevant Profiles
```

Qdrant replaced the earlier FAISS-based vector search implementation.

The backend provides an endpoint for generating the profile vectors:

```text
POST /match/create-vectors
```

This endpoint creates the Qdrant indexes/vectors required by the matchmaking system.

---

# 🧩 Backend Architecture

The backend is organized into separate modules:

```text
ai-matrimony-backend/
│
├── auth/
│   └── Authentication dependencies
│
├── database/
│   └── Database configuration
│
├── functions/
│   ├── chunks.py
│   ├── extract_text_from_pdf.py
│   ├── generate_vectors.py
│   ├── match_making.py
│   ├── search_vector.py
│   └── structure_output.py
│
├── models/
│   └── Pydantic schemas
│
├── routes/
│   ├── auth.py
│   ├── dashboard.py
│   ├── user_profile.py
│   ├── match_profile.py
│   ├── admin.py
│   └── download.py
│
├── app.py
├── cloudinary_config.py
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Backend Framework | FastAPI |
| Programming Language | Python |
| Database | MongoDB |
| Vector Database | Qdrant |
| LLM | Google Gemini |
| LLM Framework | LangChain |
| Embeddings | Hugging Face / Sentence Transformers |
| Authentication | JWT |
| Validation | Pydantic |
| Media Storage | Cloudinary |
| API Server | Uvicorn |
| Containerization | Docker |
| Environment Management | python-dotenv |

---

# 📦 Main Dependencies

The project uses the following major libraries:

```text
FastAPI
Uvicorn
MongoDB / PyMongo / Motor
Qdrant Client
LangChain
LangChain Qdrant
LangChain Google GenAI
LangChain HuggingFace
Sentence Transformers
Transformers
PyJWT
python-jose
Passlib
Cloudinary
Pydantic
python-dotenv
```

---

# 📁 Project Structure

### `auth/`

Contains authentication-related dependencies and access-control logic.

### `database/`

Contains database-related configuration and MongoDB access.

### `functions/`

Contains the core AI and vector-search functionality.

Important modules include:

```text
chunks.py
generate_vectors.py
search_vector.py
match_making.py
structure_output.py
```

### `models/`

Contains Pydantic schemas used for request and response validation.

### `routes/`

Contains the FastAPI API routes.

Main route modules include:

```text
auth.py
dashboard.py
user_profile.py
match_profile.py
admin.py
download.py
```

### `app.py`

The main FastAPI application.

The application registers the major API routers and configures CORS middleware.

---

# 📡 API Modules

The backend is divided into the following API modules:

| Module | Purpose |
|---|---|
| Authentication | Login, authentication and access control |
| Dashboard | Dashboard and profile statistics |
| User Profile | Matrimonial profile operations |
| Match | AI-powered matchmaking and vector operations |
| Admin | Administrative operations |
| Download | Download-related functionality |

---

# 🤖 Match API

The matchmaking router uses the `/match` prefix.

### Find Profiles

```text
GET /match/find
```

Used to retrieve available matrimonial profiles for the matching flow.

### Show Matches

```text
POST /match/show-matches
```

This is the primary AI matchmaking endpoint.

It:

1. Retrieves the selected profile.
2. Generates profile chunks.
3. Performs Qdrant semantic search.
4. Retrieves relevant profiles.
5. Sends the retrieved information to the AI matchmaking layer.
6. Structures the AI response.
7. Returns the matched profiles.

### Create Vectors

```text
POST /match/create-vectors
```

Creates the Qdrant vectors/indexes required for semantic profile search.

---

# 🗄️ Data Architecture

The application uses two main data layers.

## MongoDB

MongoDB acts as the primary application database.

It stores application and matrimonial profile information.

```text
Application Data
      ↓
   MongoDB
```

## Qdrant

Qdrant stores/searches vector representations used for semantic profile retrieval.

```text
Profile Information
      ↓
   Embeddings
      ↓
    Qdrant
```

The two databases have different responsibilities:

```text
                 Application
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
      MongoDB                Qdrant
   Structured Data       Vector Search
```

---

# 🔐 Authentication

The backend uses JWT-based authentication to protect API resources.

Authenticated requests are handled through backend dependencies that provide access to the authenticated user and database context.

Protected operations include profile and matchmaking functionality.

---

# ☁️ Cloudinary

Cloudinary is integrated into the backend for media management.

Configuration is loaded through environment variables:

```env
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

---

# ⚙️ Environment Variables

Create a `.env` file in the project root.

Example:

```env
MONGO_URI=your_mongodb_connection_string

GOOGLE_API_KEY=your_google_gemini_api_key

QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key

CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
```

> **Important:** Never commit your `.env` file or API keys to GitHub.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/syedarshad7862/ai-matrimony-backend.git
```

Move into the project directory:

```bash
cd ai-matrimony-backend
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file:

```bash
.env
```

Add the required MongoDB, Gemini, Qdrant, and Cloudinary configuration.

---

# ▶️ Run the Application

Start the FastAPI development server:

```bash
uvicorn app:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI provides interactive API documentation automatically.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

The Swagger UI can be used to test the available API endpoints.

---

# 🐳 Docker

The project includes a Dockerfile and uses Python 3.11 as the base image.

Build the Docker image:

```bash
docker build -t ai-matrimony-backend .
```

Run the container:

```bash
docker run -p 8000:8000 ai-matrimony-backend
```

For deployment environments that provide a `PORT` environment variable, the Docker configuration starts Uvicorn using that port.

---

# 🔄 AI Matching Pipeline

A simplified representation of the matching pipeline:

```text
                 User
                  │
                  ▼
          Select Matrimonial
              Profile
                  │
                  ▼
              MongoDB
                  │
                  ▼
          Profile Processing
                  │
                  ▼
        Text Chunk Generation
                  │
                  ▼
             Embeddings
                  │
                  ▼
              Qdrant
                  │
                  ▼
        Semantic Profile Search
                  │
                  ▼
        Relevant Candidate Data
                  │
                  ▼
        LangChain + Gemini
                  │
                  ▼
         AI Matchmaking Logic
                  │
                  ▼
         Structured Response
                  │
                  ▼
                API
```

---

# 🧠 AI Components

## LangChain

LangChain is used as part of the LLM application layer and integrates the vector-search and model components.

## Google Gemini

Gemini is used for the LLM-based matchmaking stage.

The retrieved profile information is processed by the matchmaking layer before the final structured response is returned.

## Hugging Face Embeddings

Hugging Face / Sentence Transformers are used for generating embeddings that support semantic vector search.

## Qdrant

Qdrant provides the vector storage and similarity-search layer for matrimonial profiles.

---

# 🔒 Security Considerations

The project uses:

- JWT authentication
- Protected API routes
- Environment variables for secrets
- MongoDB authentication
- Qdrant API configuration
- Cloudinary API credentials
- CORS configuration

For production deployment, secrets should always be stored securely and never committed to source control.

---

# 📈 Future Improvements

Possible future improvements include:

- Advanced compatibility scoring
- Reciprocal preference matching
- Improved profile ranking
- Hybrid semantic + structured filtering
- AI-generated match explanations
- Match history
- Recommendation feedback
- Profile quality analysis
- Improved vector-search ranking
- Automated testing
- Production monitoring and logging
- Rate limiting
- API versioning

---

# 🎯 Project Goals

The main goal of this project is to explore how **Generative AI, semantic search, vector databases, and backend engineering** can be combined to build a practical matrimonial matchmaking system.

The project demonstrates experience with:

- REST API development
- FastAPI backend architecture
- MongoDB
- Vector databases
- Semantic search
- Embeddings
- LangChain
- LLM integration
- AI-powered recommendations
- JWT authentication
- Cloudinary integration
- Docker

---

# 👨‍💻 Author

**Syed Arshad**

Full Stack Developer | Python Backend Developer | GenAI Developer

### GitHub

https://github.com/syedarshad7862

### LinkedIn

https://linkedin.com/in/syed-arshad-9a9967253

### Portfolio

https://syedarshad7862.github.io/arshad/

---

# ⭐ Project

If you find this project useful or interesting, consider giving the repository a ⭐.

---

## 📄 License

This project is intended for educational and development purposes.
