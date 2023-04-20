""" Exceptions for IRC client errors """


class ConfigNotFound(Exception):
    """ Exception type for an unfound configuration """
    pass # pylint: disable=unnecessary-pass


class InvalidConfigError(Exception):
    """ Exception type for an incorrect configuration """
    pass # pylint: disable=unnecessary-pass
