from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Открываем и читаем содержимое файла contacts.html
        with open('contacts.html', encoding='utf-8') as f:
            html = f.read()
        # Отправляем статус 200 (ОК)
        self.send_response(200)
        # Устанавливаем заголовок Content-Type как text/html с кодировкой utf-8
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        # Отправляем содержимое файла в ответ
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    # Запускаем сервер на порту 8000
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('Сервер запущен на http://localhost:8000')
    httpd.serve_forever()
