import socket
from HTTP import Request, Response

class Shotglass:
    def __init__(self, port=80, host="0.0.0.0"):
        self.port = port
        self.host = host
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.error_handlers = {}
        self.routes = {}

    def route(self, path, request_type='GET'):
        def decorator(func):
            if path not in self.routes:
                self.routes[path] = {}
            self.routes[path][request_type] = func
            return func
        return decorator

    def errorhandler(self, error_code):
        def decorator(func):
            self.error_handlers[error_code] = func
            return func
        return decorator
        

    # def send_file(self, client_socket, file_path, content_type):
    #     print("sending")
    #     with open(file_path, 'rb') as file:
    #         file_data = file.read()
    #     response = self.create_response(200, content_type, file_data)
    #     self.send_response(client_socket, response)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server is listening on {self.host}:{self.port}")

    def handle_request(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            try:
                text_request = client_socket.recv(1500).decode('utf-8')
            except Exception as e:
                print(f"Error receiving request: {str(e)}")
                continue
            try:
                request = Request(text_request)
            except Exception as e:
                print(f"Error parsing request: {str(e)}")
                continue
            print(request.method)
            print(request.path)
            if request.method == 'GET':
                self.handle_get_request(client_socket, request)
            elif request.method == 'POST':
                self.handle_post_request(client_socket, request)
            else:
                error_response = self.create_response(501, "text/plain", "Not Implemented")
                self.send_response(client_socket, error_response)
            client_socket.close()

    def handle_get_request(self, client_socket, request):
        if request.path in self.routes:
            self.routes[request.path]['GET'](client_socket)
        else:
            self.error_handlers[404](client_socket)


    def handle_post_request(self, client_socket, request):
        if request.path in self.routes:
            self.routes[request.path]['POST'](client_socket, request)
        else:
            error_response = self.create_response(404, "text/plain", "Not Found")
            self.send_response(client_socket, error_response)

    # def get_content_type(self, file_path):
    #     content_type = "text/plain"
    #     if file_path.endswith(".html"):
    #         content_type = "text/html"
    #     elif file_path.endswith(".css"):
    #         content_type = "text/css"
    #     elif file_path.endswith(".js"):
    #         content_type = "application/javascript"
    #     return content_type

    def create_response(self, status_code, content_type, content, headers=None):
        return Response(status_code, content_type, content, headers)

    def send_response(self, client_socket, response):
        http_response = f"{response.version} {response.status_code} OK\r\n"
        http_response += "Content-Type: {}\r\n".format(response.content_type)
        for header, value in response.headers.items():
            http_response += "{}: {}\r\n".format(header, value)
        http_response += "\r\n"
        if type(response.content) == str:
            response.content = response.content.encode()
        encoded = http_response.encode() + response.content
        client_socket.send(encoded)
        

    def run(self):
        self.start()
        self.handle_request()
