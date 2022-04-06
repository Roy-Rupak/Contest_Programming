a = []
i = int(input())
while (i):
    n = input().split(' ')
    a.append((n))
    i -= 1
print(a)
dict = {}
for x, y in a:
    if x not in dict:
        dict[x] = int(y)
    else:
        dict[x] += int(y)
#dict.sort(key=lambda x:x[1],reverse=True)
s=sorted(dict.items(), key=lambda item: item[1],reverse=True)
print(s)
print((sorted((dict),reverse=True)))
for key in sorted((dict),reverse=True):
    print(key)
