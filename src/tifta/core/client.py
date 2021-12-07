"""A module holding fundamental routines for the creation of an SFTP client."""

import paramiko


class _SFTPClient(object):
    """A class for setting up an SFTP client."""

    def __init__(self, hostname, **server_data):
        """Initialize the server by saving connection data."""
        self._hostname = hostname
        self._server_data = server_data

    def _start_ssh_client(self):
        """Start an SSH client."""
        self._ssh_client = paramiko.SSHClient()
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh_client.connect(self._hostname, **self._server_data)

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

    def _remove_file(self, remote_filepath):
        """Removes a file in the SFTP server."""
        self._start_ssh_and_sftp_client()
        self._sftp_client.remove(remote_filepath)
        self._close_sftp_and_ssh_client()


class TIFTAClient(_SFTPClient):
    """A secure class for setting up an SFTP client."""

    def __init__(self, hostname, **connect_data):
        """Initializes a client session."""
        super().__init__(hostname, **connect_data)

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

    def remove_file(self, remote_filepath):
        """Removes server file."""
        self._remove_file(remote_filepath)
