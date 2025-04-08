import datetime
import random

objectifs = {
    "Janvier": "Bouge ton corps ! 5 séances de sport par semaine pour ton moral et ton corps :muscle:",
    "Février": "Marche vers le bien-être ! 10 000 pas par jour, chaque pas compte :man_walking:",
    "Mars": "Plonge dans les livres ! Lis un livre par semaine :books:",
    "Avril": "Fais résonner la musique ! Apprends un instrument :notes:",
    "Mai": "Partez à la découverte du monde ! Ose l’aventure :earth_africa:",
    "Juin": "Enrichis ton vocabulaire ! Apprends 10 mots par semaine dans une autre langue :brain:",
    "Juillet": "Deviens maître de ton budget ! Fixe-toi un objectif financier :moneybag:",
    "Août": "Savoure les liens ! Organise un repas par semaine avec tes proches :fork_knife_plate:",
    "Septembre": "Commence la journée en paix ! 5 min de méditation chaque matin :person_in_lotus_position:",
    "Octobre": "Essaie un nouveau sport ! Découvre-toi autrement :ping_pong:",
    "Novembre": "Sois la lumière de quelqu’un ! Une bonne action par semaine :sparkles:",
    "Décembre": "Prends des nouvelles ! Appelle un proche chaque semaine :telephone_receiver:"
}

# Liste d'encouragements aléatoires
encouragements = [
    "Tu peux le faire, ne lâche rien ! :fire:",
    "Chaque petit pas te rapproche de ton objectif :raised_hands:",
    "Continue comme ça, tu es sur la bonne voie :100:",
    "Un jour à la fois, mais avec détermination :muscle:",
    "Bravo pour tes efforts, ils comptent vraiment :clap:"
]

def afficher_objectif_du_mois():
    mois = datetime.datetime.now().strftime("%B")
    mois = mois.capitalize()
    print(f"\n:dart: Objectif de {mois} :")
    print(objectifs.get(mois, "Aucun objectif défini pour ce mois."))

def envoyer_rappel_quotidien():
    print(f"\n:date: Rappel quotidien : N'oublie pas ton challenge du mois !")

def afficher_encouragement():
    message = random.choice(encouragements)
    print(f"\n:love_letter: Message d'encouragement : {message}")

def main():
    afficher_objectif_du_mois()
    envoyer_rappel_quotidien()
    afficher_encouragement()

if __name__ == "__main__":
    main()
