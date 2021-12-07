import click

from tifta.core.config import (
    _append_varname_and_value_to_config_file,
    _setup_clean_tifta_environment,
)
from tifta.core.paths import _TIFTA_CLIENT_CONFIG_PATH, _TIFTA_HOST_CONFIG_PATH


@click.group()
def main_cli():
    """The entry point for the TIFTA CONFIG tool"""
    ...


@main_cli.command()
def clean():
    """A command for cleaning and generating a fresh TIFTA environment."""
    _setup_clean_tifta_environment()


@main_cli.command()
@click.argument("varname", type=str)
@click.argument("value", type=str)
@click.option("--host_conf", default=_TIFTA_HOST_CONFIG_PATH, type=str)
def host(varname, value, host_conf):
    """Allows to configure TIFTA HOST file by adding new arguments and values."""
    _append_varname_and_value_to_config_file(varname, value, host_conf)


@main_cli.command()
@click.argument("varname", type=str)
@click.argument("value", type=str)
@click.option("--client_conf", default=_TIFTA_CLIENT_CONFIG_PATH, type=str)
def client(varname, value, client_conf):
    """Allows to configure TIFTA CLIENT file by adding new arguments and values."""
    _append_varname_and_value_to_config_file(varname, value, client_conf)


main_cli()
