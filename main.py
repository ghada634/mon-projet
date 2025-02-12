import hashlib
import math

# Vérification de sécurité avec une clé secrète (à ajouter dans les secrets GitHub)
SECRET_KEY = "changeme"  # Remplace ceci par une vraie clé dans un environnement sécurisé

def hash_secret_key(key):
    """Hash la clé secrète avec SHA-256 pour plus de sécurité."""
    return hashlib.sha256(key.encode()).hexdigest()

def complex_calculations():
    """Effectue des calculs mathématiques avancés."""
    result = sum(math.factorial(i) for i in range(1, 6))  # 1! + 2! + 3! + 4! + 5!
    return result

def main():
    """Fonction principale exécutant les fonctionnalités."""
    hashed_key = hash_secret_key(SECRET_KEY)
    print(f"Clé secrète hashée (sécurisée) : {hashed_key}")

    result = complex_calculations()
    print(f"Résultat des calculs complexes : {result}")

if __name__ == "__main__":
    main()






