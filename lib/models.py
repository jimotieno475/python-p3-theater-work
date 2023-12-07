from sqlalchemy import ForeignKey, Column, Integer, String, MetaData,Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
class Audition():
    __tablename__='auditions'

    id=Column(Integer(),Primary_key=True)
    actor=Column(String())
    location=Column(String())
    phone=Column(Integer())
    hired=Column(Boolean())
    role_id=Column(Integer(),ForeignKey('roles.id'))

    def __repr__(self):
        return f'Audition(id={self.id},'+\
            f'actor={self.actor},'+\
            f'location={self.location},'+\
            f'phone={self.phone},'+\
            f'hired={self.hired})'

class Role():
    __tablename__='roles'

    id=Column(Integer(),Primary_key=True)
    actor=Column(String())
    auditions = relationship("Audition", backref="role") 

    def __repr__(self):
        return f'Role(id={self.id},'+\
            f'actor={self.actor})'

    def actors(self):
        return [audition.actor for audition in self.auditions]

    def locations(self):
        return [audition.location for audition in self.auditions]

    def lead(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if hired_auditions:
            return hired_auditions[0]
        else:
            return 'no actor has been hired for this role'

    def understudy(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if len(hired_auditions) > 1:
            return hired_auditions[1]
        else:
            return 'no actor has been hired for understudy for this role'

    def call_back(self):
        hired_audition = self.lead()
        if hired_audition:
            hired_audition.hired = True