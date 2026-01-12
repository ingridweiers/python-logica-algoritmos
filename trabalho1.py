print ('Olá sejam bem-vindos a loja Ingrid Weiers')

valorDoPedido = float(input('Digite o valor do pedido:R$ '))
quantidadeParcelas = int(input('Digite a quantidade de parcelas: '))

if quantidadeParcelas < 4:
    juros = 0.0
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 0.04  # 4%
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 0.08  # 8%
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 0.16  # 16%
else:
    juros = 0.32  # 32%


valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

if quantidadeParcelas >= 4:
    print(f'O valor das parcelas é de: R$ {valorDaParcela:.2f}')
    print(f'O valor total parcelado é de: R$ {valorTotalParcelado:.2f}')
else:
    print('Sem juros aplicados.')
    print(f'Valor da parcela: R$ {valorDaParcela:.2f}')


   