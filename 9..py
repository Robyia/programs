"""9: Script to ping and check whether any given IPs are active, also whether given set of
software are installed in the existing system ( like java, kubectl, aws etc) """

sudo python36 -m pip install boto3  # Install boto3 for Python 3.6.
python -m pip show boto3            # Verify boto3 is installed for the current version of Python.
