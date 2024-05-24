# Demo Flask application to test Python keycloak Async Functions

This simple flask application is to showcase some of the async functions implemented in python keycloak library. This project make use of get and create user APIs to list and create keycoak users.

## Setup 
1. Clone the python-keycloak "async_feature" branch
2. Clone this repo.
3. Create a virtual environment with "python -m venv keycloak-env"
4. Activate the virtual environment with command "source keycloak-env/bin/activate"
5. Go the python-keycloak environment and run "pip install ." to install the library from local.
6. In another terminal, Run the keycloak server using docker with "docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:24.0.3 start-dev"
7. Go to keycloak-demo directory and install requirements with "pip install -r requirements.txt"
8. Run "export FLASK_APP=main.py"
9. Run "flask run" to launch the application
10. Go to http://localhost:5000 in your browser to see the application.
