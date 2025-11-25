# Distributed Task Execution Platform
## Web Scraping & Data Collection Platform

A horizontally scalable, distributed web scraping platform built with Python, Celery, RabbitMQ, Redis, and Docker. Process 100k+ scraping jobs/day with intelligent rate limiting, proxy rotation, and real-time monitoring.

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for local development)

### Step 1: Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd DTE-Platform

# Copy environment file
cp env.example .env

# Edit .env file with your configurations (optional for local dev)
```

### Step 2: Start Services with Docker Compose

```bash
# Start all services (PostgreSQL, Redis, RabbitMQ, API)
docker-compose up -d

# Check if all services are running
docker-compose ps
```

### Step 3: Access Services

- **FastAPI API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **RabbitMQ Management UI**: http://localhost:15672
  - Username: `dte_user`
  - Password: `dte_password`
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

### Step 4: Test the API

```bash
# Health check
curl http://localhost:8000/health

# API status
curl http://localhost:8000/api/v1/status
```

---

## 📁 Project Structure

```
DTE-Platform/
├── api/                    # FastAPI application
│   ├── main.py            # API entry point
│   └── routes/            # API routes (to be added)
├── workers/               # Celery workers
│   └── (to be implemented)
├── storage/               # Database models
│   └── (to be implemented)
├── config/                # Configuration
│   └── settings.py       # App settings
├── docker/                # Docker files
│   └── Dockerfile.api
├── tests/                 # Test files
├── docker-compose.yml     # Docker services
├── requirements.txt       # Python dependencies
└── README.md
```

---

## 🛠️ Development Setup

### Local Development (without Docker for API)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start services (PostgreSQL, Redis, RabbitMQ)
docker-compose up -d postgres redis rabbitmq

# Run API locally
python -m api.main
# or
uvicorn api.main:app --reload
```

---

## 📊 Current Status

### ✅ Phase 1: Core Infrastructure (COMPLETED)
- [x] Project structure setup
- [x] Docker Compose configuration
- [x] FastAPI application with health checks
- [x] Configuration management
- [x] PostgreSQL, Redis, RabbitMQ services

### 🔄 Next Steps (Phase 2)
- [ ] Database models and migrations
- [ ] Celery worker setup
- [ ] Job submission API endpoints
- [ ] Basic scraping functionality

---

## 🔧 Configuration

All configuration is managed through environment variables. See `env.example` for available options.

Key configurations:
- **Database**: PostgreSQL connection settings
- **Redis**: Cache and deduplication
- **RabbitMQ**: Message broker for task queues
- **Scraping**: Timeouts, retries, rate limits

---

## 📝 API Endpoints

### Current Endpoints
- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/v1/status` - API status

### Coming Soon
- `POST /api/v1/jobs` - Submit scraping job
- `GET /api/v1/jobs/{job_id}` - Get job status
- `GET /api/v1/jobs` - List all jobs
- `GET /api/v1/stats` - Platform statistics

---

## 🐳 Docker Services

The platform runs the following services:

1. **postgres**: PostgreSQL database
2. **redis**: Redis cache
3. **rabbitmq**: RabbitMQ message broker
4. **api**: FastAPI application

---

## 📚 Documentation

- [Technical Specification](./TECHNICAL_SPEC.md) - Complete technical details
- [API Documentation](http://localhost:8000/docs) - Interactive API docs (when running)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

MIT License

---

## 🎯 Features (Planned)

- ✅ Basic infrastructure setup
- 🔄 Priority queues (high/normal/low)
- 🔄 Per-domain rate limiting
- 🔄 Proxy rotation
- 🔄 URL deduplication
- 🔄 Auto-retry with exponential backoff
- 🔄 Real-time admin dashboard
- 🔄 Auto-scaling based on queue depth

---

**Status**: Phase 1 Complete - Ready for Phase 2 implementation