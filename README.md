# Wimbledon Result Provider API

A FastAPI-based service to provide Wimbledon final results. Designed for extensibility, maintainability, and industry readiness.

## Features
- RESTful API with FastAPI
- Type-safe request/response models (Pydantic)
- Modular project structure
- Environment-based configuration
- Automated tests (pytest)
- CORS enabled
- Ready for deployment (Docker, requirements.txt)

## Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables:**
   - Create a `.env` file in the root directory (see example below):
     ```env
     HOST=127.0.0.1
     PORT=8000
     ENV=development
     ```

## Running the Application

```bash
python -m app
```

Or with Uvicorn directly:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

## API Usage

- **Root:** `GET /`  
  Returns a welcome message.
- **Wimbledon Final Result:** `GET /wimbledon/?year=<year>`  
  Returns the final match result for the given year.

## Testing

Run all tests with:
```bash
pytest
```

## Deployment
- See `requirements.txt` for dependencies.
- (Optional) Add a `Dockerfile` for containerized deployment.

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

