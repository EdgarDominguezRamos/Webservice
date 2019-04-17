import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_carton_post):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_carton_post) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_carton_post):
    '''

    def GET(self, id_carton_post):
        id_carton_post = config.check_secure_val(str(id_carton_post)) # HMAC id_carton_post validate
        result = config.model.get_carton_post(id_carton_post) # search for the id_carton_post data
        return config.render.view(result) # render view.html with id_carton_post data
