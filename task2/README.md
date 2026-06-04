# Task 2: Auth System (Registration, Login, Dashboard)

A minimalist full-stack application implementing a user authentication flow and a personalized dashboard.

## Tech Stack

- **Backend**: Python 3, FastAPI, Uvicorn
- **Frontend**: Next.js, Tailwind CSS, TypeScript
- **UI Style**: Minimalist Black & White, Rounded UI/UX

## Project Structure

```
task2/
├── backend/
│   ├── main.py            # FastAPI application logic
│   └── requirements.txt   # Python dependencies
└── frontend/
    ├── app/               # Next.js App Router pages
    ├── package.json       # Node.js dependencies
    └── tailwind.config.js # UI styling configuration
```

## Getting Started

### Backend

1. Navigate to the backend folder:
   ```bash
   cd task2/backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

### Frontend

1. Navigate to the frontend folder:
   ```bash
   cd task2/frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:3000`.

## Features

- **Registration**: Create a new user account.
- **Login**: Securely authenticate users.
- **Dashboard**: Personalized welcome screen upon successful login.