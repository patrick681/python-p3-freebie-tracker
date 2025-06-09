from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, declarative_base
from flask_sqlalchemy import SQLAlchemy

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

db = SQLAlchemy(metadata=metadata)

class Company(db.Model):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    freebies = relationship('Freebie', back_populates='company')

    def __repr__(self):
        return f'<Company {self.name}>'
    def give_freebie(self, dev, item_name, value):
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        db.session.add(new_freebie)
        db.session.commit()


class Dev(db.Model):
    __tablename__ = 'devs'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    freebies = relationship('Freebie', back_populates='dev')

    def __repr__(self):
        return f'<Dev {self.name}>'
    def received_one(self, item_name):
        return any(f.item_name == item_name for f in self.freebies)

def give_away(self, dev, freebie):
    if freebie in self.freebies:
        freebie.dev = dev
        db.session.commit()


class Freebie(db.Model):
    __tablename__ = 'freebies'
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)

    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    dev = relationship('Dev', back_populates='freebies')
    company = relationship('Company', back_populates='freebies')

    def __repr__(self):
        return f'<Freebie {self.item_name} (${self.value})>'
    def print_details(self):
        print(f"{self.dev.name} owns a {self.item_name} from {self.company.name}")
