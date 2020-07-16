#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Animal

# Cf. 00_DatabaseCreation.py
engine = create_engine('sqlite:///database.db')

# Création de données
zebra = Animal(name="Zèbre")
print("Création d'un %s" % zebra.name)

# Insertion de données
# Insertion - création d'une session
Session = sessionmaker(bind=engine)
session = Session()
# Insertion - ajout du Zèbre
session.add(zebra)
# Insertion - envoi dans la base de données
session.commit()
