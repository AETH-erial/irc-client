""" Client Configuration class for the IRC client """
import os
import json
from irc_client.exceptions.exceptions import ConfigNotFound, InvalidConfigError
from irc_client.configuration.const import ValidConfFields


class ClientConfiguration: # pylint: disable=too-few-public-methods
    """ class to house client configuration settings """

    def __init__(self, conf_loc: str):
        """
        Init for ClientConfiguration class

        :type conf_loc: str
        :param conf_loc: the fp to the configuration location
        :raises ConfigNotFound: if the config doesn't exist at the specified location
        :raises InvalidConfigError: if the config cant be validated

        """
        conf = self.__read_config(loc=conf_loc)
        if self.__validate_fields(conf=conf) is True:
            self.__load_config(conf=conf)

    @staticmethod
    def __read_config(loc: str) -> dict:
        """
        load a configuration file

        :type loc: str
        :param loc: the path to the config file
        :returns: dictionary of the validated, loaded configuration
        :raises ConfigNotFound: if the config passed is rendered as invalid

        """
        if os.path.isfile(loc) is False:
            raise ConfigNotFound(f'could not locate a configuration at: {loc}')
        with open(loc, 'r', encoding='utf-8') as file:
            conf = json.load(fp=file)
        return conf

    @staticmethod
    def __validate_fields(conf: dict) -> bool:
        """
        validate config fields
        :type conf: dict
        :param conf: the configuration to validate
        :rtype: bool
        :returns: True if the config is good
        :raises InvalidConfigError: if the config is bad

        """
        if not isinstance(conf, dict):
            raise TypeError(f'conf should have been a dict but got a: {type(conf)}')
        for field in conf.keys():
            try:
                ValidConfFields(field)
            except ValueError as err:
                raise InvalidConfigError(f"field: {field} not in {ValidConfFields}") from err
        return True

    @classmethod
    def __load_config(cls, conf: dict) -> None:
        """
        Load the config into the classes attributes

        :type conf: dict
        :param conf: the config to load into the class
        :returns: None

        """
        for field, value in conf.items():
            setattr(cls, ValidConfFields(field).name, value)
