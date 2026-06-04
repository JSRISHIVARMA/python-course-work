#Tuple
#1)It is a container to store different datatyped elements
#2)it is a immutable
#3)It is a heterogineous
#4)representation of tuple is '()'

#Operations of tuple
'''t = (1,2,3,4,5,6)
k = (1,2,3,4,5,6,5)
print("tuple of elements in t : ",t)
print("tuple of elements in k  : ",k)
print("concatination of both t and k : ",t+k)
print("thriple Repetation if t : ",t*3)
print("Getting 3rd Indexed Value is : ",t[3])
print("getting till 3rd position : ",t[:4])
print("Reversing the tuple : ",t[::-1])
print("checking of 30 element in t : ",30 in t)'''

#methods of tuple
'''t = (1,2,3,4,5,6)
k = (1,2,3,4,5,6,5)
print("size of elements in t : ",len(t))
print("sum of elements in t : ",sum(t))
print("min of elements in t : ",min(t))
print("max of elements in t : ",max(t))
print("sorting  of elements in t : ",sorted(t))
print("count of elements in t : ",t.count(1))
print("index of elements in t : ",t.index(4))
h = (1,2,3,4,[1,2,3221],221,233)
print("tuple of elements in h : ",h)
a = h[4].append(10)
print("updating list inside the tuple : ",h)'''

#Set
#1)It is a container to store immutable datatyped elements
#2)it is a mutable
#3)It is a heterogineous
#4)It is a unodered datatype


#Operations of tuple
'''s = {1,2,3,44,2,2}
print("set of elements in s : ",s)
a = s.add(211.122)
print("adding float value elements in h set : ",s)
print("finding i value elements in s : ",1 in s)
h = {12,3,312,33,4,344,3444,3}
print("union of  values s and h sets : ",s | h)
print("union of  values s and h sets : ",s.union(h))
print("intersection of  values s and h sets : ",s.intersection(h))
print("Difference of  values s and h sets : ",s - h)
print("Simettric of  values s and h sets : ",s ^ h)
print("subset of  values s and h sets : ",s <= h)
print("Superset of  values s and h sets : ",s >= h)
print("superset of  values s and {1,2} sets : ",s >= {1,2})'''

#Methods of tuple
s = {1,2,3,44,2,2}
print("set of elements in s : ",s)
a = s.add(200)
print("adding 200 element s set : ",s)
u = s.update({201,445,65})
print("updating  201,445,65 elements  in s set : ",s)
p = s.pop()
print("popping element s set : ",s)
r = s.remove(2)
print("removing 2 element in s set : ",s)
#d = s.discord(44)
#print("Discording 2 element s set : ",s)
h = {12,3,312,33,4,344,3444,3}
print("set of elements in h : ",h)
c = h.copy()
d = c.add(20000)
print("updated copied set of elements in c : ",c)
print("original set of elements in h : ",h)
print("size of elements in s : ",len(s))
print("sum of elements in s : ",sum(s))
print("min of elements in s : ",min(s))
print("max of elements in s : ",max(s))
print("sorting  of elements in s : ",sorted(s))