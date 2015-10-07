__author__ = 'shaleen'

import MySQLdb
import abc

class Connector:

    QUICKRDB = 'test'
    QUICKRROOT = 'root'
    QUICKRPASS = 'help2012'
    QUICKRLOCAL = 'localhost'
    QUICKRTABLE = 'Quickr'


    def generateDBConnector(self, root):
        if root == 'QUICKR':
            return MySQLdb.connect(self.QUICKRLOCAL, self.QUICKRROOT, self.QUICKRPASS, self.QUICKRDB)
        if root == 'TEST':
            return MySQLdb.connect(self.QUICKRLOCAL, self.QUICKRROOT, self.QUICKRPASS, self.QUICKRDB)

    @abc.abstractmethod
    def getCursor(self):
        return

    @abc.abstractmethod
    def getInsertQueryTemplate(self):
        return

    @abc.abstractmethod
    def populateAndExecute(self):
        return


