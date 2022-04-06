class Trie(object):
   def __init__(self):
      self.child = {}
   def insert(self, word):
      current = self.child
      for l in word:
         if l not in current:
            current[l] = {}
         current = current[l]
      current['#']=1
   def search(self, word):
      current = self.child
      for l in word:
         if l not in current:
            return False
         current = current[l]
      return '#' in current
   def startsWith(self, prefix):
      current = self.child
      for l in prefix:
         if l not in current:
            return False
         current = current[l]
      return True
n=input().split(',')
keys=[]
for x in range(0,len(n)-2):
    s=n[x].split('-')
    #print(s)
    keys.append(s[0]+s[1])
    #T.insert(s[0]+s[1])

#keys = ["the","a","there","anaswe","any","by","their"]
output = ["Not present in trie",
			"Present in trie"]

# Trie object
t = Trie()

# Construct trie
for key in keys:
	t.insert(key)

print(t.startsWith(n[-1]))