my_file = open("input","r")
content_list = my_file.read()
print(content_list)
content_list=content_list.split("\n")
my_file.close()
print(content_list)

incr = 0
for i in range(0,len(content_list)-4):
    A1=int(content_list[i])
    A2=int(content_list[i+1])
    A3=int(content_list[i+2])
    B1=int(content_list[i+1])
    B2=int(content_list[i+2])
    B3=int(content_list[i+3])
    print(B3)
    ASUM=A1+A2+A3
    BSUM=B1+B2+B3
    if(BSUM > ASUM):
        incr=incr+1
print(incr)
