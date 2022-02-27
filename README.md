# Web Server

## Description

This is a web server program that accepts HTTP requests and sends the requested resource along with HTTP response headers. If the requested resource does not exist, then the server sends an HTTP 404 message to the client.

## Running the Server

The syntax for running the server is as follows: <br><br>
``python webserver.py -r [root-directory] -p [port-number] `` <br>
The ``-p`` argument is optional. The server listens on port 80 by default. This is the standard port number for HTTP.

## Connecting to the Server

To connect to the server, open a web browser and type in the following in the address bar (filling in the appropriate info as needed): <br>
``[server-IP]:[port-number]/[path-to-resource].[file-extension]``
