print ("Olá sejam bem-vindos a loja de marmitas Ingrid Weiers")
print("                    Cardápio:")
print("  | Tamanho |   Bife acebolado(BA)    |   Filé de Frango (FF) |")
print("  |    P    |       R$16.00           |        R$15.00        |")     
print("  |    M    |       R$18.00           |        R$17.00        |")
print("  |    G    |       R$22.00           |        R$21.00        |")
 
#Primeiro, crie um dicionário para mapear os códigos dos sabores para seus nomes completos
sabores = {
    "BA": "bife acebolado",
    "FF": "filé de frango"
}

total_pedido = 0

while True:
    # B. Input do sabor (BA/FF)
    sabor = input("Escolha o sabor (BA/FF): ")
    
    # Verifica se o sabor é válido
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente.")
        continue  # Reinicia o loop para pedir o sabor novamente
    
    # C. Input do tamanho (P/M/G)
    tamanho = input("Escolha o tamanho (P/M/G): ")
    
    # Verifica se o tamanho é válido
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        continue  # Reinicia o loop para pedir o tamanho novamente
    
    # D. Calcula o valor do pedido com base no sabor e tamanho escolhidos
    if sabor == "BA":
        if tamanho == "P":
            valor_pedido = 16
        elif tamanho == "M":
            valor_pedido = 18
        elif tamanho == "G":
            valor_pedido = 22
    elif sabor == "FF":
        if tamanho == "P":
            valor_pedido = 15
        elif tamanho == "M":
            valor_pedido = 17
        elif tamanho == "G":
            valor_pedido = 21
    
    # E. Acumula o valor do pedido ao total_pedido
    total_pedido += valor_pedido
    
# linha modificada que imprime o pedido atual para usar este dicionário e formatar a mensagem conforme desejado
    print(f"Você pediu um {sabores[sabor]} no tamanho {tamanho}: R$ {valor_pedido:.2f}")
    
    # Pergunta se deseja pedir mais alguma coisa
    continuar = input("Deseja pedir mais alguma coisa? (S/N): ")
    if continuar.upper() != "S":
        break  # Encerra o loop se a resposta não for 'S' (sim)

# F. Imprime o total do pedido acumulado
print(f"Total do pedido: R$ {total_pedido:.2f}")