#validacao contém apenas as funções de validação e a função obter_input_valido. Não deve ser executado diretamente para interagir com o usuário; em vez disso, ele deve ser importado e usado por main.py

import re
from datetime import datetime

def validar_cpf(cpf: str) -> bool:

    # Verifica a formatação do CPF
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False
    return True

def validar_cnpj(cnpj: str) -> bool:
    cnpj_limpo = re.sub(r'\D', '', cnpj)
    return len(cnpj_limpo) == 14 and cnpj_limpo.isdigit()

def validar_data(data_str: str) -> bool:
    if len(data_str) != 8 or not data_str.isdigit():
        return False
    try:
        datetime.strptime(data_str, '%d%m%Y')
        return True
    except ValueError:
        return False

def validar_telefone(telefone: str) -> bool:
    telefone_limpo = re.sub(r'\D', '', telefone)
    return len(telefone_limpo) in [10, 11] and telefone_limpo.isdigit()

def validar_campo_obrigatorio(campo: str) -> bool:
    return bool(campo.strip())

def obter_input_valido(mensagem: str, validacao) -> str:
    while True:
        valor = input(mensagem)
        if validacao(valor):
            return valor
        else:
            print("Entrada inválida. Por favor, tente novamente.")
