CREATE DATABASE eco_system;

USE eco_system;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE usuarios_eco( 
    id_usuario_eco integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(50) NOT NULL,
    apellido_paterno varchar(50) NOT NULL,
    apellido_materno varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    telefono varchar(50) NOT NULL,
    descripcion text NOT NULL
    )ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE guardado(
    id_guardado int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_post  int     null
    )ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE comentarios(
    id_comentario int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario  varchar(15)     not null,
    apellido_p  varchar(15) not null,
    fecha_comentario    datetime    not null);

CREATE TABLE post(
    id_post int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    procedimiento   LONGTEXT   not null,
    link_video  varchar(100) null,
    id_comentario   int null,
    FOREIGN KEY (id_comentario) REFERENCES comentarios(id_comentario));

CREATE TABLE caracteristicas_usuario(
    preferencias  text     not null,
    seguidores  text    not null,
    seguidos  text    not null,
    id_post int  null,
    id_usuario_eco  int not null,
    id_guardado      int    null,
    FOREIGN KEY (id_post) REFERENCES post(id_post),
    FOREIGN KEY (id_guardado) REFERENCES guardado(id_guardado),
    FOREIGN KEY (id_usuario_eco) REFERENCES usuarios_eco(id_usuario_eco));

INSERT INTO clientes(nombre,apellido_paterno,apellido_materno,telefono,email)VALUES(
    'Andres','Masel','Calamaro','7775912409','andy@gmail.com'),
    ('Alejandro','Lora','Serna','7710927169','Alex@gmail.com'));

INSERT INTO usuarios_eco(nombre,apellido_paterno,apellido_materno,email,telefono,descripcion)VALUES(
    'Alejandro','Lora','Serna','Alex@gmail.com','7710927169','Musico ecologico');

INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('Edgar',MD5(concat('Edgar', 'kuorra_key')), 0, 1, 'Edgar', 'edgar@gmail.com','TIC:SI', MD5(concat('Edgar', 'kuorra_key', '2016/06/04')), 0),
('Abigail',MD5(concat('Abigail', 'kuorra_key')), 1, 1, 'Abigail', 'abita@gmail.com','TIC:SI', MD5(concat('Abigail', 'kuorra_key','2016/06/04')), 0);


SELECT * FROM users;
SELECT * FROM sessions;

CREATE USER 'eco_system'@'localhost' IDENTIFIED BY 'eco_system.2019';
GRANT ALL PRIVILEGES ON eco_system.* TO 'eco_system'@'localhost';
FLUSH PRIVILEGES;
