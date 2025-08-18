git clone https://github.com/yourusername/incident-management
cd incident-management

docker build -t incident-app .
docker run -p 5000:5000 --env-file .env incident-app

Step 4: Initialize DB (inside container or locally)

from app import db, create_app
app = create_app()
app.app_context().push()
db.create_all()