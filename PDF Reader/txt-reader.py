f = open('Conventions.txt','r')
message = f.read()
print(message)
f.close()

print (message.splitlines())
 
