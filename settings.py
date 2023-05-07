import os
from typing import Optional


"""
Environment variables
"""
SECRET_KEY: Optional[str] = os.getenv("SECRET_KEY")
USERNAME: Optional[str] = os.getenv("USERNAME")
PASSWORD: Optional[str] = os.getenv("PASSWORD")
