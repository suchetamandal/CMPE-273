# CMPE-273
Lab Assignment - 1
Spring Semester 2017
Sucheta Mandal


1. First create a index.html -> $echo "Hello World" > index.html
1. Now Run '$ python -m SimpleHTTPServer' to create a local server.
2. Then create multiple TCP connection by using Apache Benchmarking tool.
   $ab -k -c 4 -n 20 http://localhost:8000
3. Now we can run 'socket-mon.py' to list all tcp connections sorted by their numbers.   
