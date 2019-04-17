import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_aluminio_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_aluminio_post) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_aluminio_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_aluminio_post) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html



    @staticmethod
    def GET_EDIT(id_aluminio_post, **k):
        message = None # Error message
        id_aluminio_post = config.check_secure_val(str(id_aluminio_post)) # HMAC id_aluminio_post validate
        result = config.model.get_aluminio_post(int(id_aluminio_post)) # search for the id_aluminio_post
        result.id_aluminio_post = config.make_secure_val(str(result.id_aluminio_post)) # apply HMAC for id_aluminio_post
        return config.render.edit(result, message) # render aluminio_post edit.html

    @staticmethod
    def POST_EDIT(id_aluminio_post, **k):
        form = config.web.input()  # get form data
        form['id_aluminio_post'] = config.check_secure_val(str(form['id_aluminio_post'])) # HMAC id_aluminio_post validate
        # edit user with new data
        result = config.model.edit_aluminio_post(
            form['id_aluminio_post'],form['titulo'],form['descripcion'],form['procedimiento'],form['link_video'],form['id_usuario_eco'],
        )
        if result == None: # Error on udpate data
            id_aluminio_post = config.check_secure_val(str(id_aluminio_post)) # validate HMAC id_aluminio_post
            result = config.model.get_aluminio_post(int(id_aluminio_post)) # search for id_aluminio_post data
            result.id_aluminio_post = config.make_secure_val(str(result.id_aluminio_post)) # apply HMAC to id_aluminio_post
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/aluminio_post') # render aluminio_post index.html
