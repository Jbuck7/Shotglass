import socket
import threading
import time
import pytest
from shotglass import Shotglass

class ShotglassClient:
    def __init__(self, host = "0.0.0.0", port=80):
        self.host = host
        self.port = port
    
    def send_request(self, request):
        start = time.time()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.host, self.port))
            client.sendall(request.encode())
            response = client.recv(1024)
        end = time.time()
        response_time = end - start
        return response, response_time

@pytest.fixture
def server():
    server = Shotglass()
    thread = threading.Thread(target=server.run)
    thread.start()
    
    yield server
    
    server.server_socket.close()
    
@pytest.fixture
def client():
    return ShotglassClient()

def test_response_time(server, client):
    requests = 100
    total_response_time = 0
    
    for i in range(requests):
        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        response, response_time = client.send_request(request)
        total_response_time += response_time
    
    avg_response_time = total_response_time / requests
    print("Average response time for shotglass: " + str(avg_response_time))
    num_request_per_sec = int(60 / avg_response_time)
    print("Number of GET request for shotglass per second: " + str(num_request_per_sec))

if __name__ == "__main__":
    pytest.main(["-v"])
        