from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from Web.auth import login_required
from Web.db import get_db

bp = Blueprint('warehouse', __name__)

@bp.route('/barang')
def index():
    db = get_db()
    # container = []
    # for kodeBarang,namaBarang,satuan,hargaSatuan,Merk,gambar in db.execute('SELECT * FROM Barang'):
    #     container.append((ids,nama,satuan,harga,Merk,gambar))
    return 'hello'


