import networkx as nx
import matplotlib.pyplot as plt

'''
Class for input-output file management
'''
class Repository:

    def __init__(self):
        self.__fileName = ''
        self.__settingsFileName = ''

    @property
    def fileName(self):
        return self.__fileName

    @fileName.setter 
    def fileName(self, newFileName):
        with open(newFileName, 'r') :
            pass
        self.__fileName = newFileName

    @property
    def settingsFileName(self):
        return self.__settingsFileName

    @settingsFileName.setter 
    def settingsFileName(self, newFileName):
        self.__settingsFileName = newFileName
    
    '''
        Description: reads a network in gml format

        Out: the network
    '''
    def readGMLNetwork(self):
        gmlNet = nx.read_gml(self.__fileName, label = 'id')
        return gmlNet

    '''
        Description: empties file

        In: resultFileName - file to be cleared
    '''
    def clearResultFile(self, resultFileName):
        with open(resultFileName, 'w'):
            pass

    '''
        Description: writes result to file

        In: resultFileName - the file to write the result into
            bestChromo - the result of the genetic algorithm
    '''
    def writeResultToFile(self, resultFileName, bestChromo):
        with open(resultFileName, 'w') as file:
            file.write(str(len(set(bestChromo.repres))))
            file.write('\n')
            file.write(str(bestChromo.repres))

    '''
    Description: reads settings from the settings file
    '''
    def readSettings(self):
        with open(self.__settingsFileName, 'r') as settings:
            lines = settings.readlines()
            popsize = int(lines[0])
            noIterations = int(lines[1])
            return popsize, noIterations
    
    '''
    Description: writes settings from the settings file
    '''
    def writeSettingsFile(self, popsize, noIt):
        with open(self.__settingsFileName, 'w') as settings:
            settings.write(popsize)
            settings.write('\n')
            settings.writable(noIt)
