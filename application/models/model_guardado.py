import web
import config

db = config.db


def get_all_guardado():
    try:
        return db.select('guardado')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_guardado(id_guardado):
    try:
        return db.select('guardado', where='id_guardado=$id_guardado', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_guardado(id_guardado):
    try:
        return db.delete('guardado', where='id_guardado=$id_guardado', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_guardado(id_usuario_eco):
    try:
        return db.insert('guardado',id_usuario_eco=id_usuario_eco)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_guardado(id_guardado,id_usuario_eco):
    try:
        return db.update('guardado',id_guardado=id_guardado,
id_usuario_eco=id_usuario_eco,
                  where='id_guardado=$id_guardado',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
