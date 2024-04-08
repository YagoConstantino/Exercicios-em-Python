# ___________Começo cadastrar produto/////nome//valor//fabricante//código
# consultar produtos////todos os produtos//por código//fabricante// retornar

listaprodutos = []


# ---cadastrar produto---
def cadastrar_produto(code):
    try:
        print('Bem vindo ao Cadastro de Produtos')
        print(f'o Código do produto a ser cadastrado é:{code}')
        nome = input('Digite  o nome do produto:\n')
        valor = int(input('Digite  o valor do produto:\n'))
        fabricante = input('Digite o fabricante do produto\n')
        dicionario_produtos = {'Nome': nome,
                               'Fabricante': fabricante,
                               'Valor': valor,
                               'Código': code}
        return listaprodutos.append(dicionario_produtos.copy())
    except:
        ValueError('Coloque o dado correto... tente novamente')


# ----- Fim do Cadastro---


def consulta_produto():  # ---Começao de consulta por produto---
    print('Bem vindo a Consulta de Produtos')
    while True:
        try:
            print('1-Consultar todos os produtos')
            print('2-Consultar por Código')
            print('3-Consultar por Fabricante')
            print('4-Retornar')
            opcao2 = int(input('Escolha uma Tarefa a ser executada\n'))  # Consulta todos os produtos cadastrados
            match opcao2:
                case 1:
                    print('Bem vindo a Consultar todos os produtos')
                    for produto in listaprodutos:  # seleciona cada dicionário de minha lista
                        for key, value in produto.items():  # seleciona cada conjunto chave/valor do dicionário(nome/leite)
                            print('{}:{}\n'.format(key, value))  # imprime cada conjunto

                case 2:
                    print('Bem vindo a Consultar por Código')
                    entrada = int(input('Qual o Código do produto?:\n'))
                    for produto in listaprodutos:
                        if produto['Código'] == entrada:
                            for key, value in produto.items():
                                print('{}:{}\n'.format(key, value))
                case 3:
                    print('Bem vindo a Consultar por Fabricante')
                    entrada = input('Qual o nome do Fabricante?:')
                    for produto in listaprodutos:
                        if produto['Fabricante'] == entrada:
                            for key, value in produto.items():
                                print('{}:{}\n'.format(key, value))

                case 4:
                    print('Retornando ao Menu Principal')
                    return
                case _:
                    print('Opção inválida...Tente novamente')
                    continue
        except ValueError:
            print('É necessário usar um código que seja um número inteiro e positivo entre 1 e 4 ')


# ____Fim da consulta____

# ------Começo da Remoção---
def remover_produto():
    print('Bem vindo a Remoção de produtos')
    entrada = int(input('Qual o Código do produto a ser removido?:'))
    for produto in listaprodutos:
        if produto['Código'] == entrada:
            listaprodutos.remove(produto)
            # ------------Fim da Remoção-----------


# Main :
# Bem vindo ao controle de produtos da mercearia de Yago Constantino RU:4206622
print('Bem vindo Ao controle de produtos da mercearia de Yago Constantino Ru:4206622')
Codigo = 0
while True:
    try:
        print('1-Cadastrar Produto')
        print('2-Consultar produto(s)')
        print('3-Remover produto')
        print('4-Sair')
        opcao = int(input('Escolha uma Tarefa a ser executada\n'))
        match opcao :
            case 1 :
                Codigo += 1
                cadastrar_produto(Codigo)
            case 2 :
                consulta_produto()
            case 3:
                remover_produto()
            case 4:
                print('\nCadastro de produtos Encerrado....')
                break
            case _:
                print('Opção inválida...Tente novamente\n')
                continue
    except ValueError:
        print('É necessário usar um código que seja um número inteiro e positivo entre 1 e 4\n ')

# ---------Fim Main-------------1

