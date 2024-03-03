# settings.py
import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(""), '.env')
load_dotenv(dotenv_path)


