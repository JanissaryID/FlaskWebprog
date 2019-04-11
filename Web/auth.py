import functools
import datetime as dt

from flask import (
    Blueprint , flash , g , redirect , render_template , request , session , url_for
)
from werkzeug.security import check_password_hash , generate_password_hash

from Web.db import get_db
# from . import warehouse

bp = Blueprint ( 'auth' , __name__ , url_prefix = '/auth' )
tgl = dt.date.isoformat(dt.date.today())
thn = tgl[2:4]
bln = tgl[5:7]

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('auth.barang'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/barang', methods=('GET', 'POST'))
def barang():
    db = get_db()
    brng = db.execute('SELECT * FROM Barang')
    # db.commit()
    return render_template('auth/barang.html',container = brng )

@bp.route('/hapus/<ide>', methods=('GET', 'POST'))
def Hapus(ide):
    db = get_db()
    db.execute('DELETE FROM Barang WHERE kodeBarang=?',(ide,))
    db.commit()
    return redirect(url_for('auth.barang'))

    


@bp.route('/tambah', methods=('GET', 'POST'))
def tambah():
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        satuan = request.form['satuan']
        harga = request.form['harga']
        bukti = 'M'+thn+'/'+bln+'/'+'001'
        merk = request.form['merk']
        gambar = request.form['gambar']
        db = get_db()
        error = None
        if error is None:
            db.execute(
                'INSERT INTO Barang (kodeBarang,namaBarang,satuan,hargaSatuan,Tanggal,Merk,gambar) VALUES (?, ?, ?, ?, ?, ?, ?)',
                (kode, nama, satuan, harga,bukti ,merk, gambar)
            )
            db.commit()
            return redirect(url_for('auth.barang'))

        flash(error)

    return render_template('auth/tambah.html')

@bp.route('/ubah/<ide>', methods=('GET', 'POST'))
def ubah(ide):
    db = get_db()
    brng = db.execute('SELECT * FROM Barang WHERE kodeBarang=?',(ide,)).fetchone()

    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        satuan = int(request.form['satuan'])
        harga = int(request.form['harga'])
        merk = request.form['merk']
        gambar = request.form['gambar']
        db = get_db()
        error = None
        if error is None:
            db.execute(''' UPDATE Barang SET namaBarang = ?,satuan = ?,hargaSatuan = ?,Merk =?,gambar =? WHERE kodeBarang = ? ''',(nama,satuan,harga,merk,gambar,ide))
            db.commit()
            return redirect(url_for('auth.barang'))

        flash(error)

    return render_template('auth/edit.html', data = brng)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('warehouse.index'))

        return view(**kwargs)

    return wrapped_view