import os

def check_secret_key():
    """Vérifie si la clé secrète est correcte."""
    secret_key = os.getenv("MY_SECRET_KEY", "default_value")
    expected_key = "SuperSecretKey123"

    if secret_key == expected_key:
        print("✅ Clé correcte : Accès autorisé")
    else:
        print("❌ Clé incorrecte : Accès refusé")

if __name__ == "__main__":
    check_secret_key()






