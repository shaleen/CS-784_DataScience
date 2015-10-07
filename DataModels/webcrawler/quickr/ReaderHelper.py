__author__ = 'shaleen'
import urllib
import os
import glob

class Helper(object):
    def __init__(self):
        self._html_directory = 'html/'

    def readContentFromFile(self, fileName):
        f = open(fileName, 'r')
        return f

    def getAbsoluteUrl(self, fileName):
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, fileName)
        return abs_file_path

    def getHtmlFileHandle(self, name):
        script_dir = os.path.dirname(__file__)
        rel_path = self._html_directory + name
        abs_file_path = os.path.join(script_dir, rel_path)
        return abs_file_path

