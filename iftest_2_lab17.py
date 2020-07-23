
# if BOOLEAN EXPRESSION:
 #   STATEMENTS
# A few important things to note about if statements:

# ipchk = "192.168.0.1"
# a string tests as True if ipchk:  print("Looks like the IP address was set: " + ipchk)  use .format method to display
# changed format to - print('Looks like the IP address was set to {}'.format(ipchk))

ipchk = "192.168.0.1"

if ipchk:
    print('Looks like the IP address was set to {}'.format(ipchk))

# var ipchk is set by the user

ipchk = input("Apply an IP address: ") # this line now prompts the user for input # 10.0.0.2

# a provided string will test true
if ipchk:
    print('Looks like the IP address was set to {}'.format(ipchk))  # output looks like the IP address was set to 10.0.0.2

ipchk = input("Apply an IP address: ") # prompts user input
if ipchk:
    print('Looks like the IP address was set to {}'.format(ipchk))
else:
    print("You did not provide input.")


ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# if user set IP of gateway
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk: # if any data is provided, this will test true
   print("Looks like the IP address was set: " + ipchk) # indented under if
else: # if data is NOT provided
   print("You did not provide input.") # indented under else

ipchk = input ('Apply an IP address: ')
if ipchk == "192.168.70.1":
   print('Looks like the IP address of the Gateway was set: {}. This is not recommended'.format(ipchk))
elif ipchk:
    print("Looks like the IP address was set to {}".format(ipchk))
else:
    print("You did not provide input.")

