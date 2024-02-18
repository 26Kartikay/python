num=int(input("please enter the number whose table you want to print"))
end=int(input("please enter the number till which you want table to print "))
for i in range(0,end+1,1):
    print(num,"x",i,"=",num*i)