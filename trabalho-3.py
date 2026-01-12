def escolha_modelo():
    while True:
        try:
            modelo = input("Escolha o modelo de camiseta desejado (MCS - Manga Curta Simples   MLS - Manga Longa Simples , MCE - Manga Curta com Estampa, MLE - Manga Longa com Estampa): ").strip().upper()
            if modelo in ["MCS", "MLS", "MCE", "MLE"]:
                if modelo == "MCS":
                    return 1.80
                elif modelo == "MLS":
                    return 2.10
                elif modelo == "MCE":
                    return 2.90
                elif modelo == "MLE":
                    return 3.20
            else:
                print("Opção de modelo inválida. Por favor, escolha entre MCS, MLS, MCE ou MLE.")
        except KeyboardInterrupt:
            print("\n\nOperação interrompida pelo usuário.")
            exit()
        except Exception as e:
            print(f"Erro: {e}")

def num_camisetas():
    while True:
        try:
            num_camisetas = int(input("Digite o número de camisetas desejado: "))
            if num_camisetas < 20:
                return num_camisetas
            elif num_camisetas >= 20 and num_camisetas < 200:
                return num_camisetas * 0.95  # Aplica desconto de 5%
            elif num_camisetas >= 200 and num_camisetas < 2000:
                return num_camisetas * 0.93  # Aplica desconto de 7%
            elif num_camisetas >= 2000 and num_camisetas <= 20000:
                return num_camisetas * 0.88  # Aplica desconto de 12%
            else:
                print("Não aceitamos tantas camisetas de uma vez.")
        except KeyboardInterrupt:
            print("\n\nOperação interrompida pelo usuário.")
            exit()
        except ValueError:
            print("Valor inválido. Digite apenas números inteiros.")

def frete():
    while True:
        try:
            opcao_frete = int(input("Escolha o tipo de frete desejado:\n"
                                    "1 - Transportadora (adicional R$ 100.00)\n"
                                    "2 - Sedex (adicional R$ 200.00)\n"
                                    "0 - Retirar na fábrica (sem custo adicional)\n"
                                    "Opção: "))
            if opcao_frete in [0, 1, 2]:
                if opcao_frete == 1:
                    return 100.00
                elif opcao_frete == 2:
                    return 200.00
                else:
                    return 0.00
            else:
                print("Opção de frete inválida. Por favor, escolha entre 1, 2 ou 0.")
        except KeyboardInterrupt:
            print("\n\nOperação interrompida pelo usuário.")
            exit()
        except Exception as e:
            print(f"Erro: {e}")

def main():
    try:
        print("Sejam bem-vindos a fábrica de camisetas da Ingrid Weiers")
    
        # Escolha do modelo
        modelo = escolha_modelo()
        print(f"\nModelo escolhido: {modelo:.2f} reais por unidade\n")

        # Número de camisetas
        num_camisas = num_camisetas()
        if isinstance(num_camisas, int):
            total_camisas = modelo * num_camisas
        else:
            total_camisas = num_camisas  # Já é o total com desconto aplicado
        print(f"\nNúmero de camisetas escolhido: {int(num_camisas)}\n")

        # Tipo de frete
        valor_frete = frete()
        if valor_frete > 0:
            print(f"\nFrete escolhido: Adicional de {valor_frete:.2f} reais\n")
        else:
            print("\nFrete escolhido: Retirar na fábrica\n")

        # Cálculo do total a pagar
        total = total_camisas + valor_frete
        print(f"== Total a Pagar ==\n{total:.2f} reais")

    except KeyboardInterrupt:
        print("\n\nOperação interrompida pelo usuário.")
        exit()
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
if __name__ == "__main__":
    main()