import sys
import os

# Add the flask-project directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'flask-project'))

from app import app

if __name__ == "__main__":
    app.run()
