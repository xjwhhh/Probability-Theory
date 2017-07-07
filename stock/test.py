
ff=open("C:\\Users\\xjwhh\\Desktop\\newstock.txt")
f=open("C:\\Users\\xjwhh\\Desktop\\newstock1.txt",'a')
list_of_all_the_lines = ff.readlines( )
for i in range(0,len(list_of_all_the_lines)):
    j=j=list_of_all_the_lines[i]
    t=j[-8:-2]
    f.write(t)
    f.write("\n")