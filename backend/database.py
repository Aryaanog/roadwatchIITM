import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. The code looks for a system variable named 'DATABASE_URL'.
# If it doesn't find it (which is true on your local machine), it uses your local string.
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:aryaan@localhost:5432/roadwatch_data"
)

# 2. Production protocol compatibility handler
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 3. Core Engine Initialization with Cloud Performance Optimization
# pool_pre_ping=True automatically tests connections and recycles dead ones (critical for serverless DBs)
if "localhost" not in DATABASE_URL:
    engine = create_engine(
        DATABASE_URL, 
        pool_pre_ping=True,
        pool_recycle=300
    )
else:
    engine = create_engine(DATABASE_URL)

# 4. Request lifecycle session management
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()