""" Simplified client for an IRC chat """
from irc.client import ServerConnection
from irc_client.configuration.client_configuration import ClientConfiguration


class IrcFunction: # pylint: disable=too-few-public-methods
    """ IRC chat client functionality """
    def __init__(self, connection: ServerConnection):
        if not isinstance(connection, ServerConnection):
            raise TypeError(f'connection should have been a ServerConnection but got a: {type(connection)}')
        self._server_conn = connection


class IrcClient(IrcFunction, ClientConfiguration):
    """ IRC client class with inherited attributes from config and IrcFunction """
    def __init__(self, conf_loc: str, connection: ServerConnection):
        super().__init__(conf_loc)
        super().__init__(connection)
