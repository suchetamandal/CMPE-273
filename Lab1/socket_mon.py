import psutil
import operator

#collect all tcp connections
tcp_conections= psutil.net_connections(kind='tcp')
process_dict = {}

for tcp_con in tcp_conections:
    if tcp_con.laddr and tcp_con.raddr:
        if tcp_con.pid in process_dict:
            process_dict[tcp_con.pid] += 1; #If the pid is already present in dictionary; increase it's counter
        else:
            process_dict[tcp_con.pid] = 1; # add a new entry


#Sort dictionary
sorted_process_dict = sorted(process_dict.items(),key= operator.itemgetter(1))

#print output
print "\"pid\",\"laddr\",\"raddr\",\"status\""
for proc in sorted_process_dict:
    for con in tcp_conections:
        if con.laddr and con.raddr:
            if con.pid == proc[0]:
                updated_op = "\"{0}\",\"{1}@{2}\",\"{3}@{4}\",\"{5}\"".format(con.pid,con.laddr[0],con.laddr[1],con.raddr[0],con.raddr[1],con.status)
                print (updated_op)