#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Animal


# Lien avec la base de données
engine = create_engine('sqlite:///database.db')

# Création d'une session
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

query = session.query(Animal).all()
for res in query:
    print(res)
