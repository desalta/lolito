from app import db

class Runas(db.Model):
    __tablename__ = 'runas'

    name = db.Column(db.String(50), primary_key=True)
    prim_runa = db.Column(db.String(5))
    prim_clave = db.Column(db.String(5))
    prim_ran1 = db.Column(db.String(5))
    prim_ran2 = db.Column(db.String(5))
    prim_ran3 = db.Column(db.String(5))
    sec_runa = db.Column(db.String(5))
    sec_ran1 = db.Column(db.String(5))
    sec_ran2 = db.Column(db.String(5))
    frag1 = db.Column(db.String(5))
    frag2 = db.Column(db.String(5))
    frag3 = db.Column(db.String(5))

    def sett(self, prim_runa,prim_clave,prim_ran1,prim_ran2,prim_ran3,sec_runa,sec_ran1,sec_ran2,frag1,frag2,frag3):
        self.prim_runa = prim_runa
        self.prim_clave = prim_clave
        self.prim_ran1 = prim_ran1
        self.prim_ran2 = prim_ran2
        self.prim_ran3 = prim_ran3
        self.sec_runa = sec_runa
        self.sec_ran1 = sec_ran1
        self.sec_ran2 = sec_ran2
        self.frag1 = frag1
        self.frag2 = frag2
        self.frag3 = frag3
        return self

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def delete(name):
        emp = Runas.query.get(name)
        if emp is not None:
            db.session.delete(emp)
            db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def get(name):
        return Runas.query.get(name)

    @staticmethod
    def get_all():
        return Runas.query.order_by(Runas.name.asc()).all()