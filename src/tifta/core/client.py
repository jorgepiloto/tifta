"""A module holding fundamental routines for the creation of an SFTP client."""

import paramiko


class _SFTPClient(object):
    """A class for setting up an SFTP client."""

    def __init__(self, user, host, password, passphrase, key_path, port):
        """Initialize the server by saving connection data."""
        self._server_data = dict(
            hostname=host,
            port=port,
            username=user,
            password=password,
            key_filename=str(key_path),
            passphrase=passphrase,
        )

    def _start_ssh_client(self):
        """Start an SSH client."""
        self._ssh_client = paramiko.SSHClient()
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh_client.connect(**self._server_data)

    def _start_sftp_client(self):
        """Start an SFTP session."""
        self._sftp_client = self._ssh_client.open_sftp()

    def _start_ssh_and_sftp_client(self):
        """Start both SSH and SFTP clients."""
        self._start_ssh_client()
        self._start_sftp_client()

    def _close_ssh_client(self):
        """Close the SHH client."""
        self._ssh_client.close()

    def _close_sftp_client(self):
        """Close the SFTP client."""
        self._sftp_client.close()

    def _close_sftp_and_ssh_client(self):
        """Close the SFTP and SSH clients in this order."""
        self._close_sftp_client()
        self._close_ssh_client()

    def _upload_file(self, local_filepath, remote_filepath):
        """Uploads a file to the SFTP server."""
        self._start_ssh_and_sftp_client()
        self._sftp_client.put(local_filepath, remote_filepath)
        self._close_sftp_and_ssh_client()

    def _download_file(self, remote_filepath, local_filepath):
        """Download a file from the SFTP server."""
        self._start_ssh_and_sftp_client()
        self._sftp_client.get(remote_filepath, local_filepath)
        self._close_sftp_and_ssh_client()

    def _delete_file(self, remote_filepath):
        """Removes a file in the SFTP server."""
        self._start_ssh_and_sftp_client()
        self._sftp_client.remove(remote_filepath)
        self._close_sftp_and_ssh_client()


class TIFTAClient(_SFTPClient):
    """A secure class for setting up an SFTP client."""

    def __init__(
        self,
        user,
        host,
        password,
        passphrase,
        key_path,
        port,
    ):
        """Initializes a client session."""
        super().__init__(user, host, password, passphrase, key_path, port)

    @property
    def host(self):
        """IP address of the SFTP host."""
        return self._server_data["hostname"]

    @property
    def port(self):
        """The port being used for the connection."""
        return self._server_data["port"]

    @property
    def username(self):
        """The username for logging in the host machine."""
        return self._server_data["username"]

    def upload_file(self, local_filepath, remote_filepath):
        """Uploads local file to server."""
        self._upload_file(local_filepath, remote_filepath)

    def download_file(self, remote_filepath, local_filepath):
        """Donwload remote server file to local machine."""
        self._download_file(remote_filepath, local_filepath)

    def delete_file(self, remote_filepath):
        """Removes server file."""
        self._delete_file(remote_filepath)
