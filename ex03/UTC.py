utc_a,utc_b,time_a=input().split()
utc_a=float(utc_a)
utc_b=float(utc_b)
time_a=float(time_a)

time_b=time_a - utc_a + utc_b
time_b=time_b % 24
print(int(time_b))

