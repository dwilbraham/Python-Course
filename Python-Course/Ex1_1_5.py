[x * x for x in xrange(10, 50) if x % 2 == 0]

list1 = list(xrange(3))
list2 = list(xrange(4))
list3 = list(xrange(5))
[(x,y,z) for x in list1 for y in list2 for z in list3]