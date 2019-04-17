# Author : Salvador Hernandez Mendoza
# Email  : salvadorhm@gmail.com
# Twitter: @salvadorhm
import web
import config


#activate ssl certificate
ssl = False

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    '/users', 'application.controllers.users.index.Index',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/usuarios_eco', 'application.controllers.usuarios_eco.index.Index',
    '/usuarios_eco/view/(.+)', 'application.controllers.usuarios_eco.view.View',
    '/usuarios_eco/edit/(.+)', 'application.controllers.usuarios_eco.edit.Edit',
    '/usuarios_eco/delete/(.+)', 'application.controllers.usuarios_eco.delete.Delete',
    '/usuarios_eco/insert', 'application.controllers.usuarios_eco.insert.Insert',
    '/post', 'application.controllers.post.index.Index',
    '/post/view/(.+)', 'application.controllers.post.view.View',
    '/post/edit/(.+)', 'application.controllers.post.edit.Edit',
    '/post/delete/(.+)', 'application.controllers.post.delete.Delete',
    '/post/insert', 'application.controllers.post.insert.Insert',
    '/guardado', 'application.controllers.guardado.index.Index',
    '/guardado/view/(.+)', 'application.controllers.guardado.view.View',
    '/guardado/edit/(.+)', 'application.controllers.guardado.edit.Edit',
    '/guardado/delete/(.+)', 'application.controllers.guardado.delete.Delete',
    '/guardado/insert', 'application.controllers.guardado.insert.Insert',
    '/aluminio_post', 'application.controllers.aluminio_post.index.Index',
    '/aluminio_post/view/(.+)', 'application.controllers.aluminio_post.view.View',
    '/aluminio_post/edit/(.+)', 'application.controllers.aluminio_post.edit.Edit',
    '/aluminio_post/delete/(.+)', 'application.controllers.aluminio_post.delete.Delete',
    '/aluminio_post/insert', 'application.controllers.aluminio_post.insert.Insert',
    '/carton_post', 'application.controllers.carton_post.index.Index',
    '/carton_post/view/(.+)', 'application.controllers.carton_post.view.View',
    '/carton_post/edit/(.+)', 'application.controllers.carton_post.edit.Edit',
    '/carton_post/delete/(.+)', 'application.controllers.carton_post.delete.Delete',
    '/carton_post/insert', 'application.controllers.carton_post.insert.Insert',
    '/pet_post', 'application.controllers.pet_post.index.Index',
    '/pet_post/view/(.+)', 'application.controllers.pet_post.view.View',
    '/pet_post/edit/(.+)', 'application.controllers.pet_post.edit.Edit',
    '/pet_post/delete/(.+)', 'application.controllers.pet_post.delete.Delete',
    '/pet_post/insert', 'application.controllers.pet_post.insert.Insert',
    '/comentarios', 'application.controllers.comentarios.index.Index',
    '/comentarios/view/(.+)', 'application.controllers.comentarios.view.View',
    '/comentarios/edit/(.+)', 'application.controllers.comentarios.edit.Edit',
    '/comentarios/delete/(.+)', 'application.controllers.comentarios.delete.Delete',
    '/comentarios/insert', 'application.controllers.comentarios.insert.Insert',

    '/api_post/?', 'application.api.post.api_post.Api_post',
    '/api_usuarios_eco/?', 'application.api.usuarios_eco.api_usuarios_eco.Api_usuarios_eco',
)

app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'kuorra'
    web.config.session_parameters['timeout'] = 10
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


def InternalError(): 
    raise config.web.seeother('/')


def NotFound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = True # hide db transactions
    web.config.debug = True # hide debug print
    web.config.db_printing = True # hide db transactions
    # app.internalerror = InternalError
    app.notfound = NotFound
    app.run()
