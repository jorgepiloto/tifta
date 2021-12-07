"""
A module holding different routines for private and public keys generation.

The logic behind these routines relies on the paramiko library. You may also
generate a pair of SSH keys by using the `ssh-keygen` utility:


.. code-block:: bash

    ssh-keygen -q -t {ktype} -b {bits} -m PEM -f {filename} -N {passphrase}


.. note::

    The paramiko library seems to struggle when dealing with private and public
    keys, no matter if they ship or not with a passphrase. Please, keep track of
    official issue: https://github.com/paramiko/paramiko/issues/387
"""


from paramiko import DSSKey, ECDSAKey, RSAKey

from tifta.core.paths import _TIFTA_KEYS_PATH

_PARAMIKO_CIPHERS = {"dsa": DSSKey, "rsa": RSAKey, "ecdsa": ECDSAKey}
"""A dictionary relating cipher name with its paramiko class."""


def _generate_keys(
    cipher_name="rsa",
    key_filename="tifta_key",
    output_path=_TIFTA_KEYS_PATH,
    bits=2048,
    passphrase=None,
    comment=None,
):
    """Generates private and public keys using desired cipher"""

    # Check desired cipher is a valid one
    try:
        Cipher = _PARAMIKO_CIPHERS[cipher_name]
    except KeyError:
        raise ValueError(
            f"Cipher {cipher_name} is not a valid one. Supported ciphers: {list(_PARAMIKO_CIPHERS.keys())}"
        )

    # Build key filepath
    key_filepath = str(output_path / key_filename)

    # Generate private key
    pkey = Cipher.generate(bits)
    pkey.write_private_key_file(
        key_filepath, password=passphrase
    ) if passphrase is not None else pkey.write_private_key_file(key_filepath)

    # Generate associated public key
    pubkey = (
        Cipher(filename=key_filename, password=passphrase)
        if passphrase is not None
        else Cipher(filename=key_filepath)
    )

    with open(key_filepath + ".pub", "w") as pubkey_file:
        pubkey_file.write(f"{pubkey.get_name()} {pubkey.get_base64()}")
        if comment is not None:
            pubkey_file.write(f" {comment}")
