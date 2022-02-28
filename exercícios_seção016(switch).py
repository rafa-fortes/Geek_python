def select_mes(opcao):
    opcoes = {
        1: 'Mês Janeiro',
        2: 'Mês Fevereiro',
        3: 'Mês Março',
        4: 'Mês Abril',
        5: 'Mês Maio',
        6: 'Mês Junho',
        7: 'Mês Julho',
        8: 'Mês Agosto',
        9: 'Mês Setembro',
        10: 'Mês outubro',
        11: 'Mês Novembro',
        12: 'Mês Dezembro',
    }
    return opcoes.get(opcao, 'Número inválido! ')

if __name__ == '__main__':
    opcao = int(input('Digite um número inteiro entre 1 a 12: ')) 
    print(select_mes(opcao))   