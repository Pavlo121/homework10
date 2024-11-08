import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Обробник запитів
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Відправляємо текстове повідомлення клієнту
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World! This is a multi-threaded server.")

# Функція для запуску сервера
def run_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on port 8080...")
    httpd.serve_forever()

# Створюємо кілька потоків для одночасного обслуговування клієнтів
def start_server_in_thread():
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True  # сервер буде автоматично зупинятися при завершенні програми
    server_thread.start()

if __name__ == "__main__":
    start_server_in_thread()
    # Сервер буде працювати в окремому потоці, тому можна додати додаткову логіку тут, якщо потрібно.
    input("Press Enter to stop the server...\n")
