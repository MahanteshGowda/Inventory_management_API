"""
This script runs the LimaPaymentApis application using a development server.
"""
from os import environ
from source import app


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 8799
    app.run(HOST, PORT)
