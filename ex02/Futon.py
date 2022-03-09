m,v,n=input().split()
m=float(m)
v=float(v)
n=float(n)
weight=v * m
carrying = n * 1000
capacity = carrying/weight
print(int(capacity))