import configparser
import sys


CONFIG_FILE = 'fides.ini'


def generate_config_file():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    config['DEFAULT']['LicenseKey'] = '<ENTER your license key her>'
    config['SERVER']['Url'] = 'http://localhost'

    with open(CONFIG_FILE, 'w') as config_file:    # save
        config.write(config_file)


if len(sys.argv) < 1:
    print("Usage: ...")
elif sys.argv[1] == 'generate_config_file':
    generate_config_file()
