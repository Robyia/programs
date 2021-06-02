my_file=open("test.txt","r")
list1=[]
for line in my_file:
    stripped_line=line.strip()
    line_list=stripped_line.split()
    list1.append(line_list)
my_file.close()
print(list1)




