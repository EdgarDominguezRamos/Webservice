import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_guardado, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_guardado) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_guardado, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_guardado) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

   

    @staticmethod
    def GET(self, id_guardado, **k):
        message = None # Error message
        id_guardado = config.check_secure_val(str(id_guardado)) # HMAC id_guardado validate
        result = config.model.get_guardado(int(id_guardado)) # search  id_guardado
        result.id_guardado = config.make_secure_val(str(result.id_guardado)) # apply HMAC for id_guardado
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_guardado, **k):
        form = config.web.input() # get form data
        form['id_guardado'] = config.check_secure_val(str(form['id_guardado'])) # HMAC id_guardado validate
        result = config.model.delete_guardado(form['id_guardado']) # get guardado data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_guardado = config.check_secure_val(str(id_guardado))  # HMAC user validate
            id_guardado = config.check_secure_val(str(id_guardado))  # HMAC user validate
            result = config.model.get_guardado(int(id_guardado)) # get id_guardado data
            result.id_guardado = config.make_secure_val(str(result.id_guardado)) # apply HMAC to id_guardado
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/guardado') # render guardado delete.html 
