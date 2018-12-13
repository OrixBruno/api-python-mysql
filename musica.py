import peewee
from flask import Flask, jsonify, request

banco = peewee.MySQLDatabase('sqlConn', user='user', password='pass', host='server.net', port=3306)

class Musica(peewee.Model):
    codigo = peewee.AutoField()
    titulo = peewee.TextField()
    artista = peewee.TextField()
    ano = peewee. IntegerField()

    def to_dict(self):
        return {'id':self.codigo, 'titulo': self.titulo, 'artista': self.artista, 'ano': self.ano}

    class Meta:
        database = banco