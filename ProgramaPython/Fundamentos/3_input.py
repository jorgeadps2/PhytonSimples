#utilizando o imput
name = input("Digite o nome do Filme:\n") 
yearLaunch = int(input("Digite o ano de lançamento:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

print(type(name))
print(type(yearLaunch))
print(type(noteMovie))


#Exercicio:
#Escreva um programa que leia o nome de uma pessoa usando input() 
# e imprima a mensagem:"Olá, <nome>!" (com ponto de exclamação no final e quebra de linha no final).
nome = input("Digite seu nome")
print(f"Olá, {nome}!")