a=int(input())
b=int(input())
c=str(input())
stack=""
i=0
while i<len(c):
    if c[i]=='S':
        i+=a
        if i>len(c):
            i=len(c)%i
    elif c[i]=='F':
        i-=b
        if i<0:
            i=len(c)+i
    elif c[i]=='!':
        break
    else:

        stack+=c[i]
        i+=1
print(stack)



