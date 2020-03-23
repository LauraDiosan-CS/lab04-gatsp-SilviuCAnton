from random import randint, sample
from domain.TSPChromosome import Chromosome

'''
Class for a generic genetic algorithm
'''
class GeneticAlgorithm:
    def __init__(self, param = None, problParam = None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []
        
    @property
    def population(self):
        return self.__population
    
    '''
    Description: Initiates the population with a 'popSize' number of chromosomes
    '''
    def initialisation(self):
        for _ in range(0, self.__param["popSize"]):
            c = Chromosome(self.__problParam)
            self.__population.append(c)
    
    '''
    Description: recomputes the fitness of each chromosome in the current population
    '''
    def evaluation(self):
        for c in self.__population:
            res = self.__problParam['function'](c.repres, self.__param)
            c.fitness = res

    '''
    Description : returns the most 'fit' chromosome

    Out: best - the chromosome with the best fitness
    '''        
    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best

    '''
    Description : returns the least 'fit' chromosome

    Out: worst - the chromosome with the worst fitness
    '''      
    def worstChromosome(self):
        worst = self.__population[0]
        for c in self.__population:
            if (c.fitness > worst.fitness):
                worst = c
        return worst

    '''
    Description: selects one chromosome from the current population

    Out: the selected chromosome
    '''
    def selection(self):
        pos1 = randint(0, self.__param["popSize"] - 1)
        pos2 = randint(0, self.__param["popSize"] - 1)
        if (self.__population[pos1].fitness < self.__population[pos2].fitness):
            return pos1
        else:
            return pos2 
        
    '''
    Descripton: generates a new generation of chromosomes by crossing two parents and mutating the child 
    '''
    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param["popSize"]):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    '''
    Descripton: generates a new generation of chromosomes using elitism principle - the best chromosome in the generation passes on to the next generation 
    '''
    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param["popSize"] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    '''
    Descripton: generates a new generation of chromosomes using steady state principle - replaces the worst chromosome with a newborn one if the newborn has a better fitness
    ''' 
    def oneGenerationSteadyState(self):
        for _ in range(self.__param["popSize"]):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__problParam['function'](off.repres, self.__param)
            worst = self.worstChromosome()
            if (off.fitness < worst.fitness):
                worst = off       
            