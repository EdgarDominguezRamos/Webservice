import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, , **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE() # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, , **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE() # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(, **k):

    @staticmethod
    def POST_DELETE(, **k):
    '''

    def GET(self, , **k):
        message = None # Error message
         = config.check_secure_val(str()) # HMAC  validate
        result = config.model.get_vista_aluminio(int()) # search  
        result. = config.make_secure_val(str(result.)) # apply HMAC for 
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, , **k):
        form = config.web.input() # get form data
        form[''] = config.check_secure_val(str(form[''])) # HMAC  validate
        result = config.model.delete_vista_aluminio(form['']) # get vista_aluminio data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
             = config.check_secure_val(str())  # HMAC user validate
             = config.check_secure_val(str())  # HMAC user validate
            result = config.model.get_vista_aluminio(int()) # get  data
            result. = config.make_secure_val(str(result.)) # apply HMAC to 
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/vista_aluminio') # render vista_aluminio delete.html 
