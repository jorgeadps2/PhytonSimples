name = input("Digite o nome do Filme:\n") 
yearLaunch = int(input("Digite o ano de lançamento:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

print("Dados do Filme")
print("=====================")

# #Alternativa 1
print("Nome do Filme:", name)
print("Ano de lançamento", yearLaunch)
print("Nota do Filme", noteMovie)

# #Alternativa 2
print("Nome do Filme:", name, "\nAno de Lançamento:", yearLaunch, "\nNota do Filme:", noteMovie)

#Alternativa 3 
print(f"nome do Jogo: {name}\n"
      f"Ano do Filme: {yearLaunch}\n"
      f"Nota do Filme: {noteMovie}\n"
)