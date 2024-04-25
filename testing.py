from shotglass import Shotglass

app = Shotglass()

@app.route("/")
def index(client_socket):
    with open('templates/home.html', 'r') as file:
        html_string = file.read()
    response = app.create_response(200, "text/html", html_string)
    app.send_response(client_socket, response)

@app.route("/static/style.css")
def serve_static(client_socket):
    file_path = "static/style.css"
    with open(file_path, 'r') as file:
        file_data = file.read()
    response = app.create_response(200, "text/css", file_data)
    app.send_response(client_socket, response)

@app.errorhandler(404)
def page_not_found(e):
    return app.render_template('404.html'), 404

app.run()