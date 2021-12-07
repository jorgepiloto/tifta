"""A module providing TIFTA utilities for writing and reading config files."""

import json
import os
from getpass import getuser

from tifta.core.keygen import _generate_keys
from tifta.core.paths import (
    _TIFTA_CLIENT_CONFIG_PATH,
    _TIFTA_DIRPATHS,
    _TIFTA_HOST_CONFIG_PATH,
)

_DEFAULT_CLIENT_CONFIG_DATA = dict(
    hostname="127.0.0.1", username=str(getuser()), port=22
)
_DEFAULT_HOST_CONFIG_DATA = dict(sftp_dirpath="sftp_playground")
_DEFAULT_TIFTA_CONFIG_DATA = (_DEFAULT_CLIENT_CONFIG_DATA, _DEFAULT_HOST_CONFIG_DATA)
_TIFTA_CONFIG_FILES = (_TIFTA_CLIENT_CONFIG_PATH, _TIFTA_HOST_CONFIG_PATH)


def _setup_clean_tifta_environment():
    """Generates default TIFTA configuration files."""

    # Create each fundamental directory if required
    for dirpath in _TIFTA_DIRPATHS:
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

    # Generate private and public key
    _generate_keys()

    # Dump client and host configuration
    for config_data, file_path in zip(_DEFAULT_TIFTA_CONFIG_DATA, _TIFTA_CONFIG_FILES):
        with open(file_path, "w") as config_file:
            json.dump(config_data, config_file, indent=2, sort_keys=True)


def _append_varname_and_value_to_config_file(varname, value, conf_filepath):
    """
    Appends varname to desired TIFTA host or client config file.

    Notes
    -----
    Because TIFTA config files are stored as JSON, the best way to add data is
    to load the content of this files into a Python dictionary and then
    overwrite the whole file again.
    """

    # Read the JSON config file
    with open(conf_filepath, "r") as conf_file:
        config_data = dict(json.load(conf_file))

    # Append the new varname and value
    config_data[varname] = value

    # Dump all the content in a new fresh-clean config file
    with open(conf_filepath, "w") as conf_file:
        json.dump(config_data, conf_file, indent=2, sort_keys=True)


def _read_tifta_client_config_file(client_config_filepath):
    """Parses the TIFTA client configuration file."""

    # Read the client config file
    with open(client_config_filepath, "r") as client_conf_file:
        config_data = dict(json.load(client_conf_file))

        # Retrieve the 'hostname' and the rest of the parameters
        try:
            hostname = config_data.pop("hostname")
            return hostname, config_data
        except KeyError:
            raise ValueError(f"Key 'hostname' not found in {client_config_filepath}")


def _read_tifta_host_config_file():
    """Parses the TIFTA client configuration file."""

    # Read the client config file
    with open(_TIFTA_HOST_CONFIG_PATH, "r") as host_conf_file:
        config_data = dict(json.load(host_conf_file))

        # Retrieve the 'sftp_dirpath' and the rest of the parameters
        try:
            sftp_dirpath = config_data.pop("sftp_dirpath")
            return sftp_dirpath, config_data
        except KeyError:
            raise ValueError(f"Key 'sftp_dir' not found in {_TIFTA_HOST_CONFIG_PATH}")
