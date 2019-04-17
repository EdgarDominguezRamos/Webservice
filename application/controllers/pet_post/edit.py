import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_pet_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_pet_post) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_pet_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_pet_post) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_pet_post, **k):

    @staticmethod
    def POST_EDIT(id_pet_post, **k):
        
    '''

    def GET(self, id_pet_post, **k):
        message = None # Error message
        id_pet_post = config.check_secure_val(str(id_pet_post)) # HMAC id_pet_post validate
        result = config.model.get_pet_post(int(id_pet_post)) # search for the id_pet_post
        result.id_pet_post = config.make_secure_val(str(result.id_pet_post)) # apply HMAC for id_pet_post
        return config.render.edit(result, message) # render pet_post edit.html

    def POST(self, id_pet_post, **k):
        form = config.web.input()  # get form data
        form['id_pet_post'] = config.check_secure_val(str(form['id_pet_post'])) # HMAC id_pet_post validate
        # edit user with new data
        result = config.model.edit_pet_post(
            form['id_pet_post'],form['titulo'],form['descripcion'],form['procedimiento'],form['link_video'],form['id_usuario_eco'],
        )
        if result == None: # Error on udpate data
            id_pet_post = config.check_secure_val(str(id_pet_post)) # validate HMAC id_pet_post
            result = config.model.get_pet_post(int(id_pet_post)) # search for id_pet_post data
            result.id_pet_post = config.make_secure_val(str(result.id_pet_post)) # apply HMAC to id_pet_post
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/pet_post') # render pet_post index.html
