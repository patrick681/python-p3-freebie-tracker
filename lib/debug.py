from lib.app import create_app
from lib.models import db, Company, Dev, Freebie

def run_tests():
    app = create_app()
    with app.app_context():
        # Drop all tables and recreate fresh
        db.drop_all()
        db.create_all()
        
        # Seed data (same as your seed.py)
        company1 = Company(name="TechCorp", founding_year=2010)
        company2 = Company(name="DevSolutions", founding_year=2015)
        dev1 = Dev(name="Alice")
        dev2 = Dev(name="Bob")
        freebie1 = Freebie(item_name="Sticker Pack", value=10, company=company1, dev=dev1)
        freebie2 = Freebie(item_name="Mug", value=15, company=company2, dev=dev2)
        freebie3 = Freebie(item_name="T-Shirt", value=20, company=company1, dev=dev2)

        db.session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
        db.session.commit()

        # Test queries
        print("All Companies:")
        for c in Company.query.all():
            print(c, "with freebies:", c.freebies)

        print("\nAll Devs:")
        for d in Dev.query.all():
            print(d, "with freebies:", d.freebies)

        print("\nFreebies owned by Dev Bob:")
        bob = Dev.query.filter_by(name="Bob").first()
        for f in bob.freebies:
            print(f)

        # Test relationship access
        freebie = Freebie.query.first()
        print("\nFreebie and its company and dev:")
        print(freebie, freebie.company, freebie.dev)

        print("\n[Dev.all()] Listing all devs using classmethod:")
        for dev in Dev.all():
            print(dev)

        print("\n[Freebie.print_details()] on the first freebie:")
        if freebie:
            freebie.print_details()
            
if __name__ == "__main__":
    run_tests()
