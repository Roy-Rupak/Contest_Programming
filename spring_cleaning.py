from collections import defaultdict
my_dict = defaultdict(lambda: defaultdict(int))
#n=int(input())
while(True):
    s=input()
    if s=="":
        break
    s=s.split('-')
    my_dict[s[0]][s[1]]+=1
#print(my_dict.items())
s,r='',''
for key,value in my_dict.items():
    #print(key,*value.keys(),*value.values())
    s=''
    s+=key+':'
    for k,v in value.items():
        s+=str(k)+' '+str(v)+','
    r+='\n'+s[:-1]

print(r)