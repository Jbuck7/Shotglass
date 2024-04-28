import time as t
import pytest
from shotglass import Shotglass

app = Shotglass()

class fakeSocket:
    def send(self, data):
        pass

@app.route("/", "GET")
def test_response_time():
    request = 100
    
    def get_request(socket):
        data = "TEXT"
        response = app.create_response(200, "text/html", data)
        Shotglass.send_response(app, socket, response)
    
    start = t.time()
    
    for i in range(request):
        get_request(fakeSocket())
        
    end = t.time()
    
    time = (end - start) / request
    num_get_request_per_sec = int(60 / time)
    print("\nAverage response time for shotglass: " + str(time))
    print("Number of GET request for shotglass per second: " + str(num_get_request_per_sec))

if __name__ == "__main__":
    pytest.main(["-v"])
