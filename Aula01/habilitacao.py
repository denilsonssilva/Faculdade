idade = int(input('Digite a sua idade: '))
tempo_cnh = int(input('Quantos anos de habilitação? '))
aliquota = 0.05

if idade < 25:
    aliquota += 0.03
if tempo_cnh <= 2:
    aliquota += 0.02

print(f'Sua aliquota é: {aliquota:.1%}')
