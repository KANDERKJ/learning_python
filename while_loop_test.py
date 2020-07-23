# count-controlled while loop

print('The IP of the server is?')
server = input('Enter in IP address')
port1 = int(input('The server start port is'))
port2 = int(input('The server end port is?'))
while port1 <= port2:
    print('server {} : {}'.format(server, port1))
    port1 += 1  #  port1 = port1 + 1 the first statement is short hand notation
# display output as follows
# The IP of the server is?
# Enter in IP address 192.168.0.2
# The server start port is 5060
# The server end port is? 5069
# server  192.168.0.2 : 5060
# server  192.168.0.2 : 5061
# server  192.168.0.2 : 5062
# server  192.168.0.2 : 5063
# server  192.168.0.2 : 5064
# server  192.168.0.2 : 5065
# server  192.168.0.2 : 5066
# server  192.168.0.2 : 5067
# server  192.168.0.2 : 5068
# server  192.168.0.2 : 5069

# while loop examples
i = 0
while i < 100:
    print('i = {}'.format(i * 2))
    i+= 1

