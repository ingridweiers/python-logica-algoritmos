print("Bem-vindos à empresa de Ingrid Weiers")

# Lista para armazenar os funcionários
lista_funcionarios = []
# ID global inicializado com o RU (exemplo)
id_global = 4297913

def cadastrar_funcionario(id):
    print(f"Id do funcionário: {id_global}")
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    
    # Criando um dicionário com os dados do funcionário
    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    
    # Adicionando o funcionário à lista
    lista_funcionarios.append(funcionario.copy())
    print("Funcionário cadastrado com sucesso!")

def consultar_funcionarios():
    while True:
        print("\nOpções de consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\nTodos os funcionários:")
            for func in lista_funcionarios:
                print(func)
        elif opcao == "2":
            id_consulta = int(input("Digite o ID do funcionário: "))
            for func in lista_funcionarios:
                if func["id"] == id_consulta:
                    print("\nFuncionário encontrado:")
                    print(func)
                    break
            else:
                print("Funcionário não encontrado.")
        elif opcao == "3":
            setor_consulta = input("Digite o setor: ")
            print(f"\nFuncionários do setor {setor_consulta}:")
            for func in lista_funcionarios:
                if func["setor"].lower() == setor_consulta.lower():
                    print(func)
        elif opcao == "4":
            return
        else:
            print("Opção inválida")

def remover_funcionario():
    while True:
        id_remover = int(input("Digite o ID do funcionário a ser removido: "))
        for func in lista_funcionarios:
            if func["id"] == id_remover:
                lista_funcionarios.remove(func)
                print("Funcionário removido com sucesso!")
                return
        print("Id inválido")

# Menu principal
while True:
    print("\nMenu Principal:")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        id_global += 1
        cadastrar_funcionario(id_global)
    elif opcao == "2":
        consultar_funcionarios()
    elif opcao == "3":
        remover_funcionario()
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida")

# Exemplo de uso:
# Cadastro de 3 funcionários
cadastrar_funcionario(id_global)
id_global += 1
cadastrar_funcionario(id_global)
id_global += 1
cadastrar_funcionario(id_global)

# Consulta de todos os funcionários
consultar_funcionarios()

# Consulta por ID
id_consulta = id_global - 1
print(f"\nConsulta por ID {id_consulta}:")
for func in lista_funcionarios:
    if func["id"] == id_consulta:
        print(func)
        break

# Consulta por setor
setor_consulta = "TI"
print(f"\nConsulta por setor {setor_consulta}:")
for func in lista_funcionarios:
    if func["setor"].lower() == setor_consulta.lower():
        print(func)