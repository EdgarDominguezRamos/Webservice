import web
import config

db = config.db


def get_all_vista_aluminio():
    try:
        return db.select('vista_aluminio')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_vista_aluminio():
    try:
        return db.select('vista_aluminio', where='=$', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_vista_aluminio():
    try:
        return db.delete('vista_aluminio', where='=$', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_vista_aluminio(Titulo,descripcion,procedimiento,link_video,id_usuario_eco,categoria):
    try:
        return db.insert('vista_aluminio',Titulo=Titulo,
descripcion=descripcion,
procedimiento=procedimiento,
link_video=link_video,
id_usuario_eco=id_usuario_eco,
categoria=categoria)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_vista_aluminio(id_post,Titulo,descripcion,procedimiento,link_video,id_usuario_eco,categoria):
    try:
        return db.update('vista_aluminio',id_post=id_post,
Titulo=Titulo,
descripcion=descripcion,
procedimiento=procedimiento,
link_video=link_video,
id_usuario_eco=id_usuario_eco,
categoria=categoria,
                  where='=$',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
