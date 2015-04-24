# a03p02a.py
l1 = [a for a in range(1, 11)]
print("list l1 =", l1)

# a03p02b.py
l2 = [a for a in range(10, 101, 10)]
print("list l2 =", l2)

# a03p02c.py
l3 = ['python', 'django', 'flask', 'string', 'function', 'classes']
print("list l3 =", l3)

# a03p02d.py
l4 = {"l1": l1, "l2": l2, "l3": l3}
print("list l4 =", l4)

# a03p02e.py
main_list = []
main_list.extend(l1)
main_list.extend(l2)
main_list.extend(l3)

# a03p02f.py
l5 = l1 * 2

# a03p02g.py
main_list.append(l5)

# a03p02h.py
print ("occurance of 1 in main list is:-", main_list.count(1))
