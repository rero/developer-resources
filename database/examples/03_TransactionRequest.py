#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Animal


# Lien avec la base de données
engine = create_engine('sqlite:///database.db')

# Création de plusieurs sessions
Session = sessionmaker(bind=engine)
session1 = Session()  # essai 1 de la transaction
session2 = Session()  # essai 2 avec erreur
session3 = Session()  # essai 3 avec erreur + rollback
session4 = Session()  # essai 4 avec erreur + rollback (en plus tendu)
lecture = Session()  # seulement pour vérification

# Préparation de plusieurs objets
# sachant que le Zèbre a déjà été enregistré !
lion = Animal(name='Lion')
giraffe = Animal(name='Girafe')
monkey = Animal(name='Singe')
elephant = Animal(name='Éléphant')
snake = Animal(name='Serpent')


def display_count(session_name):
    total = lecture.query(Animal).count()
    print("Avant session %s : %s" % (str(session_name), total))
    print("\t%s" % [x.name for x in lecture.query(Animal).all()])


# Transaction - version 1: à la manière facile
# begin_nested() créer un point de sauvegarde pour éventuellement
# revenir en arrière
display_count(1)
with session1.begin_nested():
    session1.add(lion)
    session1.add(snake)
# version 1: vérification
assert lecture.query(Animal).count() == 3  # Avec le zèbre

# Transaction - version 2: avec erreur (et donc try/except)
# SI une erreur survient => un rollback est effectué
display_count(2)
session2.begin_nested()
try:
    session2.add(giraffe)
    raise
    session2.add(monkey)
    session2.commit()
except:
    # no rollback
    pass
# version 2 : vérification
assert lecture.query(Animal).count() == 3

# Transaction - version 3: la même que la 2, avec erreur (en plus tendu)
display_count(3)
session3.begin_nested()
session3.add(elephant)  # l'éléphant arrive !
session3.commit()
try:
    session3.add(giraffe)
    raise
    session3.add(monkey)
    session3.commit()
except:
    session3.rollback()
# version 3 : vérification
# L'éléphant est resté car il y a eu un commit !
assert lecture.query(Animal).count() == 4

# Transaction - version 4: la même que la 3, plus compliqué
display_count(4)
session4.begin_nested()
try:
    session4.add(giraffe)
    session4.commit()
    raise
    session4.add(monkey)
    session4.commit()
except:
    session4.rollback()
# version 4 : vérification
# Tout le bloc du try est annulé ! Même avec un commit !
assert lecture.query(Animal).count() == 4
