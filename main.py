class Fracao:
  numerador = 1 
  denominador = 1 
  

  def __init__(self, numerador, denominador):
    self.numerador = numerador
    self.denominador = denominador
  def add(self, fracao):
    num = (self.numerador * fracao.denominador) \
        + (fracao.numerador * self.denominador)
    den = self.denominador * fracao.denominador
    return Fracao(num,den)
  def solve(self): 
    return self.numerador / self.denominador
  def __str__(self):
    return f"{self.numerador}/{self.denominador}"
  def sub(self,fracao):
    num = (self.numerador * fracao.denominador) \
        - (fracao.numerador * self.denominador)
    den = self.denominador * fracao.denominador
    return Fracao(num,den)
  def mul(self,fracao):
    num = (self.numerador * fracao.denominador) \
        * (fracao.numerador * self.denominador)
    den = self.denominador * fracao.denominador
    return Fracao(num,den) 
  def simpl(self):
    num = self.numerador
    den = self.denominador
    while num%2==0 and den%2==0 or num%3==0 and den%3==0 or num%5==0 and den%5==0 or num%7==0 and den%7==0:
      if num%2==0 and den%2==0:
          num/=2                                           ##TESTAR COM NUM NO LUGAR DOS SELFS.
          den/=2
      elif num%3==0 and den%3==0:
          num/=3
          den/=3   
      elif num%5==0 and den%5==0:
          num/=5
          den/=5   
      elif num%7==0 and den%7==0:
          num/=7
          den/=7
    return Fracao(num,den)


def menu():
  print("CALCULADORA!!")
  print("1 - SOMA")
  print("2 - SUBTRAÇÃO")
  print("3 - MULTIPLICAÇÃO")
  print("4 - DIVISÃO")
  print("5 - SIMPLIFICAÇÃO")
  print("6 - RESOLVER")
       
  
x = int(input("digite x: "))
y = int(input("digite y: "))  
code = 0
menu() 
fracao1 = Fracao(x,y)
code = int(input("digite a opção: "))
if code == 1:
   z = int(input("digite x2: "))
   w = int(input("digite y2: "))  
   fracao2 = Fracao(z,w)
   print(Fracao.add(fracao1,fracao2))
elif  code == 2:
   z = int(input("digite x2: "))
   w = int(input("digite y2: "))  
   fracao2 = Fracao(z,w)
   print(Fracao.sub(fracao1,fracao2))
elif  code == 3:
   z = int(input("digite x2: "))
   w = int(input("digite y2: "))  
   fracao2 = Fracao(z,w)
   print(Fracao.mul(fracao1,fracao2))  
elif  code == 4:
   z = int(input("digite x2: "))
   w = int(input("digite y2: "))  
   fracao2 = Fracao(z,w)    
   print(Fracao.sub(fracao1,fracao2))  
elif code == 5:
   fracao1 = Fracao.simpl(fracao1)  
   print(f"fração simplificada: {fracao1}")
elif code == 6:
   print(Fracao.solve(fracao1))  