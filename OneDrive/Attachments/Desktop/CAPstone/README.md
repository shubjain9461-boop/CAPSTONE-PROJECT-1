# Internal DevOps Utilities API

A FastAPI-based internal utilities application for monitoring system metrics, AWS S3 bucket information, and other DevOps operations.

## Features

- **System Metrics**: Real-time system metrics monitoring (CPU, memory, disk usage)
- **AWS S3 Integration**: List and categorize S3 buckets by creation date
- **RESTful API**: Clean, documented endpoints with FastAPI
- **Auto-reload**: Development server with auto-reload on code changes

## Project Structure

```
.
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── app/
│   ├── __init__.py
│   └── api.py             # FastAPI application setup
├── routers/
│   ├── __init__.py
│   ├── metrics.py         # System metrics endpoints
│   └── aws.py             # AWS S3 endpoints
└── services/
    ├── __init__.py
    ├── metrics_service.py # System metrics logic
    └── aws_service.py     # AWS S3 operations
```

## Prerequisites

- Python 3.8+
- AWS credentials configured (for S3 operations)

## Installation

1. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

2. **Activate virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python main.py
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

### Health Check
- **GET** `/`
  - Returns: `{"message": "hello dosto this is devops"}`

### System Metrics
- **GET** `/metrics`
  - Returns system metrics (CPU, memory, disk usage, etc.)
  - Status: 200
  - Error handling: 500 on failure

### AWS S3 Buckets
- **GET** `/bucket-info`
  - Returns S3 bucket information categorized by age
  - Response:
    ```json
    {
      "total_buckets": 5,
      "new_buckets": ["bucket1", "bucket2"],
      "old_buckets": ["bucket3", "bucket4", "bucket5"]
    }
    ```
  - Buckets created in last 30 days are classified as "new"
  - Status: 200
  - Error handling: 500 on failure

## Documentation

Interactive API documentation available at:
- **Swagger UI**: `http://127.0.0.1:8000/doc`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Configuration

### AWS Setup

Ensure AWS credentials are configured:
- Set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables, or
- Configure `~/.aws/credentials` file, or
- Use IAM role if running on EC2

Required S3 permissions:
- `s3:ListAllMyBuckets`

## Dependencies

- **fastapi**: Web framework for building APIs
- **uvicorn**: ASGI server
- **boto3**: AWS SDK for Python
- **psutil**: System and process utilities

## Troubleshooting

### AWS Bucket Info Returns Error
- Verify AWS credentials are configured
- Check IAM permissions for S3 ListBucket access
- Ensure boto3 is properly installed

### Metrics Endpoint Not Working
- Verify psutil is installed
- Check system permissions for reading metrics

### Port Already in Use
- Change the default port in `main.py` or use:
  ```bash
  uvicorn app.api:app --host 0.0.0.0 --port 8001
  ```

## Development

The development server automatically reloads on code changes. Watch the console for updates.

```
metrics imported
route added
router included
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## License

Internal use only
