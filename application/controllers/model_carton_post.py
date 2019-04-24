import web
import config

db = config.db


def get_all_carton_post():
    try:
        return db.select('carton_post')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_carton_post(id_carton_post):
    try:
        return db.select('carton_post', where='id_carton_post=$id_carton_post', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_carton_post(id_carton_post):
    try:
        return db.delete('carton_post', where='id_carton_post=$id_carton_post', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_carton_post(titulo,descripcion,procedimiento,link_video,id_usuario_eco):
    try:
        return db.insert('carton_post',titulo=titulo,
descripcion=descripcion,
procedimiento=procedimiento,
link_video=link_video,
id_usuario_eco=id_usuario_eco)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_carton_post(id_carton_post,titulo,descripcion,procedimiento,link_video,id_usuario_eco):
    try:
        return db.update('carton_post',id_carton_post=id_carton_post,
titulo=titulo,
descripcion=descripcion,
procedimiento=procedimiento,
link_video=link_video,
id_usuario_eco=id_usuario_eco,
                  where='id_carton_post=$id_carton_post',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
