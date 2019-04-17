import web
import config
import json


class Api_pet_post:
    def get(self, id_pet_post):
        try:
            # http://0.0.0.0:8080/api_pet_post?user_hash=12345&action=get
            if id_pet_post is None:
                result = config.model.get_all_pet_post()
                pet_post_json = []
                for row in result:
                    tmp = dict(row)
                    pet_post_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(pet_post_json)
            else:
                # http://0.0.0.0:8080/api_pet_post?user_hash=12345&action=get&id_pet_post=1
                result = config.model.get_pet_post(int(id_pet_post))
                pet_post_json = []
                pet_post_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(pet_post_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            pet_post_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(pet_post_json)

# http://0.0.0.0:8080/api_pet_post?user_hash=12345&action=put&id_pet_post=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, titulo,descripcion,procedimiento,link_video,id_usuario_eco):
        try:
            config.model.insert_pet_post(titulo,descripcion,procedimiento,link_video,id_usuario_eco)
            pet_post_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(pet_post_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_pet_post?user_hash=12345&action=delete&id_pet_post=1
    def delete(self, id_pet_post):
        try:
            config.model.delete_pet_post(id_pet_post)
            pet_post_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(pet_post_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_pet_post?user_hash=12345&action=update&id_pet_post=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_pet_post, titulo,descripcion,procedimiento,link_video,id_usuario_eco):
        try:
            config.model.edit_pet_post(id_pet_post,titulo,descripcion,procedimiento,link_video,id_usuario_eco)
            pet_post_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(pet_post_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            pet_post_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(pet_post_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_pet_post=None,
            titulo=None,
            descripcion=None,
            procedimiento=None,
            link_video=None,
            id_usuario_eco=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_pet_post=user_data.id_pet_post
            titulo=user_data.titulo
            descripcion=user_data.descripcion
            procedimiento=user_data.procedimiento
            link_video=user_data.link_video
            id_usuario_eco=user_data.id_usuario_eco
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_pet_post)
                elif action == 'put':
                    return self.put(titulo,descripcion,procedimiento,link_video,id_usuario_eco)
                elif action == 'delete':
                    return self.delete(id_pet_post)
                elif action == 'update':
                    return self.update(id_pet_post, titulo,descripcion,procedimiento,link_video,id_usuario_eco)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
