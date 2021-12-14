def print_basic(mensagem):
    print(mensagem)


def print_soma(valor: int) -> None:
    valor_um = 3

    print(f'A soma foi: {valor + valor_um}')


def print_subtracao(valor_um: int, valor_dois: int) -> str:
    """
    Aplica a soma do primeiro parâmetro com o segundo, mostrando o resultado no console.

    A função se utiliza de uma concatenação simples, entre o valor resultante do cálculo entre os
    parâmetros, e a mensagem do método print.
    O cálculo é: (valor_um subtrai valor_dois)

    :param: valor_um:int
    :param: valor_dois:int
    :return: none
    """

    print(f'A subtração foi: {valor_um-valor_dois}')
    return 'Success'


if __name__ == '__main__':
    print(f'Caso 1')
    print_soma(7)
    print(f'Caso 2')
    print_subtracao(8, 3)
    print(f'Caso 3')
    print_subtracao(5, 3)
    print(f'Caso 4')
    print_basic('Treinamento de Python!!')
