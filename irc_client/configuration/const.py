""" Constant values for the libraries usage """
from enum import Enum


class ValidConfFields(Enum):
    """ Enum type for validating a config field """
    SERVER_NICKNAME = 'server nickname'
    PORT = 'port'
    SERVER_FQDN = 'server fqdn'
    SERVER_IP = 'server ip'
    CLIENT_NAME = 'client name'
