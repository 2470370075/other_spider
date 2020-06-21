l = [2,9,4,1,5]
l1 = []
for i in range(len(l)):

    l1.append(min(l))
    l.remove(min(l))


print(l1)

