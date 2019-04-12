import web
import config
import json


class Api_guardado:
    def get(self, id_guardado):
        try:
            # http://0.0.0.0:8080/api_guardado?user_hash=12345&action=get
            if id_guardado is None:
                result = config.model.get_all_guardado()
                guardado_json = []
                for row in result:
                    tmp = dict(row)
                    guardado_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(guardado_json)
            else:
                # http://0.0.0.0:8080/api_guardado?user_hash=12345&action=get&id_guardado=1
                result = config.model.get_guardado(int(id_guardado))
                guardado_json = []
                guardado_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(guardado_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            guardado_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(guardado_json)

# http://0.0.0.0:8080/api_guardado?user_hash=12345&action=put&id_guardado=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, id_usuario_eco):
        try:
            config.model.insert_guardado(id_usuario_eco)
            guardado_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(guardado_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_guardado?user_hash=12345&action=delete&id_guardado=1
    def delete(self, id_guardado):
        try:
            config.model.delete_guardado(id_guardado)
            guardado_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(guardado_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_guardado?user_hash=12345&action=update&id_guardado=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_guardado, id_usuario_eco):
        try:
            config.model.edit_guardado(id_guardado,id_usuario_eco)
            guardado_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(guardado_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            guardado_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(guardado_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_guardado=None,
            id_usuario_eco=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_guardado=user_data.id_guardado
            id_usuario_eco=user_data.id_usuario_eco
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_guardado)
                elif action == 'put':
                    return self.put(id_usuario_eco)
                elif action == 'delete':
                    return self.delete(id_guardado)
                elif action == 'update':
                    return self.update(id_guardado, id_usuario_eco)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
