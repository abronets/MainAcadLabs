set1 = set('f127dh1207cc')
set2 = set('a7v657323xjjf')

print(set1)

inter = tuple(set1.intersection(set2))
differ = tuple(set1.difference(set2))

inter = inter[:3]

print(set(differ))

inter = inter[::-1]

list(inter)
list(differ)

