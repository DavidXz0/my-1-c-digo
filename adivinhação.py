import random
print("===JOGO DA ADIVINHAÇÃO===")
numero_secreto = random.randit(1, 10)
tentativas= 0
while True:
  chute = int(input("Digite um número entre 1 a 10:  "))
     tentativas +=1
if chute == numero_secreto:
  print(f"Parabéns! Você acertou com {tentativas} tentativas(s). ")
break
elif chute < numero_secreto :
print("Tente um número maior!")
else :
print("Tente um número maior!") 
