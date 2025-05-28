# lib/seed.py

from lib.app import create_app
from lib.models import db, Company, Dev, Freebie

def seed_data():
    # Clear existing data
    Company.query.delete()
    Dev.query.delete()
    Freebie.query.delete()
    db.session.commit()

    # Create Companies
    company1 = Company(name="TechCorp", founding_year=2010)
    company2 = Company(name="DevSolutions", founding_year=2015)

    # Create Devs
    dev1 = Dev(name="Alice")
    dev2 = Dev(name="Bob")

    # Create Freebies
    freebie1 = Freebie(item_name="Sticker Pack", value=10, company=company1, dev=dev1)
    freebie2 = Freebie(item_name="Mug", value=15, company=company2, dev=dev2)
    freebie3 = Freebie(item_name="T-Shirt", value=20, company=company1, dev=dev2)

    # Add to session
    db.session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_data()
