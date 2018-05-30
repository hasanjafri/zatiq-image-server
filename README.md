# zatiq-image-server
Zatiq Image Service for Mobile App

# STEPS TO RUN LOCALLY:
git clone https://github.com/hasanjafri/zatiq-image-server.git
cd zatiq-image-server

python3 -m venv ./venv
Windows: (using git bash): source venv/Scripts/activate
Mac/Linux: source venv/bin/activate

pip install -r requirements.txt
export FLASK_ENV=development
export FLASK_APP=application.py
flask run
