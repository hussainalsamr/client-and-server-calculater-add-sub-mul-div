import socket
def cal(message):
    numbers=[]
    parameters=[]
    math_op=['add','sub','mul','div']
    parameters=message.split()
    if len(parameters)>3:return 'Invalid request:you most inter only three parameters'
    if not ((parameters[1].isdigit()) and (parameters[2].isdigit())): return 'Invalid request:second and third parameters must be digits'
    if not (parameters[0] in math_op): return  "Invalid request: first parameters must be one of (add,sub,mul,div)"
    if (parameters[0]=='add'):return (int(parameters[1]) + int (parameters[2]))
    if (parameters[0] == 'sub'): return (int(parameters[1]) - int(parameters[2]))
    if (parameters[0] == 'mul'): return (int(parameters[1]) * int(parameters[2]))
    if (parameters[0] == 'div'): return (int(parameters[1]) / int(parameters[2]))
serverport=12800
BUFFER_SIZE=1024
serversocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind(('',serverport))
print('The server is ready to receive port 12800')
while 1:
    message,clientaddress=serversocket.recvfrom(BUFFER_SIZE)
    message=message.decode('utf-8')
    response=str(cal(message))
    serversocket.sendto(response.encode('utf-8'),clientaddress)
    print(str(message)+'='+str(response))
    serversocket.close()
