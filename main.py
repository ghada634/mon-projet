# main.py

def hello_world(name="World"):
    """Retourne un message de salutation personnalisé."""
    return f"Hello, {name}!"

def get_user_input():
    """Demande à l'utilisateur d'entrer son nom."""
    # Si le programme ne peut pas demander à l'utilisateur, utilise une valeur par défaut
    name = "World"  # Valeur par défaut
    return name

def main():
    """Point d'entrée du programme."""
    name = get_user_input()
    greeting = hello_world(name)
    print(greeting)

if __name__ == "__main__":
    main()




