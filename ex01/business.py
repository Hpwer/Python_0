n,s,o=input().split()
n=float(n)
s=float(s)
o=float(o)
price_of_buy=n-(n*s/100)
profit=(price_of_buy * o/100)
print( int (profit))



