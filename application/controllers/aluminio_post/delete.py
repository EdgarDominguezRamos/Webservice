import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_aluminio_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_aluminio_post) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_aluminio_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_aluminio_post) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


    @staticmethod
    def GET_DELETE(id_aluminio_post, **k):
        message = None # Error message
        id_aluminio_post = config.check_secure_val(str(id_aluminio_post)) # HMAC id_aluminio_post validate
        result = config.model.get_aluminio_post(int(id_aluminio_post)) # search  id_aluminio_post
        result.id_aluminio_post = config.make_secure_val(str(result.id_aluminio_post)) # apply HMAC for id_aluminio_post
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_aluminio_post, **k):
        form = config.web.input() # get form data
        form['id_aluminio_post'] = config.check_secure_val(str(form['id_aluminio_post'])) # HMAC id_aluminio_post validate
        result = config.model.delete_aluminio_post(form['id_aluminio_post']) # get aluminio_post data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_aluminio_post = config.check_secure_val(str(id_aluminio_post))  # HMAC user validate
            id_aluminio_post = config.check_secure_val(str(id_aluminio_post))  # HMAC user validate
            result = config.model.get_aluminio_post(int(id_aluminio_post)) # get id_aluminio_post data
            result.id_aluminio_post = config.make_secure_val(str(result.id_aluminio_post)) # apply HMAC to id_aluminio_post
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/aluminio_post') # render aluminio_post delete.html 
