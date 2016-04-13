import os
from accounts import accounts
from whitelist import whitelist

DEBUG=True

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'flswio')

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Name of the field used to store the owner of each document
AUTH_FIELD = 'user_id'


DOMAIN = {}

DOMAIN['accounts'] = accounts
DOMAIN['whitelist'] = whitelist
