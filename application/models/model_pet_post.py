import web
import config

db = config.db


def get_all_pet_post():
    try:
        return db.select('pet_post')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_pet_post(id_pet_post):
    try:
        return db.select('pet_post', where='id_pet_post=$id_pet_post', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_pet_post(id_pet_post):
    try:
        return db.delete('pet_post', where='id_pet_post=$id_pet_post', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_pet_post(titulo,descripcion,procedimiento,link_video,id_usuario_eco):
    try:
        return db.insert('pet_post',titulo=titulo,
descripcion=descripcion,
procedimiento=procedimiento,
link_video=link_video,
id_usuario_eco=id_usuario_eco)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_pet_post(id_pet_post,titulo,descripcion,procedimiento,link_video,id_usuario_eco):
    try:
        return db.update('pet_post',id_pet_post=id_pet_post,
titulo=titulo,
descripcion=descripcion,
procedimiento=procedimiento,
link_video=link_video,
id_usuario_eco=id_usuario_eco,
                  where='id_pet_post=$id_pet_post',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
