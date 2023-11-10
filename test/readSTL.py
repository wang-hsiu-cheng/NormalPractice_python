import struct
def ffb(x): 
    return str(round(struct.unpack('f',x)[0],6))
f=open('test.stl','rb')
print(f.read(84))
temp=''
for j in range(4):
    temp='facet normal: '
    for i in range(3):
        temp=temp+ffb(f.read(4))+' '
    print (temp)

    for n in range(3):
        temp='vertex: ' 
        for i in range(3): 
            temp=temp+ffb(f.read(4))+' ' 
        print (temp) 
    attr=f.read(2)
    print('###################################')
   
f.close()
temp=temp[:-1]
print(temp)