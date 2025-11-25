"""
Application configuration settings
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Database
    POSTGRES_USER: str = "dte_user"
    POSTGRES_PASSWORD: str = "dte_password"
    POSTGRES_DB: str = "dte_platform"
    DATABASE_URL: Optional[str] = None
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    # RabbitMQ
    RABBITMQ_USER: str = "dte_user"
    RABBITMQ_PASSWORD: str = "dte_password"
    RABBITMQ_URL: Optional[str] = None
    
    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_RELOAD: bool = True
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Celery
    CELERY_BROKER_URL: Optional[str] = None
    CELERY_RESULT_BACKEND: Optional[str] = None
    
    # Scraping
    DEFAULT_TIMEOUT: int = 60
    MAX_RETRIES: int = 5
    DEFAULT_USER_AGENT: str = "Mozilla/5.0 (compatible; DTE-Platform/1.0)"
    
    # Rate Limiting
    DEFAULT_RATE_LIMIT_PER_MINUTE: int = 60
    DEFAULT_RATE_LIMIT_PER_HOUR: int = 1000
    
    # Proxy
    PROXY_LIST: Optional[str] = None
    PROXY_ROTATION_ENABLED: bool = False
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Build DATABASE_URL if not provided
        if not self.DATABASE_URL:
            self.DATABASE_URL = (
                f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@localhost:5432/{self.POSTGRES_DB}"
            )
        
        # Build RABBITMQ_URL if not provided
        if not self.RABBITMQ_URL:
            self.RABBITMQ_URL = (
                f"amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}"
                f"@localhost:5672//"
            )
        
        # Build Celery URLs if not provided
        if not self.CELERY_BROKER_URL:
            self.CELERY_BROKER_URL = self.RABBITMQ_URL
        if not self.CELERY_RESULT_BACKEND:
            self.CELERY_RESULT_BACKEND = self.REDIS_URL


# Global settings instance
settings = Settings()

