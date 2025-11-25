"""
FastAPI application entry point
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings

# Create FastAPI app
app = FastAPI(
    title="Distributed Task Execution Platform",
    description="A horizontally scalable web scraping and data collection platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Distributed Task Execution Platform API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "api"
    }


@app.get("/api/v1/status")
async def api_status():
    """API status endpoint"""
    return {
        "api": "running",
        "version": "1.0.0",
        "environment": {
            "database_url": settings.DATABASE_URL.split("@")[-1] if settings.DATABASE_URL else "not configured",
            "redis_url": settings.REDIS_URL,
            "rabbitmq_url": settings.RABBITMQ_URL.split("@")[-1] if settings.RABBITMQ_URL else "not configured"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_RELOAD
    )

