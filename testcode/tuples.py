def onehop(l):
    nw = []
    l.sort()

    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] == l[j]:
                if l[i][1] == l[j][0]:
                    a=l[i][0]
                    b=l[i][1]
                    if a!=b:
                        t=(a,b)
                        t=tuple(t)
                        if t not in nw:
                            nw=nw+[tuple(t)]

    nw.sort()
    return nw

l= []
li = input("Enter the list of tuples: ")

while li != "":
    l.append(tuple(li.split()))
    li = input()
print(onehop(l))