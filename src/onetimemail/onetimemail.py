import os
import secrets
import click
import configparser
from pathlib import Path


DIR = os.path.join(os.path.expanduser('~'), '.onetimemail')
CONFIG = os.path.join(DIR, 'config.ini')


def _get(name):
    config = configparser.ConfigParser()
    config.read(CONFIG)
    if config.has_option('config', name):
        return config.get('config', name)
    else:
        if name == 'domain':
            set_domain('example.com')
            return 'example.com'
        elif name == 'length':
            set_length('16')
            return '16'


def _set(name, value):
    config = configparser.ConfigParser()
    config.read(CONFIG)
    if not config.has_section('config'):
        config.add_section('config')
    config.set('config', name, value)
    os.makedirs(DIR, exist_ok=True)
    with open(CONFIG, 'w') as configfile:
        config.write(configfile)


def get_domain():
    return _get('domain')


def get_length():
    return _get('length')


def set_domain(domain):
    _set('domain', domain)


def set_length(length):
    _set('length', length)


@click.command()
@click.option(
    '-d', '--domain',
    help='Set your own domain.'
)
@click.option(
    '-l', '--length',
    type=int,
    help='Set the length of the randomly generated string.'
)
def cli(domain, length):
    """
    One-time email address generator.
    """

    if length is None:
        # Read length from config file
        length = int(get_length())
    else:
        # Write length to config file
        set_length(str(length))

    username = secrets.token_hex(length)[0:length]

    if domain is None:
        # Read domain from config file
        domain = get_domain()
    else:
        # Write domain to config file
        set_domain(domain)

    click.echo('{}@{}'.format(username, domain))


if __name__ == '__main__':
    cli()
