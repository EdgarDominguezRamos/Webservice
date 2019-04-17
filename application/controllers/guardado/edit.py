import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_guardado, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_guardado) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_guardado, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_guardado) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


    @staticmethod
    def GET_EDIT(id_guardado, **k):
        message = None # Error message
        id_guardado = config.check_secure_val(str(id_guardado)) # HMAC id_guardado validate
        result = config.model.get_guardado(int(id_guardado)) # search for the id_guardado
        result.id_guardado = config.make_secure_val(str(result.id_guardado)) # apply HMAC for id_guardado
        return config.render.edit(result, message) # render guardado edit.html

    @staticmethod
    def POST_EDIT(id_guardado, **k):
        form = config.web.input()  # get form data
        form['id_guardado'] = config.check_secure_val(str(form['id_guardado'])) # HMAC id_guardado validate
        # edit user with new data
        result = config.model.edit_guardado(
            form['id_guardado'],form['id_usuario_eco'],form['id_post'],form['categoria'],
        )
        if result == None: # Error on udpate data
            id_guardado = config.check_secure_val(str(id_guardado)) # validate HMAC id_guardado
            result = config.model.get_guardado(int(id_guardado)) # search for id_guardado data
            result.id_guardado = config.make_secure_val(str(result.id_guardado)) # apply HMAC to id_guardado
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/guardado') # render guardado index.html
