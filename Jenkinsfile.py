import time
import sys

def build():
    print(" Étape BUILD : Compilation de l'application...")
    time.sleep(2)
    print(" Compilation terminée.")

def test():
    print(" Étape TEST : Lancement des tests...")
    time.sleep(2)
    print(" Tous les tests sont passés.")

def deploy():
    print(" Étape DEPLOY : Déploiement de l'application...")
    time.sleep(2)
    print(" Déploiement terminé.")

if name == "main":
    if len(sys.argv) < 2:
        print(" Veuillez spécifier une étape à exécuter : build, test, deploy")
        sys.exit(1)

    step = sys.argv[1]
    if step == "build":
        build()
    elif step == "test":
        test()
    elif step == "deploy":
        deploy()
    else:
        print(f" Étape inconnue : {step}")
        sys.exit(1)
