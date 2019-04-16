import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_post) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_post, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_post) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_post, **k):

    @staticmethod
    def POST_DELETE(id_post, **k):
    '''

    def GET(self, id_post, **k):
        message = None # Error message
        id_post = config.check_secure_val(str(id_post)) # HMAC id_post validate
        result = config.model.get_post(int(id_post)) # search  id_post
        result.id_post = config.make_secure_val(str(result.id_post)) # apply HMAC for id_post
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_post, **k):
        form = config.web.input() # get form data
        form['id_post'] = config.check_secure_val(str(form['id_post'])) # HMAC id_post validate
        result = config.model.delete_post(form['id_post']) # get post data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_post = config.check_secure_val(str(id_post))  # HMAC user validate
            id_post = config.check_secure_val(str(id_post))  # HMAC user validate
            result = config.model.get_post(int(id_post)) # get id_post data
            result.id_post = config.make_secure_val(str(result.id_post)) # apply HMAC to id_post
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/post') # render post delete.html 
