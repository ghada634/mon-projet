# main.py

def hello_world(name="World"):
    """Retourne un message de salutation personnalisé."""
    return f"Hello, {name}!"

def main():
    """Demande un nom à l'utilisateur et affiche un message de salutation."""
    name = input("Entrez votre nom : ").strip()
    if not name:
        name = "World"  # Valeur par défaut si l'utilisateur ne saisit rien
    print(hello_world(name))

if __name__ == "__main__":
    main()


