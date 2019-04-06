import web
import config
import json


class Api_post:
    def get(self, id_post):
        try:
            # http://0.0.0.0:8080/api_post?user_hash=12345&action=get
            if id_post is None:
                result = config.model.get_all_post()
                post_json = []
                for row in result:
                    tmp = dict(row)
                    post_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(post_json)
            else:
                # http://0.0.0.0:8080/api_post?user_hash=12345&action=get&id_post=1
                result = config.model.get_post(int(id_post))
                post_json = []
                post_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(post_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            post_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(post_json)

# http://0.0.0.0:8080/api_post?user_hash=12345&action=put&id_post=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, procedimiento,link_video,id_comentario,titulo):
        try:
            config.model.insert_post(procedimiento,link_video,id_comentario,titulo)
            post_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(post_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_post?user_hash=12345&action=delete&id_post=1
    def delete(self, id_post):
        try:
            config.model.delete_post(id_post)
            post_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(post_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_post?user_hash=12345&action=update&id_post=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_post, procedimiento,link_video,id_comentario,titulo):
        try:
            config.model.edit_post(id_post,procedimiento,link_video,id_comentario,titulo)
            post_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(post_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            post_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(post_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_post=None,
            procedimiento=None,
            link_video=None,
            id_comentario=None,
            titulo=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_post=user_data.id_post
            procedimiento=user_data.procedimiento
            link_video=user_data.link_video
            id_comentario=user_data.id_comentario
            titulo=user_data.titulo
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_post)
                elif action == 'put':
                    return self.put(procedimiento,link_video,id_comentario,titulo)
                elif action == 'delete':
                    return self.delete(id_post)
                elif action == 'update':
                    return self.update(id_post, procedimiento,link_video,id_comentario,titulo)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
