class Request:
    def __init__(self, text_request):
        self.method, self.path, self.http_version = text_request.split(' ', 2)
        self.headers = {}
        self.body = ''

        # Parse headers and body from the text request
        lines = text_request.split('\r\n')
        i = 1  # Skip the first line (method, path, http_version)
        while i < len(lines) and lines[i] != '':
            header, value = lines[i].split(': ', 1)
            self.headers[header] = value
            i += 1
        if i < len(lines):
            self.body = '\r\n'.join(lines[i+1:])

    def get_header(self, name):
        return self.headers.get(name)

    def get_body(self):
        return self.body

# response.py
class Response:
    def __init__(self, status_code, content_type, content, headers=None, version="HTTP/1.1"):
        self.version = version
        self.status_code = status_code
        self.content_type = content_type
        self.content = content
        self.headers = headers if headers else {}