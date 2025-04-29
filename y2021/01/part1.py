my_file = open("input","r")
content_list = my_file.read()
print(content_list)
content_list=content_list.split("\n")
my_file.close()
print(content_list)

incr = 0
for i in range(1, len(content_list)-1):
    if(int(content_list[i]) > int(content_list[i-1])):
        incr=incr+1
print(incr)
