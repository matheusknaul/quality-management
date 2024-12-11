import os

"""Start mode"""

DEBUG=True

"""Upload configs"""

UPLOAD_FOLDER = './uploads'
MAX_CONTENT_LENGTH = 32 * 1024 * 1024
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'png', 'jpeg', 'docx'}

"""Autorized URLs"""

CORS_ORIGINS = [
    "http://localhost:3000"
]

