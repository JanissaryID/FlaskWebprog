 DROP TABLE IF EXISTS user ;
DROP TABLE IF EXISTS post ;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT ,
  username TEXT UNIQUE NOT NULL ,
  password TEXT NOT NULL
);

CREATE TABLE Barang (
    kodeBarang  CHAR (5)     PRIMARY KEY
                             UNIQUE
                             NOT NULL,
    namaBarang  CHAR (30)    NOT NULL,
    satuan      INTEGER (5)  NOT NULL,
    hargaSatuan INTEGER (20) NOT NULL,
    Merk        CHAR (30)    NOT NULL,
    gambar      CHAR (100)   NOT NULL
);