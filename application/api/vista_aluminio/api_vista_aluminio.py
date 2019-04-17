import web
import config
import json


class Api_vista_aluminio:
    def get(self, ):
        try:
            # http://0.0.0.0:8080/api_vista_aluminio?user_hash=12345&action=get
            if  is None:
                result = config.model.get_all_vista_aluminio()
                vista_aluminio_json = []
                for row in result:
                    tmp = dict(row)
                    vista_aluminio_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(vista_aluminio_json)
            else:
                # http://0.0.0.0:8080/api_vista_aluminio?user_hash=12345&action=get&=1
                result = config.model.get_vista_aluminio(int())
                vista_aluminio_json = []
                vista_aluminio_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(vista_aluminio_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            vista_aluminio_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(vista_aluminio_json)

# http://0.0.0.0:8080/api_vista_aluminio?user_hash=12345&action=put&=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, Titulo,descripcion,procedimiento,link_video,id_usuario_eco,categoria):
        try:
            config.model.insert_vista_aluminio(Titulo,descripcion,procedimiento,link_video,id_usuario_eco,categoria)
            vista_aluminio_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(vista_aluminio_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_vista_aluminio?user_hash=12345&action=delete&=1
    def delete(self, ):
        try:
            config.model.delete_vista_aluminio()
            vista_aluminio_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(vista_aluminio_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_vista_aluminio?user_hash=12345&action=update&=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, , Titulo,descripcion,procedimiento,link_video,id_usuario_eco,categoria):
        try:
            config.model.edit_vista_aluminio(id_post,Titulo,descripcion,procedimiento,link_video,id_usuario_eco,categoria)
            vista_aluminio_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(vista_aluminio_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            vista_aluminio_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(vista_aluminio_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_post=None,
            Titulo=None,
            descripcion=None,
            procedimiento=None,
            link_video=None,
            id_usuario_eco=None,
            categoria=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_post=user_data.id_post
            Titulo=user_data.Titulo
            descripcion=user_data.descripcion
            procedimiento=user_data.procedimiento
            link_video=user_data.link_video
            id_usuario_eco=user_data.id_usuario_eco
            categoria=user_data.categoria
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get()
                elif action == 'put':
                    return self.put(Titulo,descripcion,procedimiento,link_video,id_usuario_eco,categoria)
                elif action == 'delete':
                    return self.delete()
                elif action == 'update':
                    return self.update(, Titulo,descripcion,procedimiento,link_video,id_usuario_eco,categoria)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
