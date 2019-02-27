import subprocess
import sys


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


def installRequired():
    '''flask
    flask-wtf
    flask-login
    flask-sqlalchemy
    flask-migrate
    pipenv'''
    install('flask')
    install('flask-wtf')
    install('flask-login')
    install('flask-sqlalchemy')
    install('flask-migrate')
    install('pipenv')


if __name__ == "__main__":
    installRequired()
