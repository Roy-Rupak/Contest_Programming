n=int(input())
lst=[]
i=0
s=input().split(' ')
while(i<n):
    lst.append(s[i])
    i+=1
j=0
d=int(input())
def insert(a,b):
    if b in lst:
        index=lst.index(b)
        if a not in lst:
            lst.insert(index+1,a)
    else:
        if a not in lst:
            lst.append(a)

def remove(a):
    if a in lst:
        lst.remove(a)
def swap(a,b):
    if a in lst and b in lst:
        index1=lst.index(a)
        index2=lst.index(b)
        lst[index1],lst[index2]=lst[index2],lst[index1]


while(j<d):
    s=input().split(' ')
    if s[0]=='I' or s[0]=='i':
        insert(s[1],s[2])
    elif s[0]=='R' or s[0]=='r':
        remove(s[1])
    elif s[0]=='S' or s[0]=='s':
        swap(s[1],s[2])
    j+=1
t=""
for x in lst:
    t+=x+' '
print(t[:-1])
