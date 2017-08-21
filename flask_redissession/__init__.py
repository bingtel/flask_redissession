
__version__ = '0.3.1'

from .session import RedisSessionInterface


class Session(dict):
    def __init__(self, app=None):
        self.app = app
        if app is not NOne:
            self.init_app(app)

    def init_app(self, app):
        app.session_interface = self._session_interface(app)

    def _session_interface(self, app):
        config = app.config
        config.setdefault('SESSION_KEY_PREFIX', 'session:')
        config.setdefault('SESSION_REDIS', 'localhost:6379')
        config.setdefault('SESSION_PERMANENT', True)
        session_interface = RedisSessionInterface(
                config['SESSION_KEY_PREFIX'], config['SESSION_PERMANENT'])
        return session_interface

    

            
    