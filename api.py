from eve import Eve
from eve.auth import BasicAuth
from flask import current_app as app
import sys,logging
from werkzeug.security import  generate_password_hash,check_password_hash
from pprint import pformat

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))
logger.setLevel(logging.DEBUG)

class RolesAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        accounts = app.data.driver.db['accounts']
        lookup = {'username': username}
        account = accounts.find_one(lookup)
        logger.debug(pformat([ username, password]))
        if resource == 'accounts' and method == 'POST':
            if not account:
                logger.debug("new user creation, no credentials checked")
                return True

        account = accounts.find_one(lookup)
        if not account:
            logger.debug("Account doesn't exist")
            return False

        if len(allowed_roles) and not account['role'] in allowed_roles:
            logger.debug("User does not have the required role")
            logger.debug(pformat(allowed_roles))
            logger.debug(pformat(account))
            return False

        if not check_password_hash(account['password'], password):
            logger.debug("Password failed hash function check")
            return False

        return True

def accounts_pre_insert(items):
    logger.debug("pre insert hook for accounts fired")
    for item in items:
        logger.debug("hashing password for " + pformat(item))
        item['password'] = generate_password_hash(item['password'])

if __name__ == '__main__':
    logger.debug("foo")
    logger.warning("something")
    logger.error("foobar")
    logger.info("starting")
    app = Eve(auth=RolesAuth)
    app.on_insert_accounts += accounts_pre_insert
    app.run()
