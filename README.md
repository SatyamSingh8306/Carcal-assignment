# Wimbledon Result Provider API

A FastAPI-based service that uses AI agents to search for and provide Wimbledon final results. The system combines web search capabilities with LLM processing to deliver accurate, structured tournament data.

## Features
- RESTful API with FastAPI
- AI-powered data retrieval using LangChain agents
- Web search integration via Tavily Search API
- LLM processing with Groq for data formatting
- LangSmith integration for comprehensive logging and monitoring
- Type-safe request/response models (Pydantic)
- Modular project structure
- Environment-based configuration
- Automated tests (pytest)
- CORS enabled
- Ready for deployment (Docker, requirements.txt)

## Agent Workflow

The application uses a sophisticated AI agent workflow to retrieve and format Wimbledon results:

### 1. **Agent Search Phase**
- **Tool**: Tavily Search API integration
- **Process**: The agent searches the web for Wimbledon final results for the requested year
- **Configuration**: Uses `TAVILY_API_KEY` for search capabilities
- **Output**: Raw search results containing tournament information

### 2. **LLM Processing Phase**
- **Model**: Groq LLM (configurable via `GROQ_MODEL`)
- **Process**: The raw search data is processed through a structured prompt template
- **Format**: Converts unstructured web data into standardized JSON format
- **Validation**: Ensures data consistency and completeness

### 3. **Data Structuring**
- **Input**: Raw web search results
- **Processing**: LLM extracts and formats:
  - Champion name
  - Runner-up name
  - Match score
  - Number of sets
  - Tiebreak information
- **Output**: Structured `WimbledonResult` object

### 4. **Response Generation**
- **Validation**: Pydantic models ensure type safety
- **Format**: Consistent JSON response structure
- **Error Handling**: Graceful handling of missing or invalid data

### 5. **Logging and Monitoring (LangSmith)**
- **Tracing**: All LLM operations are automatically traced and logged
- **Monitoring**: Real-time visibility into agent performance and LLM interactions
- **Debugging**: Detailed logs for troubleshooting and optimization
- **Analytics**: Performance metrics and usage analytics available in LangSmith dashboard

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
   - Copy `env.example` to `.env` and fill in your API keys:
     ```bash
     cp env.example .env
     ```
   - Update the `.env` file with your actual API keys:
     ```env
     # Server Configuration
     HOST=127.0.0.1
     PORT=8000
     ENV=development
     
     # Groq LLM Configuration
     GROQ_MODEL=llama3-8b-8192
     GROQ_API_KEY=your_actual_groq_api_key
     
     # Tavily Search API Configuration
     TAVILY_API_KEY=your_actual_tavily_api_key
     
     # LangSmith Configuration (Optional - for logging and monitoring)
     LANGSMITH_TRACING=true
     LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
     LANGSMITH_API_KEY=""
     LANGSMITH_PROJECT=""
     ```
   
   **Required API Keys:**
   - **Groq API Key**: Get from [Groq Console](https://console.groq.com/)
   - **Tavily API Key**: Get from [Tavily AI](https://tavily.com/)
   
   **Optional API Keys:**
   - **LangSmith API Key**: Get from [LangSmith](https://smith.langchain.com/) for comprehensive logging and monitoring of LLM operations

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
  Returns the final match result for the given year using AI agent search and LLM processing.

### Example Response
```json
{
  "champion": "Novak Djokovic",
  "runner_up": "Matteo Berrettini", 
  "score": "6–7(4–7), 6–4, 6–4, 6–3",
  "sets": 4,
  "tiebreak": true
}
```

## Testing

Run all tests with:
```bash
pytest
```

## Architecture

### Service Layer
- **`app/services/agent.py`**: LangChain agent configuration with Groq LLM and Tavily search
- **`app/services/mapper.py`**: Data source connector that orchestrates agent search and LLM formatting
- **`app/services/promtps.py`**: Prompt templates for structured data extraction and formatting

### Data Flow
1. **Request** → Route handler (`app/routes/wimbledon.py`)
2. **Search** → Agent searches web using Tavily API
3. **Process** → LLM formats raw data using structured prompts
4. **Validate** → Pydantic models ensure data integrity
5. **Response** → Structured JSON returned to client

## Deployment
- See `requirements.txt` for dependencies.
- Ensure all environment variables are properly configured in production.
- (Optional) Add a `Dockerfile` for containerized deployment.

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

