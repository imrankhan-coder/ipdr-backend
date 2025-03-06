# IPDR Backend

## Overview
The IPDR Backend is a FastAPI-based service designed to manage and store NAT logs from MikroTik PPPoE users. It utilizes Elasticsearch for efficient log storage and retrieval and provides secure authentication mechanisms.

## Features
- FastAPI-powered backend
- Stores NAT logs in Elasticsearch
- Secure authentication with OAuth 2.0, LDAP, and SAML
- Multi-tenancy support
- RESTful API endpoints for log retrieval
- Role-based access control for law enforcement agencies

## Prerequisites
- Ubuntu 22.04
- Python 3.10+
- Elasticsearch 8+
- Redis (for caching, optional)
- Nginx (as a reverse proxy, optional)

## Installation
### 1. Clone the Repository
```sh
cd /var/www
git clone https://github.com/imrankhan-coder/ipdr-backend.git
cd ipdr-backend
```

### 2. Create a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```ini
ELASTICSEARCH_HOST=http://localhost:9200
ELASTICSEARCH_INDEX=ipdr-logs
SECRET_KEY=your-secret-key
AUTH_METHOD=oauth2  # Options: oauth2, ldap, saml
LOG_RETENTION_DAYS=180
```

### 5. Start the Backend
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Deployment (Systemd Service)
### 1. Create a Systemd Service File
```sh
sudo nano /etc/systemd/system/ipdr-backend.service
```
Add the following content:
```ini
[Unit]
Description=IPDR Backend FastAPI Service
After=network.target

[Service]
User=root
WorkingDirectory=/var/www/ipdr-backend
ExecStart=/var/www/ipdr-backend/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

### 2. Enable and Start the Service
```sh
sudo systemctl daemon-reload
sudo systemctl enable ipdr-backend
sudo systemctl start ipdr-backend
```

## API Endpoints
- `GET /logs` - Retrieve stored NAT logs
- `POST /logs` - Store new logs
- `GET /auth/me` - Get current user details
- `POST /auth/login` - Authenticate user

## Logs and Debugging
Check logs using:
```sh
sudo journalctl -u ipdr-backend --no-pager --lines=50
```

## Contribution
Pull requests are welcome. Please follow the coding standards and provide detailed commit messages.

## License
This project is licensed under the MIT License.

