s= int (input())
hours=s//3600%24
minutes=s//60%60
seconds=s%60
print ( hours//10,hours%10,':',minutes//10,minutes%10,':',seconds//10,seconds%10,sep='',end="\n")

