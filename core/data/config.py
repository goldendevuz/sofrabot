import os
import hashlib
from environs import Env

#todo:Open environs kutubxonasi orqali env faylidagi malumotlarni olamiz
env = Env()

IS_PROD = env.bool('IS_PROD')
# .env file ni core/data ichida ochamiz
if IS_PROD and not os.path.exists('core/data/.env'):
    print('.env fayli topilmadi!')
    print('.env.example faylidan nusxa ko\'chirib shablonni o\'zizga moslang.')
    exit(1)
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMIN_ID_LIST = env.str("ADMIN_ID_LIST").split(',')
ADMIN_ID_LIST = [int(admin_id) for admin_id in ADMIN_ID_LIST]
ADMINS = ADMIN_ID_LIST
WEBHOOK_DOMAIN = env.str('WEBHOOK_DOMAIN')
SECRET_KEY = env.str('SECRET_KEY')
BASE_URL = env.str('BASE_URL')
DEBUG = env.bool('DEBUG')

# webhook url yasash uchun noyob path yaratamiz
# WEBHOOK_PATH = "webhook/" 
# yoki
WEBHOOK_PATH = hashlib.md5(BOT_TOKEN.encode()).hexdigest()
WEBHOOK_URL = f"{WEBHOOK_DOMAIN}/api/webhook/{WEBHOOK_PATH}"