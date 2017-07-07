ff=open("C:\\Users\\xjwhh\\Desktop\\newstock1.txt")
list_of_all_the_lines = ff.readlines( )
for i in range(0,len(list_of_all_the_lines)):
    j=list_of_all_the_lines[i]
    t=j[0:3]
    if (t == "600"):
        section = "沪市A股1"
    elif (t == "601"):
        section = "沪市A股2"
    elif (t == "603"):
        section = "沪市A股3"
    elif (t == "900"):
        section = "沪市B股"
    elif (t == "000"):
        section = "深市A股"
    elif (t == "200"):
        section = "深市B股"
    elif (t == "300"):
        section = "创业板"
    elif (t == "002"):
        section = "中小板"
    else:
        section = "其他"
    f=open("C:\\Users\\xjwhh\\Desktop\\"+section+".txt",'a')
    f.write(j)
