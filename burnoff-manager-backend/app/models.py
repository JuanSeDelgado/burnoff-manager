from datetime import datetime
from .db import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    membership_id = db.Column(db.Integer, db.ForeignKey("membership.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    membership = db.relationship("Membership", backref="users")

    def __repr__(self):
        return f"<User {self.full_name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "phone": self.phone,
            "membership_id": self.membership_id,
            "created_at": self.created_at.isoformat()
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Membership(db.Model):
    __tablename__ = "membership"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # Ej: "mañana", "completo", etc.
    expires_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Membership {self.type} hasta {self.expires_at}>"

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "expires_at": self.expires_at.isoformat()
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Admin(db.Model):
    __tablename__ = "admin"

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(120),nullable= False)
    type= db.Column(db.String(120),nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # hashed password
    super_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Admin {self.email}>"

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "name":self.name,
            "type":self.type,
            "super_admin": self.super_admin,
            "created_at": self.created_at.isoformat()
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

