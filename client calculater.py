import socket
serverip='127.0.0.1'
serverport=12800
BUFFER_SIZE=1024
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
opp=['+','-','*','/']
while 1:
   x=input("number 1 :")
   y=input("number 2 :")
   op=input('input operation (+,-,*,/)')
   if op=='+':op='add'
   if op=='-':op='sub'
   if op=='*':op='mul'
   if op=='/':op='div'
   message=(op+' '+x+' '+y)
   client.sendto(message.encode('utf-8'),(serverip,serverport))
   response,address=client.recvfrom(BUFFER_SIZE)
   print (message +'='+response.decode('utf-8'))

client.close()