# FastAPI + SQLite Form Handler with Fetch API

A complete example of sending form data from JavaScript to FastAPI and storing it in SQLite.

## Project Structure

```
.
├── main.py              # FastAPI application with POST endpoint
├── database.py          # SQLite database configuration
├── models.py            # SQLAlchemy ORM model
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html      # Frontend with Fetch API
└── forms.db            # SQLite database (auto-generated)
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/emmanuelmarlelopiyong-sudo/fastapi-sqlite-fetch-js.git
   cd fastapi-sqlite-fetch-js
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
uvicorn main:app --reload
```

Open your browser and go to:
```
http://127.0.0.1:8000
```

## How It Works

1. **Frontend (index.html)**:
   - HTML form with fields: name, email, message
   - JavaScript fetch API sends form data as JSON to the backend
   - Shows success/error messages

2. **Backend (main.py)**:
   - POST `/submit` endpoint receives JSON data
   - Validates data using Pydantic
   - Stores data in SQLite database
   - Returns success response

3. **Database**:
   - SQLite database with `form_data` table
   - Stores: id, name, email, message
   - Auto-created on first run

## API Endpoints

### GET /
Returns the HTML form page.

### POST /submit
Receives form data as JSON and saves to database.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello World"
}
```

**Response:**
```json
{
  "message": "Form data saved successfully",
  "id": 1,
  "data": {
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello World"
  }
}
```

### GET /records
Returns all saved records from the database.

## Technologies Used

- **FastAPI**: Web framework
- **SQLAlchemy**: ORM for database operations
- **SQLite**: Database
- **Pydantic**: Data validation
- **Jinja2**: Template rendering
- **Fetch API**: Frontend HTTP requests
