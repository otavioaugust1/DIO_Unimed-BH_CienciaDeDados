# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
salario = int(input()) 

if salario <= 600.00: 
    percentual = 0.17  
     
elif salario >= 600.01 and salario <=900.00:
    percentual = 0.13    
     
elif salario >= 900.01 and salario <=1500.00: 
    percentual = 0.12   

elif salario >= 1500.01 and salario <=2000.00: 
    percentual = 0.10
    
else: percentual = 0.05

novoSalario = (salario * (percentual + 1))
reajuste = (novoSalario - salario)

p = int(percentual * 100)

print(f"Novo salario: {(novoSalario):.2f}\n Reajuste ganho: {reajuste:.2f}\n Em percentual: {p} %".replace(".","."))


# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)