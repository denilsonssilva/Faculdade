valor = float(input('Preço do produto: '))
qtd = int(input('Quantidade: '))
total = valor * qtd

if total > 200 or qtd >= 25:
    desconto = total * 0.08
    total -= desconto
    print(f'O valor final com desconto é {total:.2f}')
else:
    print(f'O valor final é: {total:.2f}')
