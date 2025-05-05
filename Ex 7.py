# Lista para armazenar os dados dos funcionários
funcionarios = []

# Loop para ler os dados dos funcionários
for i in range(4):
    nome = input("Digite o nome do funcionário {}: ".format(i + 1))
    salario_antigo = float(input("Digite o salário antigo do funcionário {}: ".format(i + 1)))
    idade = int(input("Digite a idade do funcionário {}: ".format(i + 1)))
    sexo = input("Digite o sexo do funcionário {} (M/F): ".format(i + 1))
    percentual_aumento = float(
        input("Digite o percentual de aumento salarial para o funcionário {} (em %): ".format(i + 1)))

    # Calcula o novo salário com o aumento percentual
    novo_salario = salario_antigo * (1 + percentual_aumento / 100)

    # Adiciona os dados do funcionário à lista
    funcionarios.append({
        'nome': nome,
        'salario_antigo': salario_antigo,
        'idade': idade,
        'sexo': sexo.upper(),
        'percentual_aumento': percentual_aumento,
        'novo_salario': novo_salario
    })

# Calcula a soma dos salários antigos e dos novos salários
soma_salarios_antigos = sum(funcionario['salario_antigo'] for funcionario in funcionarios)
soma_novos_salarios = sum(funcionario['novo_salario'] for funcionario in funcionarios)

# Calcula a média das idades
media_idades = sum(funcionario['idade'] for funcionario in funcionarios) / len(funcionarios)

# Imprime os resultados
print("\nResultados:")
print("Soma dos salários antigos:", soma_salarios_antigos)
print("Soma dos novos salários:", soma_novos_salarios)
print("Média das idades:", media_idades)

# Imprime os novos salários de cada funcionário
print("\nNovos salários:")
for funcionario in funcionarios:
    print("Nome:", funcionario['nome'])
    print("Novo Salário:", funcionario['novo_salario'])
    print()