import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_carton_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_carton_post) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_carton_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_carton_post) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_carton_post, **k):

    @staticmethod
    def POST_EDIT(id_carton_post, **k):
        
    '''

    def GET(self, id_carton_post, **k):
        message = None # Error message
        id_carton_post = config.check_secure_val(str(id_carton_post)) # HMAC id_carton_post validate
        result = config.model.get_carton_post(int(id_carton_post)) # search for the id_carton_post
        result.id_carton_post = config.make_secure_val(str(result.id_carton_post)) # apply HMAC for id_carton_post
        return config.render.edit(result, message) # render carton_post edit.html

    def POST(self, id_carton_post, **k):
        form = config.web.input()  # get form data
        form['id_carton_post'] = config.check_secure_val(str(form['id_carton_post'])) # HMAC id_carton_post validate
        # edit user with new data
        result = config.model.edit_carton_post(
            form['id_carton_post'],form['titulo'],form['descripcion'],form['procedimiento'],form['link_video'],form['id_usuario_eco'],
        )
        if result == None: # Error on udpate data
            id_carton_post = config.check_secure_val(str(id_carton_post)) # validate HMAC id_carton_post
            result = config.model.get_carton_post(int(id_carton_post)) # search for id_carton_post data
            result.id_carton_post = config.make_secure_val(str(result.id_carton_post)) # apply HMAC to id_carton_post
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/carton_post') # render carton_post index.html
