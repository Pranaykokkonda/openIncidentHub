## 🚨 Incident Management System

A lightweight, open-source portal to **log, track, assign, and resolve incidents** (infrastructure or application-related) with **role-based access**, **REST APIs**, **email notifications**, and **Docker support**.

---
## 📌 Features

🔐 Role-based access (Admin, user, viewer)

🌐 REST API for incident management

✉️ Email notifications (SMTP)

🖥️ Web UI (Flask + Bootstrap)

📊 Incident status tracking

🗃️ SQLite for persistent storage

🐳 Dockerized deployment

---
## 🛠️ Tech Stack
| Component        | Technology        |
| ---------------- | ----------------- |
| Backend          | Python + Flask    |
| Frontend         | HTML + Bootstrap  |
| Database         | SQLite            |
| Auth & Roles     | Flask-Login       |
| Email Service    | Flask-Mail + SMTP |
| Containerization | Docker            |

---
## 🚀 Getting Started
### 1. Clone the Repo

```bash
git clone https://github.com/Pranaykokkonda/openIncidentHub.git
```
```bash
cd openIncidentHub
```

### 2. Update your `.env` and `register.html`  Files

### • Update your `.env` file with :

- MAIL_USERNAME=<Your-gmail>
- MAIL_DEFAULT_SENDER=<your-gmail>
- MAIL_PASSWORD=<app-password>

🔐 Setting Up **MAIL_PASSWORD** for Gmail SMTP (you’ll need to generate an App Password:)

• Visit https://myaccount.google.com/apppasswords

• Enter app name and click on create

• A new password will be generated copy it and paste in .env (at **MAIL_PASSWORD=**)

 
### • Update your `register.html` file with :
  Go to `app/templates/register.html` and update details with your **username, email_id and password**

---
### 3. 🚀 Deploying the Application
## Using Docker

```bash
docker build . -t open  
```
```bash
docker images  
```
```bash
docker run -p 80:5000 open:latest
```
```bash
docker ps  
```

## Using Manual Setup via Command Line
🛠️ *Install essential Python development tools and package manager (pip).*
```bash
apt install python3-dev python3-pip
```

📦 *Install the `venv` module to create isolated Python environments.*
```bash
apt install python3-venv
```

🧪 *Create a new virtual environment named `openincidenthub`.*
```bash
python3 -m venv openincidenthub
```

🚀 *Activate the virtual environment to install packages and run Python code in isolation mode.*
```bash
source openincidenthub/bin/activate
```

📦 *Install all required Python packages listed in `requirements.txt` file.*
```bash
pip install -r requirements.txt
```

🚀 *Run the Flask application using `run.py` file.*
```bash
python run.py
```

---
### 🌐 Access the Application in Browser
🐳 **`If you deployed Application via Docker`:** 

*Open your browser and navigate to:* **`http://<your-server-ip>`**

.

💻 **`If you deployed Application via Manual Commands`:**

*Open your browser and navigate to:* **`http://<your-server-ip>:5000`**

---

