def meu_switch(opcao):
    opcoes = {
        1: 'Hoje é domingo!',
        2: 'Hoje é segunda-feira!',
        3: 'Hoje é terça-feira!',
        4: 'Hoje é quarta-feira!',
        5: 'Hoje é quinta-feira!',
        6: 'Hoje é sexta-feira!',
        7: 'Hoje é sábado!',
    }
    return opcoes.get(opcao, 'Opção inválida. ')

if __name__=='__main__':
    opcao = int(input('Digite um número inteiro entre 1 e 7: '))
    print(meu_switch(opcao)) 