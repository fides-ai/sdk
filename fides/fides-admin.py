import configparser
import sys
import os


CONFIG_FILE = 'fides.ini'


def generate_config_file():
    config = configparser.ConfigParser()

    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)

    license_key = '<ENTER your license key here>'
    if len(sys.argv) > 2:
        license_key = sys.argv[2].split('=')[1]

    config['DEFAULT']['license_key'] = license_key
    config['DEFAULT']['url'] = 'http://localhost'

    with open(CONFIG_FILE, 'w') as config_file:    # save
        print("Generating {}".format(CONFIG_FILE))
        config.write(config_file)


def print_usage():
    print("Usage:")
    print("python fides-admin.py generate_config_file LicenseKey=...")


if len(sys.argv) < 2:
    print_usage()
elif sys.argv[1] == 'generate_config_file':
    generate_config_file()
else:
    print_usage()
