import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_usuario_eco, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_usuario_eco) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_usuario_eco, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_usuario_eco) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_usuario_eco, **k):

    @staticmethod
    def POST_EDIT(id_usuario_eco, **k):
        
    '''

    def GET(self, id_usuario_eco, **k):
        message = None # Error message
        id_usuario_eco = config.check_secure_val(str(id_usuario_eco)) # HMAC id_usuario_eco validate
        result = config.model.get_usuarios_eco(int(id_usuario_eco)) # search for the id_usuario_eco
        result.id_usuario_eco = config.make_secure_val(str(result.id_usuario_eco)) # apply HMAC for id_usuario_eco
        return config.render.edit(result, message) # render usuarios_eco edit.html

    def POST(self, id_usuario_eco, **k):
        form = config.web.input()  # get form data
        form['id_usuario_eco'] = config.check_secure_val(str(form['id_usuario_eco'])) # HMAC id_usuario_eco validate
        # edit user with new data
        result = config.model.edit_usuarios_eco(
            form['id_usuario_eco'],form['nombre'],form['apellido_paterno'],form['apellido_materno'],form['email'],form['telefono'],form['descripcion'],
        )
        if result == None: # Error on udpate data
            id_usuario_eco = config.check_secure_val(str(id_usuario_eco)) # validate HMAC id_usuario_eco
            result = config.model.get_usuarios_eco(int(id_usuario_eco)) # search for id_usuario_eco data
            result.id_usuario_eco = config.make_secure_val(str(result.id_usuario_eco)) # apply HMAC to id_usuario_eco
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/usuarios_eco') # render usuarios_eco index.html
