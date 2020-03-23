from repo.GraphRepository import GraphRepository
from utils.GeneticAlgo import GeneticAlgorithm

'''
Class for solving the network communities problem
'''
class TSPSolver:

    def __init__(self, repository):
        self.__repo = repository
        size, iterations = self.__repo.readSettings()
        self.__noIterations = iterations
        self.__popSize = size

    '''
    Description : refreshes the settings from the settings file
    '''
    def updateSettings(self):
        size, iterations = self.__repo.readSettings()
        self.__noIterations = iterations
        self.__popSize = size

    '''
    Euristic for calculating the fit of the chromosome for the community problem

    In: communities - the community combination of the network's nodes
        param - parameter dict - need the adjacency matrix, the degrees of the nodes and the number of nodes and edeges
    
    Out: the computed fitness
    '''
    @staticmethod
    def totalDistance(permutation, probl_param):
        noNodes = probl_param['noNodes']
        mat = probl_param['mat']
        distance = 0
        for i in range(len(permutation) - 1):
            distance += probl_param['mat'][permutation[i]][permutation[i+1]]
        distance += probl_param['mat'][permutation[0]][permutation[len(permutation)-1]]
        return distance

    def changeFile(self, file):
        self.__repo.fileName = file

    '''
    Description : solves the community problem, plots the result and writes it to a given file

    In : resultFile - the output file name
    '''
    def solve(self, resultFile):
        mat = self.__repo.readData()
            
        problParam = {'noNodes' : len(mat), 'min': 0, 'max' : len(mat) - 1, 'function' : TSPSolver.totalDistance, 'mat' : mat}
        param = {'popSize' : self.__popSize, 'noNodes': len(mat), 'mat':mat}
        
        ga = GeneticAlgorithm(param, problParam)
        ga.initialisation()
        ga.evaluation()

        n = self.__noIterations
        while(n > 0):
            ga.oneGenerationElitism()
            print('Generation', self.__noIterations - n, ':', ga.bestChromosome())
            n-= 1

        self.__repo.writeResultToFile(resultFile, ga.bestChromosome().repres, ga.bestChromosome().fitness ,len(ga.bestChromosome().repres))