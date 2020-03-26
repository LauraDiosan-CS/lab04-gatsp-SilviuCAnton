from math import sqrt

class GraphRepository:

    def __init__(self):
        self.__fileName = ''
        self.__settingsFileName = ''
    
    '''
        Description: reads from file and returns a Graph as a matrix of distances between nodes

        Out: nodeDist - the distance Matrix
             startNode - the node to start the search from
             destinationNode - the node to be searched
    '''
    def readData(self):
        if(self.__fileName == "testTSP/berlin52.txt"):
            return self.readBerlin()
        else:
            nodeDist = []
            with open(self.__fileName, 'r') as file:
                nOfNodes = int(file.readline())
                for i in range(nOfNodes):
                    dist = file.readline().strip().split(',')
                    nodeDist.append(list(map(int,dist)))
            return nodeDist


    '''
        Description: writes result to file

        In: distance - the total distance
            result - the result path
            nNodes - the number of nodes in the result path
            resultFileName - the name of the file
    '''
    def writeResultToFile(self, resultFileName, result, distance, nNodes):
        with open(resultFileName, 'w') as file:
            file.write(str(nNodes))
            file.write('\n')
            for node in result:
                file.write(str(node) + ' ')
            file.write('\n')
            file.write(str(distance))
            file.write('\n')
    
    @property    
    def fileName(self):
        return self.__fileName

    @fileName.setter
    def fileName(self, newFileName):
        self.__fileName = newFileName

    @property    
    def settingsFileName(self):
        return self.__settingsFileName

    @settingsFileName.setter
    def settingsFileName(self, newSettingsFileName):
        self.__settingsFileName = newSettingsFileName

    '''
    Description: reads settings from the settings file
    '''
    def readSettings(self):
        with open(self.__settingsFileName, 'r') as settings:
            lines = settings.readlines()
            popsize = int(lines[0])
            noIterations = int(lines[1])
            return popsize, noIterations

    def readBerlin(self):
        mat = []
        with open(self.__fileName, 'r') as file:
            for line in file.readlines():
                lineargs = line.split(' ')
                mat.append((float(lineargs[1]), float(lineargs[2])))
        
        
        result = []
        for i in range(len(mat)):
            node = []
            for j in range(len(mat)):
                dist = int(sqrt((mat[i][0]-mat[j][0])*(mat[i][0]-mat[j][0]) + (mat[i][1]-mat[j][1])*(mat[i][1]-mat[j][1])))
                node.append(dist)
            result.append(node)
        
        return result