from random import randint
print("Olá 1info2!")
dado1 = randint(1, 6)
dado2 = randint(1, 6)
dado3 = randint(1, 6)
dado4 = randint(1, 6)
print("Dado 1:", dado1)
print("Dado 2:", dado2)
print("Dado 3:", dado3)
print("Dado 4:", dado4)
if dado1+dado2>dado3+dado4:
	print("Jogador 1 venceu")
if dado3+dado4>dado1+dado2:
	print("Jogador 2 venceu")
if dado1+dado2==dado3+dado4:
	print("Empate")