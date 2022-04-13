a= int(input())
b= list(map(int, input().split(' ')))

c=0
for i in b:
    d= b.count(i)
    if d==1:
        e=i
    elif d==a:
        pass
    else:
        c =1
        
if c ==1:
    print('something wrong Data. Please Try again')
else:
    print(e)
