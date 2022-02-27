"""
Name: Zehadi Alam
Description: This is a web server program that uses TCP connections
The following code has been adapted from: Computer Networking: A Top Down Approach
by Jim Kurose and Keith Ross.
"""

import argparse
import codecs
import datetime
import mimetypes
import os
import socket
import sys


def webserver(port, directory):
    """Webserver using TCP socket."""
    host_name = socket.gethostbyname(socket.gethostname())
    port_number = port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((host_name, port_number))
        server_socket.listen(1)
    except OSError as error_msg:  # handles case where port number supplied is being used by other process
        print(error_msg)
        sys.exit(1)
    print(f'{host_name} is serving on port {port_number}\n')
    img_extensions = ['.jpg', '.jpeg', '.tiff', '.gif', '.png', '.bmp', '.webp']
    while True:
        connection_socket, addr = server_socket.accept()
        print('Received message from', str(addr), '\n')
        try:
            socket_data = connection_socket.recv(4096).decode()
            print('Request Message: \n')
            print(socket_data)
            try:
                file_path = os.path.basename(str(directory)) + socket_data.split()[1]
                response_headers = {
                    'Content-Type': mimetypes.guess_type(socket_data.split()[1])[0],
                    'Content-Length': os.path.getsize(file_path),
                    'Date': f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
                }
                response_headers_extracted = ''.join(
                    f'{header}: {content}\r\n' for header, content in response_headers.items())
                print('Response Headers: \n')
                print('HTTP/1.1 200 OK')
                print(response_headers_extracted, '\n')
                print('****************************************************************')
                if os.path.splitext(file_path)[1] in img_extensions:
                    file = open(file_path, 'rb')
                    data_from_file = file.read()
                    file.close()
                    connection_socket.send(b'HTTP/1.1 200 OK\r\n')
                    connection_socket.send(response_headers_extracted.encode(encoding='UTF-8'))
                    connection_socket.send(b'\r\n')
                    connection_socket.send(data_from_file)
                else:
                    file = open(file_path)
                    with codecs.open(file_path, 'r', encoding='UTF-8', errors='ignore') as file_data:
                        data_from_file = file_data.read()
                    file.close()
                    connection_socket.send(b'HTTP/1.1 200 OK\r\n')
                    connection_socket.send(response_headers_extracted.encode(encoding='UTF-8'))
                    connection_socket.send(b'\r\n')
                    for i in range(0, len(data_from_file)):
                        connection_socket.send((data_from_file[i]).encode())
            except IndexError:
                print('There was an issue with printing the request message. Trying again...')
        except IOError:
            print('Response Headers: \n')
            print('HTTP/1.1 404 Not Found')
            print('****************************************************************')
            connection_socket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
            connection_socket.send(b'<html><title>404 Not Found</title><h1>404: Not Found</h1></html>\r\n')
        connection_socket.close()


def parse_argument():
    """Creates a command-line interface for taking arguments."""
    parser = argparse.ArgumentParser(description='Start a web server')
    parser.add_argument('-r', dest='OBJECT_DIR', type=str, required=True, help='Root directory for files')
    parser.add_argument('-p', dest='PORT', type=int, default=80,
                        help='The port number on which the server will be listening for incoming connections')
    the_args = parser.parse_args()
    return the_args


def main():
    """main method"""
    args = parse_argument()
    webserver(args.PORT, args.OBJECT_DIR)


if __name__ == '__main__':
    main()
