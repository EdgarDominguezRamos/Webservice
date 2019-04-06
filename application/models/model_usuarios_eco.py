import web
import config

db = config.db


def get_all_usuarios_eco():
    try:
        return db.select('usuarios_eco')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_usuarios_eco(id_usuario_eco):
    try:
        return db.select('usuarios_eco', where='id_usuario_eco=$id_usuario_eco', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_usuarios_eco(id_usuario_eco):
    try:
        return db.delete('usuarios_eco', where='id_usuario_eco=$id_usuario_eco', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_usuarios_eco(nombre,apellido_paterno,apellido_materno,email,telefono,descripcion):
    try:
        return db.insert('usuarios_eco',nombre=nombre,
apellido_paterno=apellido_paterno,
apellido_materno=apellido_materno,
email=email,
telefono=telefono,
descripcion=descripcion)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_usuarios_eco(id_usuario_eco,nombre,apellido_paterno,apellido_materno,email,telefono,descripcion):
    try:
        return db.update('usuarios_eco',id_usuario_eco=id_usuario_eco,
nombre=nombre,
apellido_paterno=apellido_paterno,
apellido_materno=apellido_materno,
email=email,
telefono=telefono,
descripcion=descripcion,
                  where='id_usuario_eco=$id_usuario_eco',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
