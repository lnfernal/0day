#!/usr/bin/env python3

import socket
import threading

"""
If a client connects to the server successfully without sending any request, it blocks others' connections. Even though clients send ata as soon as possible,
the server cannot handle other requests if there is no client trying to establish a connction. Handling multiple requests is inefficient because it 
wastes a lot of time waiting for I/O responses from hardware such as network interfaces.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 5566))
s.listen(10)

while True:
	conn, addr = s.accept()
	msg = conn.recv(1024)
	conn.send(msg)

"""

"""
One possible solution to prevent a server waiting for I/O operations is to dispatch tasks to other threads. The tradeoff is that numerous
threads may consume all computing power without high throughput. Even worse, an application may waste time waiting for a lock to process tasks
in critical sections. 
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1",5566))
s.listen(10240)

def handler(conn):
	while True:
		msg = conn.recv(65535)
		conn.send(msg)

while True:
	conn, addr = s.accept()
	t = threading.Thread(target=handler, args=(conn,))
	t.start()