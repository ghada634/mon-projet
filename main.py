# main.py

def hello_world(name="World"):
    """Retourne un message de salutation personnalisé."""
    return f"Hello, {name}!"

def get_user_input():
    """Demande à l'utilisateur d'entrer son nom."""
    name = input("Entrez votre nom (laisser vide pour 'World'): ").strip()
    if not name:
        name = "World"  # Valeur par défaut si l'utilisateur ne saisit rien
    return name

def main():
    """Point d'entrée du programme."""
    name = get_user_input()
    greeting = hello_world(name)
    print(greeting)

if __name__ == "__main__":
    main()



