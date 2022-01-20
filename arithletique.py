import math
a=int(input("donner un entier="))
b=int(input("donner un entier="))
p=(a+b)*2
s=a*b
print("le premetre est",p)
print("la surfece est",s)
if(p==s):
  print("le rectangle est carre")
else:
 print("le ractangle n'est pas  carre")
 diagonal=math.sqrt(a**2+b**2)
 print("la diagonal est =.%2F" %diagonal)
 r=int(input("saisir r="))
 vol=math.pi*(r*r)*a
 print("la volume est %3f" %vol)
 
