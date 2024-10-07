# Virtual Environment
python3 -m venv venv
source venv/bin/activate
deactivate **to stop**

# Update Dependencies
pip install -r requirements.txt

# Saving New Dependencies to Requirements File
pip freeze > requirements.txt

# Uvicorn Command
uvicorn main:app --reload

# Docker
docker-compose up -d
