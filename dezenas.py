#LEITOR UNIDADES DEZEWNAS CENTENAS E MILHARES
num = int(input('Digite um número: '))  # 78615
milhar = num //1000
resto = num %1000
centena = resto //100
resto = resto %100
dezena = resto //10
resto = resto%10
unidade = resto //1

print(f'O digito das Dezenas é: {dezena}!')