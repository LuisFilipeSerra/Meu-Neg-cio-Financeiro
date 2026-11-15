
# MEU NEGÓCIO FINANCEIRO
# Sistema de controle financeiro para pequenos empreendedores

print("===================================")
print("       MEU NEGÓCIO FINANCEIRO")
print("===================================")

# Entrada de dados
total_receitas = float(input("Digite o total de receitas: R$ "))
total_despesas = float(input("Digite o total de despesas: R$ "))

# Operação aritmética
saldo = total_receitas - total_despesas

# Saída de dados
print("\n===== RESUMO FINANCEIRO =====")
print(f"Total de receitas: R$ {total_receitas:.2f}")
print(f"Total de despesas: R$ {total_despesas:.2f}")
print(f"Saldo atual: R$ {saldo:.2f}")


# Análise da situação financeira
if saldo > 0:
    print("Situação financeira: saldo positivo")
elif saldo < 0:
    print("Situação financeira: saldo negativo")
else:
    print("Situação financeira: saldo zerado")