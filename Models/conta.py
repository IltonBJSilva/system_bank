from .database import db
from datetime import datetime

class Conta(db.Model):
    __tablename__ = 'contas'
    id = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Numeric(10, 2), default=0.0)
    saques_diarios = db.Column(db.Integer, default=0)
    transacoes = db.relationship('Transacao', backref='conta', lazy=True)

    def __repr__(self):
        return f"<Conta {self.id}>"

class Transacao(db.Model):
    __tablename__ = 'transacoes'
    id = db.Column(db.Integer, primary_key=True)
    conta_id = db.Column(db.Integer, db.ForeignKey('contas.id'), nullable=False)
    tipo = db.Column(db.String(10), nullable=False) # 'deposito' ou 'saque'
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Transacao {self.id} - {self.tipo} - {self.valor}>"