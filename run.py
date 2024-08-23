from app import app
from prometheus_client import start_http_server

if __name__ == '__main__':
    start_http_server(8002)
    app.run(host='0.0.0.0', port=5002)
