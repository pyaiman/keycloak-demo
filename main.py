from flask import Flask, render_template, request, redirect
from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenIDConnection
import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor
import json

app = Flask(__name__)


@app.route('/')
async def hello():
    keycloak_connection = KeycloakOpenIDConnection(
                        server_url="http://localhost:8080/",
                        username='admin',
                        password='admin',
                        realm_name="master",
                        client_id="admin-cli",
                        client_secret_key="client-secret",
                        verify=True)

    keycloak_admin = KeycloakAdmin(connection=keycloak_connection)
    
    t = await keycloak_admin.a_get_users()

    

    content = await keycloak_admin.a_get_users()

    print(t)

    return render_template('home.html', data=content)

@app.route('/create/', methods=['GET', 'POST'])
async def create():
    error = ''
    if request.method == 'POST':

        keycloak_connection = KeycloakOpenIDConnection(
                            server_url="http://localhost:8080/",
                            username='admin',
                            password='admin',
                            realm_name="master",
                            client_id="admin-cli",
                            client_secret_key="client-secret",
                            verify=True)

        keycloak_admin = KeycloakAdmin(connection=keycloak_connection)
        try:
            create = await keycloak_admin.a_create_user({"email": request.form['email'],
                                            "username": request.form['username'],
                                            "enabled": True if 'enabled' in request.form.keys() else False,
                                            "firstName": request.form['firstName'],
                                            "lastName":request.form['lastName'] })
        except Exception as e:
            error = json.loads(e.error_message).get('errorMessage', 'Unknown error occured')
            return render_template('create.html', error=error)

        return redirect("/", code=302)

    return render_template('create.html', error=error)
