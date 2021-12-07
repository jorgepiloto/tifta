"""A module holding default TIFTA paths."""

from pathlib import Path

_HOME_PATH = Path.home()
"""Home directory path of the client."""

_TIFTA_DIR_PATH = _HOME_PATH / ".tifta"
"""TIFTA directory path where all generated files are stored."""

_TIFTA_CONFIG_PATH = _TIFTA_DIR_PATH / "conf"
"""TIFTA directory path where configuration files are placed."""

_TIFTA_CLIENT_CONFIG_PATH = _TIFTA_CONFIG_PATH / "client.conf"
"""Path to TIFTA client configuration."""

_TIFTA_HOST_CONFIG_PATH = _TIFTA_CONFIG_PATH / "host.conf"
"""Path to TIFTA host configuration."""

_TIFTA_LOGS_PATH = _TIFTA_DIR_PATH / "logs"
"""TIFTA directory path where session logbooks are placed."""

_TIFTA_KEYS_PATH = _TIFTA_DIR_PATH / "keys"
"""TIFTA directory path where private and public keys are stored."""

_TIFTA_PRIVATE_KEY_PATH = _TIFTA_KEYS_PATH / "tifta_key"
"""Path to TIFTA generated private key. This file is encrypted with a passphrase."""

_TIFTA_PUBLIC_KEY_PATH = _TIFTA_KEYS_PATH / "tifta_key.pub"
"""Path to TIFTA generated public key."""

_TIFTA_DIRPATHS = (
    _TIFTA_DIR_PATH,
    _TIFTA_CONFIG_PATH,
    _TIFTA_LOGS_PATH,
    _TIFTA_KEYS_PATH,
)
"""A list holding all the critical TIFTA directory paths."""
