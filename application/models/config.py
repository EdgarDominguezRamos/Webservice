import web

db_host = 'etdq12exrvdjisg6.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'n5lawo9lbim6y860'
db_user = 'fisps63fjpzkn036'
db_pw = 'hzusc8hjw9uqw40o'


db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )