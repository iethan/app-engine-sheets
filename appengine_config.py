import sys
import os
import google
from google.appengine.ext import vendor
import logging

# lib_directory = os.path.dirname(__file__) + '/lib' 

# google.__path__.append(os.path.join(lib_directory, 'google'))

# logging.info("importing lib %s" % (lib_directory))

lib_directory = 'lib'

vendor.add(lib_directory)

