import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_usuario_eco, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_usuario_eco) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_usuario_eco, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_usuario_eco) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_usuario_eco, **k):

    @staticmethod
    def POST_DELETE(id_usuario_eco, **k):
    '''

    def GET(self, id_usuario_eco, **k):
        message = None # Error message
        id_usuario_eco = config.check_secure_val(str(id_usuario_eco)) # HMAC id_usuario_eco validate
        result = config.model.get_usuarios_eco(int(id_usuario_eco)) # search  id_usuario_eco
        result.id_usuario_eco = config.make_secure_val(str(result.id_usuario_eco)) # apply HMAC for id_usuario_eco
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_usuario_eco, **k):
        form = config.web.input() # get form data
        form['id_usuario_eco'] = config.check_secure_val(str(form['id_usuario_eco'])) # HMAC id_usuario_eco validate
        result = config.model.delete_usuarios_eco(form['id_usuario_eco']) # get usuarios_eco data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_usuario_eco = config.check_secure_val(str(id_usuario_eco))  # HMAC user validate
            id_usuario_eco = config.check_secure_val(str(id_usuario_eco))  # HMAC user validate
            result = config.model.get_usuarios_eco(int(id_usuario_eco)) # get id_usuario_eco data
            result.id_usuario_eco = config.make_secure_val(str(result.id_usuario_eco)) # apply HMAC to id_usuario_eco
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/usuarios_eco') # render usuarios_eco delete.html 
