# EX01 Developing a Simple Webserver
## Date: 05.05.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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
```

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
httpd.serve_forever()'''

## OUTPUT:
![alt text](<Screenshot 2025-05-05 195104.png>)
![alt text](<Screenshot 2025-05-05 195116.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
