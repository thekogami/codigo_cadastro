#pip install pytest

import pytest
from validacao import (
    validar_cpf, validar_cnpj, validar_data, validar_telefone, validar_campo_obrigatorio
)

def test_validar_cpf():
    assert validar_cpf("623.540.253-86") == True  # Válido
    assert validar_cpf("123.456.789-09") == True  # Válido
    assert validar_cpf("111.444.777-35") == True  # Válido
    assert validar_cpf("123.456.789-00") == False  # Inválido
    assert validar_cpf("222.222.222-22") == False  # Inválido (sequência repetida)
    assert validar_cpf("987.654.321-00") == True  # valido
    assert validar_cpf("012.345.678-90") == True  # valido
    assert validar_cpf("745.763.890-00") == False  # Inválido
    assert validar_cpf("000.000.000-00") == False  # Inválido (sequência repetida)
    assert validar_cpf("583.951.507-82") == False  # invalido
    assert validar_cpf("135.792.468-50") == False  # Inválido

def test_validar_cnpj():
    assert validar_cnpj("12.345.678/0001-95") == True    # Válido
    assert validar_cnpj("12.345.678/0001-9") == False    # Inválido (digito incompleto)
    assert validar_cnpj("11.222.333/0001-81") == True    # Válido
    assert validar_cnpj("12.345.678/0001-96") == True   # Inválido (dígito verificador errado)
    assert validar_cnpj("45.987.654/0001-32") == True    # Válido

def test_validar_data():
    assert validar_data("14021998") == True   # Válido (14/02/1998)
    assert validar_data("31021998") == False  # Inválido (data inexistente)
    assert validar_data("29022000") == True   # Válido (ano bissexto)
    assert validar_data("29021999") == False  # Inválido (não é ano bissexto)
    assert validar_data("01012000") == True   # Válido (01/01/2000)
    assert validar_data("31122099") == True   # Válido (31/12/2099)
    assert validar_data("30022020") == False  # Inválido (data inexistente)
    assert validar_data("01132020") == False  # Inválido (mês inexistente)
    assert validar_data("00000000") == False  # Inválido (sequência repetida)

def test_validar_telefone():
    assert validar_telefone("11987654321") == True   # Válido (11 dígitos)
    assert validar_telefone("987654321") == False    # Inválido (9 dígitos)
    assert validar_telefone("2198765432") == True    # Válido (10 dígitos)
    assert validar_telefone("21987654321") == True   # Válido (11 dígitos)
    assert validar_telefone("31999999999") == True   # Válido (11 dígitos)

def test_validar_campo_obrigatorio():
    assert validar_campo_obrigatorio("Nome") == True
    assert validar_campo_obrigatorio("") == False
