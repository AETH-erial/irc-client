""" Simplified client for an IRC chat """
from irc_client.configuration.client_configuration import ClientConfiguration
from irc.client import ServerConnection


class IrcFunction:
    """ IRC chat client functionality """
    def __init__(self, connection: ServerConnection):
        if not isinstance(connection, ServerConnection):
            raise TypeError(f'connection should have been a ServerConnection but got a: {type(connection)}')
        self._server_conn = connection


class IrcClient(IrcFunction, ClientConfiguration):
    def __init__(self, conf_loc: str, connection: ServerConnection):
        super().__init__(conf_loc=conf_loc)
        super().__init__(connection=connection)


