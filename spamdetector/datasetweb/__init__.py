from .data import *
from .routes import *
import bottle
import os


bottle.TEMPLATE_PATH = [os.path.join(os.path.dirname(__file__), 'templates')]
bottle.run(reloader=True)
