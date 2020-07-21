import time
tuple_record = ('etho', 'AA:BB:DD:11:12', '192.168.0.1', '5060', 'UDP')
print(tuple_record)
print(tuple_record * 2)
print(tuple_record[1])
print(tuple_record[0])

tuple_record = ('etho, AA:BB:DD:11:12, 192.168.0.1, 5060, UDP')
print(tuple_record)
print(tuple_record[1])

#list is mutable
# the immutable of tuple limits the functionality, only two methods can be used


local_time = time.localtime(time.time())
print(local_time)
print(type(local_time))
print(local_time[0])    # year
print(local_time[1])    # month
print(local_time[0:3])  #year, month, day
print(local_time[2])    #day
print(local_time[3])    #hour
print(local_time[4])    #minute
print('The year is {}'.format(local_time[0]))
print(f' The month is : {local_time[1]}')
print(f' The day is {local_time[2]}')
print('The hour is {}'.format(local_time[3]))
print('The minute is', local_time[4])
print('{}/{}/{}'.format(local_time[0], local_time[1], local_time[2]))
x, y = 10,20
x, '+', y, '=', x + y
print(x, '+', y, '=', x+y)