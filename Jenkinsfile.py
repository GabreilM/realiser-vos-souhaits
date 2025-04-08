import os
import time

def build():
    print("🔨 Étape BUILD : Compilation de l'application...")
    time.sleep(2)
    print("✅ Compilation terminée.")

def test():
    print("🧪 Étape TEST : Lancement des tests...")
    time.sleep(2)
    # Simuler un test qui passe
    test_result = True
    if test_result:
        print("✅ Tous les tests sont passés.")
    else:
        print("❌ Des tests ont échoué.")
        exit(1)

def deploy():
    print("🚀 Étape DEPLOY : Déploiement de l'application...")
    time.sleep(2)
    print("✅ Déploiement effectué avec succès.")

if name == "main":
    build()
    test()
    deploy()
