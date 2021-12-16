""" Essa classe é responsável por exemplificar o uso eficiente das notações.
A fim de melhorar a legibilidade e manutenção dos projetos."""

def print_basic(mensagem):
    print(mensagem)


def print_soma(valor: int):
    print(f'A soma foi: {valor + 3}')


def print_subtracao(valor_um: int, valor_dois: int) -> str:
    print(f'A subtração foi: {valor_um-valor_dois}')
    return 'Success'


def print_multiplicacao(valor_um: int, valor_dois: int) -> int:
    """
    Multiplica os fatores, exibindo o resultado no console.

    A função se utiliza de uma concatenação simples, entre o valor resultante do cálculo entre os
    parâmetros, e a mensagem do método print.
    O cálculo é: (valor_um subtrai valor_dois)

    :param valor_um: int
    :param valor_dois: int
    :return: int
    """

    print(f'A subtração foi: {valor_um * valor_dois}')
    return valor_um-valor_dois


def execute():
    print(f'Caso 1')
    print_basic('Treinamento de Python!!')

    print(f'Caso 2')
    print_soma(7)

    print(f'Caso 3')
    print_subtracao(8, 3)

    print(f'Caso 4')
    print_multiplicacao(5, 3)
