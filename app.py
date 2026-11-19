import os
from wsgiref.simple_server import make_server


def app(environ, start_response):
    body = b"OK\n"
    headers = [
        ("Content-Type", "text/plain; charset=utf-8"),
        ("Content-Length", str(len(body))),
    ]
    start_response("200 OK", headers)
    return [body]


def run():
    port = int(os.environ.get("PORT", "8080"))
    with make_server("0.0.0.0", port, app) as server:
        server.serve_forever()


if __name__ == "__main__":
    run()
