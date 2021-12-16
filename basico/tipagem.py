from manutencao import print_multiplicacao


def while_simples(indice: int) -> int:
    while indice < 5:
        print('Índice em:', indice)
        indice = indice + 1
    else:
        print("Limite alcançado!")
        return 0


def while_break(indice: int) -> int:
    while indice < 10:
        print('Índice em:', indice)
        indice += 1
        if indice == 8:
            print("Índice: ", indice)
            break
    else:
        # Observe que essa etapa não é executada!
        # Caso a repetição seja parada, a exceção automaticamente não é possível.
        print("fim while")
        # Mesmo não sendo usado, o return irá definir a propriedade da função.
        return 0


def for_data() -> None:
    indice = 0
    pessoas = [({'nome': 'João', 'cidade': 'Belo Horizonte'}),
               ({'nome': 'Maria', 'cidade': 'São Paulo'}),
               ({'nome': 'Pedro', 'cidade': 'Curitiba'}),
               ({'nome': 'Julia', 'cidade': 'Brasília'}),
               ({'nome': 'Bruna', 'cidade': 'Pernambuco '}),
               ({'nome': 'Guilherme', 'cidade': 'Santa Catarina'})]

    for pessoa in pessoas:
        print('No índice:', indice, 'temos', pessoa['nome'], "mora em", pessoa['cidade'])
        indice += 1
        if pessoa['nome'] == 'Julia':
            print("Sorteado! Ganhador: ", pessoa['nome'], "mora em", pessoa['cidade'])
            return


def soma(v_um: int, v_dois: int) -> str:

    return "Sua soma equivale a " + print_multiplicacao(v_um, v_dois).__str__()


# while_simples(0)


# while_break(0)


# for_data()

soma(15, 5)
