# --- 1.1 Calculadora Simples ---
class Calculadora:
    def somar(self, a, b):
        return a + b
    def subtrair(self, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b
    def dividir(self, a, b):
        if b == 0:
            return "Erro: divisao por zero"
        return a / b

calc = Calculadora()
num1 = 10
num2 = 5
print(f"{num1} + {num2} = {calc.somar(num1, num2)}")
print(f"{num1} - {num2} = {calc.subtrair(num1, num2)}")
print(f"{num1} * {num2} = {calc.multiplicar(num1, num2)}")
print(f"{num1} / {num2} = {calc.dividir(num1, num2)}")


# --- 1.2 Verificador de Palíndromos ---
def eh_palindromo(texto):
    texto_simples = texto.lower().replace(' ', '')
    return texto_simples == texto_simples[::-1]

palavra1 = "ovo"
palavra2 = "Ame a ema"
palavra3 = "python"
print(f'"{palavra1}" é palíndromo? {eh_palindromo(palavra1)}')
print(f'"{palavra2}" é palíndromo? {eh_palindromo(palavra2)}')
print(f'"{palavra3}" é palíndromo? {eh_palindromo(palavra3)}')


# --- 1.3 Fatorial (Recursivo) ---
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

numero_fatorial = 5
print(f"O fatorial de {numero_fatorial} é {fatorial(numero_fatorial)}")


# --- 1.4 Conversor de Temperaturas ---
class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
    def fahrenheit_para_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

conversor = ConversorTemperatura()
temp_c = 25
temp_f = 77
print(f"{temp_c}°C em Fahrenheit é {conversor.celsius_para_fahrenheit(temp_c):.2f}°F")
print(f"{temp_f}°F em Celsius é {conversor.fahrenheit_para_celsius(temp_f):.2f}°C")


# --- 2.1 Maior e Menor Elemento em uma Matriz ---
matriz_exemplo = [
    [10, 5, 3],
    [25, 2, 7],
    [1, 18, 32]
]
maior = matriz_exemplo[0][0]
menor = matriz_exemplo[0][0]

for linha in matriz_exemplo:
    for numero in linha:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print("Matriz:")
for linha in matriz_exemplo:
    print(linha)
print(f"Maior elemento: {maior}")
print(f"Menor elemento: {menor}")


# --- 2.2 Soma das Diagonais de uma Matriz Quadrada ---
matriz_quadrada = [
    [4, 6, 8],
    [1, 5, 9],
    [2, 7, 3]
]
n = len(matriz_quadrada)
soma_principal = 0
soma_secundaria = 0

for i in range(n):
    soma_principal += matriz_quadrada[i][i]
    soma_secundaria += matriz_quadrada[i][n - 1 - i]

print("Matriz Quadrada:")
for linha in matriz_quadrada:
    print(linha)
print(f"Soma da diagonal principal: {soma_principal}")
print(f"Soma da diagonal secundária: {soma_secundaria}")


# --- 3.1 Manipulando Dados de um Objeto ---
class NumeroContainer:
    def __init__(self, valor):
        self.valor = valor
    def imprimir_valor(self):
        print(f"O valor do atributo é: {self.valor}")

meu_numero = NumeroContainer(100)
meu_numero.imprimir_valor()
print(f"ID do objeto (simula endereço): {id(meu_numero)}")


# --- 3.2 Trocando Valores entre Objetos ---
class ValorContainer:
    def __init__(self, valor):
        self.valor = valor

def trocar_valores(obj1, obj2):
    valor_temporario = obj1.valor
    obj1.valor = obj2.valor
    obj2.valor = valor_temporario

objA = ValorContainer(10)
objB = ValorContainer(20)
print(f"Antes da troca: objA.valor = {objA.valor}, objB.valor = {objB.valor}")
trocar_valores(objA, objB)
print(f"Depois da troca: objA.valor = {objA.valor}, objB.valor = {objB.valor}")


# --- 4.1 Sistema de Gerenciamento de Funcionários ---
class Funcionario:
    def __init__(self, nome, id_func, salario, departamento):
        self.nome = nome
        self.id = id_func
        self.salario = salario
        self.departamento = departamento

funcionarios = [
    Funcionario("Ana", 1, 3000.00, "Vendas"),
    Funcionario("Marcos", 2, 3500.00, "TI"),
    Funcionario("Carlos", 3, 4200.00, "TI")
]

print("Lista de todos os funcionários:")
for func in funcionarios:
    print(f"ID: {func.id}, Nome: {func.nome}, Salário: R${func.salario:.2f}, Depto: {func.departamento}")

total_salarios_ti = 0
depto_alvo = "TI"
for func in funcionarios:
    if func.departamento == depto_alvo:
        total_salarios_ti += func.salario
print(f"\nTotal de salários do departamento '{depto_alvo}': R${total_salarios_ti:.2f}")


# --- 4.2 Agenda de Contatos ---
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

agenda = [
    Contato("Lucas", "11-9999-8888", "lucas@email.com"),
    Contato("Maria", "21-7777-6666", "maria@email.com")
]

print("Lista de contatos na agenda:")
for contato in agenda:
    print(f"Nome: {contato.nome}, Tel: {contato.telefone}, Email: {contato.email}")

nome_busca = "Lucas"
contato_encontrado = None
for contato in agenda:
    if contato.nome == nome_busca:
        contato_encontrado = contato
        break

print(f"\nBuscando por '{nome_busca}':")
if contato_encontrado:
    print(f"Telefone: {contato_encontrado.telefone}")
    print(f"Email: {contato_encontrado.email}")
else:
    print("Contato não encontrado.")