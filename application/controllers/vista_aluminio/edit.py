import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, , **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT() # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, , **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT() # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


    @staticmethod
    def GET_EDIT(, **k):
        message = None # Error message
         = config.check_secure_val(str()) # HMAC  validate
        result = config.model.get_vista_aluminio(int()) # search for the 
        result. = config.make_secure_val(str(result.)) # apply HMAC for 
        return config.render.edit(result, message) # render vista_aluminio edit.html

    @staticmethod
    def POST_EDIT(, **k):
        form = config.web.input()  # get form data
        form[''] = config.check_secure_val(str(form[''])) # HMAC  validate
        # edit user with new data
        result = config.model.edit_vista_aluminio(
            form[''],form['Titulo'],form['descripcion'],form['procedimiento'],form['link_video'],form['id_usuario_eco'],form['categoria'],
        )
        if result == None: # Error on udpate data
             = config.check_secure_val(str()) # validate HMAC 
            result = config.model.get_vista_aluminio(int()) # search for  data
            result. = config.make_secure_val(str(result.)) # apply HMAC to 
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/vista_aluminio') # render vista_aluminio index.html
