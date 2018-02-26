import peewee
from flask import Flask, jsonify, request

banco = peewee.MySQLDatabase('u635695917_pytho', user='u635695917_orix', password='brq@3007', host='mysql.hostinger.com.br', port=3306)

class Musica(peewee.Model):
    codigo = peewee.AutoField()
    titulo = peewee.TextField()
    artista = peewee.TextField()
    ano = peewee. IntegerField()

    def to_dict(self):
        return {'id':self.codigo, 'titulo': self.titulo, 'artista': self.artista, 'ano': self.ano}

    class Meta:
        database = banco