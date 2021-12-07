"""Holds the TIFTA command line interface fundamental logic."""

import click

from tifta.core.client import TIFTAClient
from tifta.core.config import (
    _append_varname_and_value_to_config_file,
    _read_tifta_client_config_file,
    _setup_clean_tifta_environment,
)
from tifta.core.paths import _TIFTA_CLIENT_CONFIG_PATH, _TIFTA_HOST_CONFIG_PATH


@click.group()
def tifta_main():
    """TIFTA: Tiny Interactive File Transfer Application."""
    pass


@tifta_main.command()
@click.argument("local_filepath", type=str)
@click.argument("remote_filepath", type=str)
@click.option("--client_conf", default=_TIFTA_CLIENT_CONFIG_PATH, type=str)
@click.password_option()
def upload(local_filepath, remote_filepath, client_conf, password):
    """Uploads local file to server."""

    # Read data from client configuration file and append password
    hostname, server_data = _read_tifta_client_config_file(client_conf)
    server_data["password"] = password

    # Establish connection and upload the file
    client = TIFTAClient(hostname, **server_data)
    client.upload_file(local_filepath, remote_filepath)


@tifta_main.command()
@click.argument("remote_filepath", type=str)
@click.argument("local_filepath", type=str)
@click.option("--client_conf", default=_TIFTA_CLIENT_CONFIG_PATH, type=str)
@click.password_option()
def download(remote_filepath, local_filepath, client_conf, password):
    """Downloads file from server."""

    # Read data from client configuration file and append password
    hostname, server_data = _read_tifta_client_config_file(client_conf)
    server_data["password"] = password

    # Establish connection and download the file
    client = TIFTAClient(hostname, **server_data)
    client.download_file(remote_filepath, local_filepath)


@tifta_main.command()
@click.argument("remote_filepath", type=str)
@click.option("--client_conf", default=_TIFTA_CLIENT_CONFIG_PATH, type=str)
@click.password_option()
def remove(remote_filepath, client_conf, password):
    """Removes file from server."""

    # Read data from client configuration file and append password
    hostname, server_data = _read_tifta_client_config_file(client_conf)
    server_data["password"] = password

    # Establish connection and remove the file
    client = TIFTAClient(hostname, **server_data)
    client.remove_file(remote_filepath)


@tifta_main.group()
def config():
    """Easily manipulate TIFTA configuration files."""
    pass


@config.command()
def clean():
    """A command for cleaning and generating a fresh TIFTA environment."""
    _setup_clean_tifta_environment()


@config.command()
@click.argument("varname", type=str)
@click.argument("value", type=str)
@click.option("--host_conf", default=_TIFTA_HOST_CONFIG_PATH, type=str)
def host(varname, value, host_conf):
    """Allows to configure TIFTA HOST file by adding new arguments and values."""
    _append_varname_and_value_to_config_file(varname, value, host_conf)


@config.command()
@click.argument("varname", type=str)
@click.argument("value", type=str)
@click.option("--client_conf", default=_TIFTA_CLIENT_CONFIG_PATH, type=str)
def client(varname, value, client_conf):
    """Allows to configure TIFTA CLIENT file by adding new arguments and values."""
    _append_varname_and_value_to_config_file(varname, value, client_conf)
