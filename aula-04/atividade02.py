#meta de 1000 reais, solicita o valor total das vendas e diz se bateu a meta

valor_total_vendas = float(input("Qual o valor total das vendas. "))
META = 1000

if valor_total_vendas >= META:
    print("Parabéns! A meta foi batida esse mês.")
else:
    print("A meta não foi batida esse mês.")