from datetime import datetime

def app(environ, start_response):
    now = datetime.now()
    string_time = "Current time: " + now.strftime("%H:%M:%S %d.%m.%Y")
    data = bytes(string_time, 'utf-8')
    start_response("200 OK", [
        ("Content-Type", "text\plain"),
        ("Content-Length", str(len(data)))
        ])
    return iter([data])
