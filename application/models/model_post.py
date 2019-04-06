import web
import config

db = config.db


def get_all_post():
    try:
        return db.select('post')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_post(id_post):
    try:
        return db.select('post', where='id_post=$id_post', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_post(id_post):
    try:
        return db.delete('post', where='id_post=$id_post', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_post(procedimiento,link_video,id_comentario,titulo):
    try:
        return db.insert('post',procedimiento=procedimiento,
link_video=link_video,
id_comentario=id_comentario,
titulo=titulo)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_post(id_post,procedimiento,link_video,id_comentario,titulo):
    try:
        return db.update('post',id_post=id_post,
procedimiento=procedimiento,
link_video=link_video,
id_comentario=id_comentario,
titulo=titulo,
                  where='id_post=$id_post',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
