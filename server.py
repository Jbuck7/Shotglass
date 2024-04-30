from shotglass import Shotglass

app = Shotglass()

@app.route("/",'GET')
def index(client_socket):
    with open('templates/home.html', 'r') as file:
        html_string = file.read()
    response = app.create_response(200, "text/html", html_string)
    app.send_response(client_socket, response)

@app.route("/Development",'GET')
def index(client_socket):
    with open('templates/Development.html', 'r') as file:
        html_string = file.read()
    response = app.create_response(200, "text/html", html_string)
    app.send_response(client_socket, response)

@app.route("/vs",'GET')
def index(client_socket):
    with open('templates/vs.html', 'r') as file:
        html_string = file.read()
    response = app.create_response(200, "text/html", html_string)
    app.send_response(client_socket, response)

@app.route("/documentation",'GET')
def index(client_socket):
    with open('templates/Doc.html', 'r') as file:
        html_string = file.read()
    response = app.create_response(200, "text/html", html_string)
    app.send_response(client_socket, response)

@app.route("/static/num.png",'GET')
def serve_static(client_socket):
    file_path = "static/num.png"
    with open(file_path, 'rb') as file:
        file_data = file.read()
    response = app.create_response(200, "image/png", file_data,{"Content-Length": len(file_data)})
    app.send_response(client_socket, response)

@app.route("/static/time.png",'GET')
def serve_static(client_socket):
    file_path = "static/time.png"
    with open(file_path, 'rb') as file:
        file_data = file.read()
    response = app.create_response(200, "image/png", file_data,{"Content-Length": len(file_data)})
    app.send_response(client_socket, response)

@app.route("/static/cpu.png",'GET')
def serve_static(client_socket):
    file_path = "static/cpu.png"
    with open(file_path, 'rb') as file:
        file_data = file.read()
    response = app.create_response(200, "image/png", file_data,{"Content-Length": len(file_data)})
    app.send_response(client_socket, response)

@app.route("/static/style.css",'GET')
def serve_static(client_socket):
    file_path = "static/style.css"
    with open(file_path, 'r') as file:
        file_data = file.read()
    response = app.create_response(200, "text/css", file_data)
    app.send_response(client_socket, response)

@app.errorhandler(404)
def page_not_found(client_socket):
    with open('templates/404.html', 'r') as file:
        html_string = file.read()
    response = app.create_response(200, "text/html", html_string)
    app.send_response(client_socket, response)

app.run()