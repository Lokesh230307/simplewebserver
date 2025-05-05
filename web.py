from http.server import HTTPServer, BaseHTTPRequestHandler


content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Simple Web Server Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            padding: 20px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        p {
            text-align: center;
            font-size: 21px;
        }
        h3 {
            color: #FFA500;
            text-align: center;
            font-size: 16px;
        }
        .back-button {
            position: absolute;
            top: 20px;
            left: 20px;
            padding: 10px 16px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        .back-button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <button class="back-button" onclick="history.back()">← Back</button>
    <h1>Shopify with me</h1>
    <p>Only for men</p>
    <h3>No discount</h3>
</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler): 
    def do_GET(self):
         print("request received") 
         self.send_response(200) 
         self.send_header('content-type', 'text/html; charset=utf-8')
         self.end_headers() 
         self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()