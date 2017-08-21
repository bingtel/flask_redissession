# -*- coding: utf-8 -*-

from flask.sessions import SessionInterface, SessionMixin
from werkzeug.datastructures import CallbackDict
from itsdangerous import Signer


class RedisSession(CallbackDict, SessionMixin):
    def __init__(self, initial=None, sid=None, permanent=None):
        def on_update(self):
            self.modified = True
        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid
        if permanent:
            self.permanent = permanent
        self.modified = False


class RedisSessionInterface(SessionInterface):
    session_class = RedisSession

    def __init__(self, session_key_prefix, redis, permanent)
    def _generate_sid(self):
        return str(uuid4())

    def _get_signer(self, app):
        if not app.secret_key:
            return None
        return Signer(app.secret_key, salt='flask_redissession',
                      key_derivation='hmac')

    def __getitem__(self, key):
        pass

    def __setitem__(self, key):
        pass