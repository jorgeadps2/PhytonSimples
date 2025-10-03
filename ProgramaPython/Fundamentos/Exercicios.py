# # 1- Escreva uma programa que lê dois nomes e retorne uma string 
# # formatada no formato "ÚltimoNome, PrimeiroNome".

# # 2- Inverta a ordem das palavras em uma string fornecida.

# # 3-Verifique se uma string fornecida é um palíndromo _
# # (pode ser lida da mesma forma de trás para frente).

# # #Ex1.
primeiroNome = input ("Digite o primeiro nome: \n")
segundoNome = input ("Digite o Segundo nome: \n")
nomeFormatado = f"{segundoNome} {primeiroNome}"
print(nomeFormatado)

# #Ex2.
texto = "aprendendo linguagem Pyton"
palavras = texto.split()
textoInvertido = " ".join(palavras [::-1])
print(textoInvertido)

#Ex.3
texto1 = "arara"
texto2 = "Python"

texto1_format = texto1.lower().replace(" ","")  #Esse comando remove espaço e deixa as palvaras em minusculo
texto2_format = texto2.lower().replace(" ","") 

palindromo1 = texto1_format == texto1 [:: -1]  # este comando verifica se o texto original é igual seu reverso
palindromo2 = texto2_format == texto2 [:: -1]

print(palindromo1)
print(palindromo2)