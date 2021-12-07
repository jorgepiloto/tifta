import click

from tifta.core.client import TIFTAClient
from tifta.core.config import _read_tifta_client_config_file
from tifta.core.paths import _TIFTA_CLIENT_CONFIG_PATH


@click.group()
def main():
    """The entry point for the TIFTA CLIENT tool"""
    ...


@main.command()
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


@main.command()
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


@main.command()
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
