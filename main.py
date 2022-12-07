def Menu():
  print("\n--------------------------------------------------------")
  print("\n1-Somar")
  print("\n2-Subtrair")
  print("\n3-Multiplicar")
  print("\n4-Dividir")
  print("\n5-Fechar")
  print("\n--------------------------------------------------------")
  escolha=int(input("\nQual das opções acima deseja escolher: "))
  return escolha

def Calculadora():
  try:
    escolha=Menu()
    x=0
    y=0
    sum=0
    fechar=0
    continuar="s"
    if escolha==1:
      while continuar=="s":
        x=int(input("\nDigite o primeiro valor que deseja somar: "))
        y=int(input("\n\nDigite o segundo valor que deseja que seja somado: "))
        sum+=x+y
        print("O resultado da soma foi: {}". format(sum))
        continuar=str(input("\nDeseja Continuar somando com os valores existentes (s/n): "))
      
    elif escolha==2:
      x=int(input("\nDigite o primeiro valor que deseja subtrair: "))
      y=int(input("\n\nDigite o segundo valor que deseja que seja subtraido do outro: "))
      sum=x-y
      print("O resultado da subtracao foi: {}". format(sum))
      
    elif escolha==3:
      x=int(input("\nDigite o primeiro valor que deseja multiplicar: "))
      y=int(input("\n\nDigite o segundo valor que deseja que seja multiplicado pelo outro: "))
      sum=x*y
      print("O resultado da multiplicacao foi: {}". format(sum))

    elif escolha==4:
      x=int(input("\nDigite o primeiro valor que deseja dividir: "))
      y=int(input("\n\nDigite o segundo valor que deseja que deseja usar para dividir o outro: "))
      sum=x/y
      print("O resultado da divisao foi: {}". format(sum))
    
    elif escolha==5:
      fechar=1
    return fechar
  except:
    print("\n Ocorreu um emprevisto, tente utilizacao mais tarde.")
while True:
  interruptor=Calculadora()
  if interruptor==1:
    break
