s=input().split(' ')
m=int(s[0])
n=int(s[1])
cus=int(s[2])
arr = [[0 for i in range(n)] for j in range(m)]
sum_=0
def calculate(x1,y1,x2,y2,budget,sum_,arr):
    #print(arr)

    for x in range(x1,x2):
        for y in range(y1,y2):
            if arr[x][y] >= budget:
                budget -= budget
                arr[x][y] -= budget
                sum_+= budget
            else:
                sum_ += arr[x][y]
                budget -= arr[x][y]
                arr[x][y] -= arr[x][y]

            #print(sum_)

    return sum_

i=0
k=0
for x in range(m):
    z=input().split()
    k=0
    for y in range(n):
        arr[x][y]=int(z[k])
        k+=1

#print(arr)
o=0
while(i<cus):
    e=input().split()
    x1=int(e[0])
    y1=int(e[2])
    x2=int(e[1])
    y2=int(e[3])
    budget=int(e[4])
    #print("budget",budget)
    o+=calculate(x1-1,y1-1,x2,y2,budget,sum_,arr)
    i+=1

#arr = [[0 for i in range(n)] for j in range(m)]
#print(arr)
print(o)
#for x in range(m):
#    for y in range(n):



