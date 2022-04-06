import math
a=[[6,10,4],[7,4,10],[10,6,4]]
F,B,P=0,1,2
n=int(input())
dict={}
last=(0,0)
while(n):
    s=input().split(' ')


    if s[0] not in dict:
        dict[s[0]] = math.sqrt(((int(last[0]) - int(s[1])) ** 2) + ((int(last[1]) - int(s[2])) ** 2))
    else:
        dict[s[0]]+= math.sqrt(((int(last[0]) - int(s[1])) ** 2) + ((int(last[1]) - int(s[2])) ** 2))
    last = (int(s[1]), int(s[2]))
    n-=1
S,T,P=0,0,0
for key,value in dict.items():
    if key=='F':
        S+=a[0][0]*value
        T+=a[1][0]*value
        P+=a[2][0]*value
    elif key=='B':
        S += a[0][1] * value
        T += a[1][1] * value
        P += a[2][1] * value
    else:
        S += a[0][2] * value
        T += a[1][2] * value
        P += a[2][2] * value

print(S,T,P)
if S==T or S==P or P==T:
    print("TIE")
else:
    if (S >= T) and (S >= P):
       largest = 'S'
    elif (T >= S) and (T >= P):
       largest = 'T'
    else:
       largest = 'P'
    print(largest)