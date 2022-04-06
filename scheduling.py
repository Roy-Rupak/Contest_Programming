n=int(input())
dict={}
while(n):
    s=input().split()
    t=s[0]+s[1]+s[2]
    if t not in dict:
        dict[t]=s[3]
    else:
        dict[t]=dict[t]+"/"+s[3]
    n-=1
print(*dict.values())