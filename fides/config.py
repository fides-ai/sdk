import os
import pkg_resources


DEFAULT_PROPERTIES_FILE_NAME = 'fides.ini'
ENV_FIDES_PROPERTIES_FILE = 'FIDES_PROPERTIES_FILE'


class Config(object):

    @classmethod
    def get_property(cls, key, default=None):
        properties = cls.get_properties()
        value = properties[key] if key in properties else default
        return value

    @classmethod
    def get_properties(cls):
        resource_package = __name__  # Could be any module/package name
        properties_file_name = os.getenv(ENV_FIDES_PROPERTIES_FILE, DEFAULT_PROPERTIES_FILE_NAME)
        resource_path = properties_file_name
        properties = pkg_resources.resource_string(resource_package, resource_path)
        return properties
