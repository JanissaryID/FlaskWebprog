from flask_wtf import Form
from wtforms import *

class barangform(Form):
    kode = StringField('Id',[validators.Length(min=4,max=5),validators.DataRequired(),validators.Required('Not Empty')])
    nama = StringField('Nama',[validators.Length(min=4,max=100),validators.DataRequired(),validators.Required('Not Empty')])
    satuan = IntegerField('Satuan',[validators.Length(min=4,max=20),validators.DataRequired(),validators.Required('Not Empty')])
    Harga = IntegerField('Harga',[validators.Length(min=4,max=20),validators.DataRequired(),validators.Required('Not Empty')])
    Merk = StringField('Merk',[validators.Length(min=4,max=20),validators.DataRequired(),validators.Required('Not Empty')])
    Gambar = FileField('Gambar',[validators.Required('Not Empty')])