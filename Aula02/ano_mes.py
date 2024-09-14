def bissexto(ano):
    return ano%4==0 and ano%100!=0 or ano%400==0

def qtd_dias(mes, ano):
    if mes == 2:
        if bissexto(ano):
            return 29
        else:
            return 28
    if mes==4 or mes==6 or mes==9 or mes==11:
        return 30
    return 31

def nome_mes (mes):
    meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho',
             'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    print(meses[mes-1])

mes = int(input('Mês? '))
ano = int(input('Ano? '))
print(f'{nome_mes(mes)} de {ano} terá {qtd_dias(mes, ano)} dias')