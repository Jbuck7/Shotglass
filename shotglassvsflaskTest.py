import time
import pytest
from flask import Flask
from flask.testing import FlaskClient
from shotglass import Shotglass

def flaskfunc(requests):
    avg_time = 0
    pytest.main(["-v"])
    
    @pytest.fixture
    def app():
        app = Flask(__name__)
        
        @app.route('/')
        def index():
            return "TEST"
        
        yield app
    
    @pytest.fixture
    def client(app):
        return app.test_client()
    
    def test(client: FlaskClient):
        response_time = 0
        
        for i in range(requests):
            start = time.time()
            response = client.get('/')
            end = time.time()
            response_time += (end - start)
            
        avg_time = response_time / requests
    
    return avg_time
    
def shotglassfunc(requests):
    app = Shotglass()


def main():
    request_num = 100
    flasktime = flaskfunc(request_num)
    shotglasstime = shotglassfunc(request_num)
    
    
    
main()