import web
import config
import json


class Api_usuarios_eco:
    def get(self, id_usuario_eco):
        try:
            # http://0.0.0.0:8080/api_usuarios_eco?user_hash=12345&action=get
            if id_usuario_eco is None:
                result = config.model.get_all_usuarios_eco()
                usuarios_eco_json = []
                for row in result:
                    tmp = dict(row)
                    usuarios_eco_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(usuarios_eco_json)
            else:
                # http://0.0.0.0:8080/api_usuarios_eco?user_hash=12345&action=get&id_usuario_eco=1
                result = config.model.get_usuarios_eco(int(id_usuario_eco))
                usuarios_eco_json = []
                usuarios_eco_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(usuarios_eco_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuarios_eco_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_eco_json)

# http://0.0.0.0:8080/api_usuarios_eco?user_hash=12345&action=put&id_usuario_eco=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,descripcion,imagen):
        try:
            config.model.insert_usuarios_eco(nombre,descripcion,imagen)
            usuarios_eco_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_eco_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuarios_eco?user_hash=12345&action=delete&id_usuario_eco=1
    def delete(self, id_usuario_eco):
        try:
            config.model.delete_usuarios_eco(id_usuario_eco)
            usuarios_eco_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_eco_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuarios_eco?user_hash=12345&action=update&id_usuario_eco=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_usuario_eco, nombre,descripcion,imagen):
        try:
            config.model.edit_usuarios_eco(id_usuario_eco,nombre,descripcion,imagen)
            usuarios_eco_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_eco_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuarios_eco_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_eco_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_usuario_eco=None,
            nombre=None,
            descripcion=None,
            imagen=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_usuario_eco=user_data.id_usuario_eco
            nombre=user_data.nombre
            descripcion=user_data.descripcion
            imagen=user_data.imagen
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_usuario_eco)
                elif action == 'put':
                    return self.put(nombre,descripcion,imagen)
                elif action == 'delete':
                    return self.delete(id_usuario_eco)
                elif action == 'update':
                    return self.update(id_usuario_eco, nombre,descripcion,imagen)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
