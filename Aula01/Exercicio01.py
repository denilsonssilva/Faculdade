valor = float(input('Valor do item: '))
qtd = int(input('Qual a quantidade: '))
total = valor * qtd
desconto = total * 0.10
total_final = total - desconto

print(f'O total comprado com desconto é: R${total_final:.2f}')
