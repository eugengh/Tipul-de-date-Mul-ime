import itertools 
s = {"A","B","C","D"}
data2 = itertools.combinations(s, 2)
data1 = itertools.combinations(s, 1)
data3 = itertools.combinations(s, 3)
data4 = itertools.combinations(s,4)
subsets = set(data1)
subsets1 = set(data2)
subsets2 = set(data3)
subsets3 = set(data4)
a = subsets.union(subsets1)
b = subsets2.union(subsets3)
c = list(a.union(b))
y = sorted(c)
print(y)

