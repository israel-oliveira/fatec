a = float(input("Digite um numero: \n"))
b = float(input("Digite um numero: \n"))
c = float(input("Digite um numero: \n"))

if((a==b) & (a==c) & (b==c)):
  print("Todos são iguais: ", a)
elif((a==b) | (a==c) | (b==c)):
  if((a==b) & (a > c)):
    print("A: ",a)
    print("B: ",b)
  elif((a==b) & (a < c)):
    print("C: ",c)
  elif((a==c) & (a > b)):
    print("A: ",a)
    print("C: ",c)
  elif((a==c) & (a < b)):
    print("B: ",b)
  elif((b==c) & (b > a)):
    print("B: ",b)
    print("C: ",c)
  elif((b==c) & (b < a)):
    print("A: ",a)
else:
  if((a > b) & (a > c)):
    print("A: ",a)
  elif(b > c):
    print("B: ",b)
  else:
    print("C: ",c)
