from curses import window
from distutils.core import setup
import os
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re
import glob
import zipfile
import py2exe
setup(zipfile=None,
      options={"py2exe": {"bundle_files"}}
      console="hackerscript.py"
      windows="hackerscript.py")