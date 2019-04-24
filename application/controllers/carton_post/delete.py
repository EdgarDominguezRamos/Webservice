import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_carton_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_carton_post) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_carton_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_carton_post) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_carton_post, **k):

    @staticmethod
    def POST_DELETE(id_carton_post, **k):
    '''

    def GET(self, id_carton_post, **k):
        message = None # Error message
        id_carton_post = config.check_secure_val(str(id_carton_post)) # HMAC id_carton_post validate
        result = config.model.get_carton_post(int(id_carton_post)) # search  id_carton_post
        result.id_carton_post = config.make_secure_val(str(result.id_carton_post)) # apply HMAC for id_carton_post
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_carton_post, **k):
        form = config.web.input() # get form data
        form['id_carton_post'] = config.check_secure_val(str(form['id_carton_post'])) # HMAC id_carton_post validate
        result = config.model.delete_carton_post(form['id_carton_post']) # get carton_post data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_carton_post = config.check_secure_val(str(id_carton_post))  # HMAC user validate
            id_carton_post = config.check_secure_val(str(id_carton_post))  # HMAC user validate
            result = config.model.get_carton_post(int(id_carton_post)) # get id_carton_post data
            result.id_carton_post = config.make_secure_val(str(result.id_carton_post)) # apply HMAC to id_carton_post
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/carton_post') # render carton_post delete.html 
