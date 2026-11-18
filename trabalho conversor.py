def celsius_para_fahrenheit (c):
    """converte temperatura de celsius para fahrenheit"""
    return (c*9/5) + 31
def kg_para_libras (kg):
    """converte peso de kg para libras"""
    return kg * 2.20462
def kg_para_litros(Kg):
    """converte kg para litros,considerando a agua (1kg = 1l)."""
    return kg * 1
#menu interativo
while True:
    print("\n---conversor---")
    print("1 - celsius para fahrenheit")
    print("2 - kg para livras")
    print("3 - kg para litros")
    print("0 - sair")
    opcao = input("escolha uma opcao:")
    if opcao == "0":
        print("saindo...ate mais!")
        break
    elif opcao =="1":
        c = float(input("digite a temperatura em celsius:"))
        print(f"{c}°c = {celsius_para_fahrenheit(c)}°f")
    elif opcao =="2":
        kg = float(input("digite o peso em kg:"))
        print(f"{kg}kg = {kg_para_libras(kg)}libras")
    elif opcao =="3":
        kg = float(input("digite o volume em kg:"))
        print(f"{kg}kg = {kg_para_litros(kg)}litros")
    else:
        print("opcao invalida,tente novamente!")