#--encoding:utf-8--#
#simulador de dado
import random
import sys
import os
import time
linha = '-' * 50
def jogar():
	print("\t Você gostaria de jogar dado?")
	if sys.version_info.major == 3:
		resposta = input("\t [N] = Não   [S] = Sim \n")
		resposta = resposta.upper()
	elif sys.version_info.major == 2:
		resposta = raw_input("\t N = Não   S = Sim \n")
		resposta = resposta.upper()
	while resposta == "S":
		print(linha)
		print("\t \t",random.randrange(1,6,))
		time.sleep(1)
		os.system("cls")
		time.sleep(1)
		jogar()
	while resposta == "SIM":
		print(linha)
		print("\t \t",random.randrange(1,6,))
		time.sleep(1)
		os.system("cls")
		time.sleep(1)
		jogar()

	if resposta == "N":
		print(linha)
		print("\t O programa será encerrado")
		time.sleep(1)
		os.system("cls")
		time.sleep(1)
		quit()
	if resposta == "NAO":
		print(linha)
		print("\t O programa será encerrado")
		time.sleep(1)
		os.system("cls")
		time.sleep(1)
		quit()
	if resposta == "NÃO":
		print(linha)
		print("\t O programa será encerrado")
		time.sleep(1)
		os.system("cls")
		time.sleep(1)
		quit()

	while resposta != "S""N":
		print(linha)
		print("\t Opção inválida!")
		time.sleep(1)
		os.system("cls")
		time.sleep(1)
		jogar()
jogar()