import time
import pytest
from flask import Flask
from flask.testing import FlaskClient
    
@pytest.fixture
def app():
    app = Flask(__name__)
        
    @app.route('/')
    def index():
        return 'TEST'
        
    yield app
    
@pytest.fixture
def client(app):
    return app.test_client()
    
def test_response_time(client: FlaskClient):
    requests = 100
    response_time = 0
    for i in range(requests):
        start = time.time()
        response = client.get('/')
        end = time.time()
        response_time += (end - start)
            
    avg_time = response_time / requests
    print("\nAverage response time: " + str(avg_time))
    num_get_request_per_sec = int(60 / avg_time)
    print("Number of GET request for flask per second: " + str(num_get_request_per_sec))
    
if __name__ == "__main__":
    pytest.main(["-v"])
