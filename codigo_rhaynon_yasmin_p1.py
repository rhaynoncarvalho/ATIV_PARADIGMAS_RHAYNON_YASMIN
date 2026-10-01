def somar (a,b):
    return (a + b)
    
def subtrair (a,b):
    return (a - b)
    
def multiplicar (a,b):
    return (a * b)
    
def dividir (a,b):
    if b == 0:
        return "Erro: Não é possível dividir por 0."
    return a / b


def calculadora ():
    continuar = True
    
    while continuar:
        print("\n CALDULADORA")
        print("1 - SOMAR")
        print("2 - SUBTRAIR")
        print("3 - MULTIPLICAR")
        print("4 - DIVIDIR")
        print("5 - SAIR")
        
        opcao = int(input("Escolha uma opção: "))
        
        
        if opcao == "5":
            continuar = False
            print("Calduladora encerrada.")
        
        elif opcao in ["1", "2", "3", "4"]:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
        
        
            if opcao == "1":
                resultado = somar(numero1, numero2)
            elif opcao == "2":
                resultado = subtrair(numero1, numero2)
            elif opcao == "3":
                resultado = multiplicar(numero1, numero2)
            else:
                resultado = dividir(numero1, numero2)
                
            print ("Resultado:", resultado)
            
        else:
            print ("Opção inválida.")
        

calculadora()
            
    
        
    
    
    
    
