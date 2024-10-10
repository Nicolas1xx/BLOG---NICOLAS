ambiente = 'teste' 

if ambiente == 'teste':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'

if ambiente == 'producao':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'nicolasSenai.mysql.pythonanywhere-services.com'
    DB_USER = 'NicolasSenai'
    DB_PASSWORD = 'adm@123456'
    DB_NAME = 'NicolasSenai$Blog'

#CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'blog'

#SENHA DO ADM
MASTER_EMAIL = "nicolas@email"
MASTER_PASSWORD = "adm123"