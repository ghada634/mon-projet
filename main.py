import math

# Fonctions pour effectuer les calculs
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erreur : Division par zéro"
    return x / y

def square_root(x):
    if x < 0:
        return "Erreur : Nombre négatif pour la racine carrée"
    return math.sqrt(x)

# Fonction pour exécuter des calculs
def calculate():
    # Valeurs d'exemple pour les tests
    num1 = 10
    num2 = 5

    # Effectuer des calculs
    print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
    print(f"Soustraction: {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
    print(f"Division: {num1} / {num2} = {divide(num1, num2)}")
    
    # Calcul de la racine carrée d'un nombre
    num = 16
    print(f"Racine carrée: √{num} = {square_root(num)}")

if __name__ == "__main__":
    calculate()





