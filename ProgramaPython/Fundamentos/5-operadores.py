num1 = int(input("Digite o primeiro número"))
num2 = int(input("Digite o segundo número"))

# #Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

# exemplo 1
print(sum)

# exemplo 2
print(f"Potência do número {num1} por {num2} é: {exp}")
print(f"Valor da Divisão de {num1} por {num2} é: {div}")

# comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
samller_equal = num1 <= num2

print(f"Os números {num1} e {num2} são iguais? {equal}")
print(f"O número {num1} é maior ou igual a {num2}?  {bigger_equal}")

# atribuição
num1 += 1 #num1 = num1 + 1
num1 -= 1 #num1 = num1 - 1
num1 *= 1 #num1 = num1 * 1
num1 /= 1 #num1 = num1 / 1