#!/usr/bin/env python3

from sqlalchemy import create_engine
from tables import Base

# Moteur pour la communication avec la base de données
engine = create_engine('sqlite:///database.db')

# Table: création => créé théoriquement le fichier 'database.db'
Base.metadata.create_all(bind=engine)
