import web

db_host = 'localhost'
db_name = 'eco_system'
db_user = 'eco_system'
db_pw = 'eco_system.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )