#!/usr/bin/env python3
"""
Gunicorn configuration for Render deployment
"""

import os

# Server socket
bind = f"0.0.0.0:{os.environ.get('PORT', '5005')}"
backlog = 2048

# Worker processes - use 1 worker for in-memory state consistency
workers = 1
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 2

# Restart workers after this many requests, with up to 50% jitter
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process naming
proc_name = "sianglao-backend"

# Application
wsgi_module = "app:app"

# Preload application
preload_app = True