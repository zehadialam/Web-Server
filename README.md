# Web Server

## Description

This is a web server program that accepts HTTP requests and sends the requested resource along with HTTP response headers. If the requested resource does not exist, then the server sends an HTTP 404 message to the client.

## Running the Server

The syntax for running the server is as follows: <br>
```
python webserver.py -r [root-directory] -p [port-number] 
``` 
The ```-p``` argument is optional. The server listens on port 80 by default. This is the standard port number for HTTP.

## Connecting to the Server

To connect to the server, open a web browser and type in the following in the address bar (filling in the appropriate info as needed): <br>
```
[server-IP]:[port-number]/[path-to-resource].[file-extension]
```
Example: ```128.238.251.26:6789/HelloWorld.html```

## Example Output
```
python webserver.py -r content -p 12000
```

```
128.238.251.26 is serving on port 12000

Received message from ('128.101.125.111', 51614)

Request Message:

GET /test.html HTTP/1.1
Host: 172.18.180.36
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: keep-alive
Upgrade-Insecure-Requests: 1

Response Headers:

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 152
Date: 2022-02-27 18:37:15


****************************************************************
```
