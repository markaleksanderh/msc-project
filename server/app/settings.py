from environs import Env

env = Env()

DEBUG = env.bool('DEBUG', default=True)
BIND_HOST = env('BIND_HOST', default='127.0.0.1')
BIND_PORT = env.int('BIND_PORT', default=5000)