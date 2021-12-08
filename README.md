# TIFTA: Tiny Interactive File Transfer Application

This repository holds all the source code, tests and documentation of the TIFTA
software. The main goals of this program are:

 * Ensure a safe and secure connection via SSH.
 * Take advantage of SSH to establish an SFTP secure channel.
 * Allow users to upload, download and remove files from remote server.

The TIFTA software is nuder heavy development and ships in the form of a command
line application. No graphical user interface is provided yet.

## How to install

### For users

If you would like to install TIFTA software, start by creating a new Python
environment and activate it. This is a good practice so you do no break your
system's Python installation:

```
python -m venv -venv && source .venv/bin/activate
```

Make sure you upgrade to the latest `pip` version by running:

```
python -m pip install -U pip
```

Finally, you can install TIFTA by running the following:

```
python -m pip install git+https://github.com/jorgepiloto/tifta.git
```

Now you should be able to run TIFTA in any working directory of your system as
long as your new Python environment is active. Try:

```
tifta --help
```

Finally, generate a new fresh TIFTA configuration by running:

```
tifta config clean
```


### For developers

Start by cloning the repository within your local machine. Installation process
only differs when installing the package, as you need now to pass the
`--editable` flag:

```
python -m pip install -e /path/to/tifta/cloned/repo
```


## How to use

Make sure that your client is properly configured and points to the right
server. You can see tifta client configuration by running:

```
cat ~/.tifta/conf/client.conf
```

Add or modify any existing varname or value using:

```
tifta config client varname "valuename"
```

as an example:

```
tifta config client hostname "192.168.X.X" # For local networks (usually).
tifta config client username "runner" # For GitHub CI virtual machines.
```

**Do not store server's password in your config files: TIFTA will ask you to
input your password if required at any time!**

When operating files within a server, all paths are assumed to be relative to
server's `home/` directory. Furthermore, **you need to specity the final name of
the uploaded/downloaded/removed/ files.**. Examples:

```
tifta upload path/to/local/file.txt path/to/remote/uploaded_file.txt # Uploads file to server
tifta download path/to/remote/file.txt path/to/remote/downloaded_file.txt # Downloads file from server
tifta remove path/to/remote/file.txt # Removes file from server
```

TIFTA CLI is properly documented, so you can always run:

```
tifta upload --help
tifta download --help
tifta remove --help
```

in case you need more help.
