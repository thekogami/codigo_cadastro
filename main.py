#ponto de entrada principal. Solicitar resposta ao usuario e valida essas informações com base nas funções definidas em validacao.py

from validacao import (
    validar_cpf, validar_cnpj, validar_data, validar_telefone, validar_campo_obrigatorio, obter_input_valido
)

def main():
    nome = obter_input_valido("Digite o nome ou razão social (campo obrigatório): ", validar_campo_obrigatorio)
    cpf_cnpj = obter_input_valido("Digite o CPF ou CNPJ (campo obrigatório): ", lambda x: validar_cpf(x) or validar_cnpj(x))
    data_nascimento = obter_input_valido("Digite a data de nascimento (ddmmaaaa, campo obrigatório): ", validar_data)
    endereco = input("Digite o endereço: ")
    bairro = input("Digite o bairro: ")
    cep = input("Digite o CEP: ")
    data_cadastro = obter_input_valido("Digite a data de cadastro (ddmmaaaa): ", validar_data) if input("Deseja cadastrar uma data de cadastro? (s/n): ").lower() == 's' else ""
    municipio = input("Digite o município: ")
    telefone = obter_input_valido("Digite o telefone (10 ou 11 dígitos): ", validar_telefone) if input("Deseja cadastrar um telefone? (s/n): ").lower() == 's' else ""
    celular = obter_input_valido("Digite o celular (campo obrigatório): ", validar_telefone)

    print("Todos os campos foram preenchidos corretamente!")

if __name__ == "__main__":
    main()
