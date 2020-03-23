from random import uniform
from random import randint

'''
Class for the chromosome representation
'''
class Chromosome:

    def __init__(self, problParam = None):
        self.__problParam = problParam
        # self.__repres = Chromosome.renumbering([int(uniform(problParam['min'], problParam['max'])) for _ in range(problParam['noDim'])])
        # self.__repres = [int(uniform(problParam['min'], problParam['max'])) for _ in range(problParam['noDim'])]

        self.__repres = []
        noLeaders = round(0.2 * (self.__problParam['max'] + 1))
        self.__repres = [None for _ in range(self.__problParam['max'] + 1)]

        for i in range(len(self.__repres)):

            if self.__repres[i] is None:
                self.__repres[i] = randint(0, self.__problParam['max'] )
                remaining = (self.__problParam['max'] + 1) - i

                if uniform(0, 1) <= noLeaders / remaining:
                    noLeaders -= 1
                    indices = (self.__problParam['mat'][i] > 0).nonzero()[1]

                    for j in indices:
                        if self.__repres[j] is None:
                            self.__repres[j] = self.__repres[i]

        self.__fitness = 0.0
    
    @property
    def repres(self):
        return self.__repres
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 

    '''
    Description : renumbers the representation of the chromosome to a standard (1-n)
    '''
    @staticmethod
    def renumbering(repr):
        reprdict = {}
        number = 1
        for label in sorted(repr):
            if label not in reprdict:
                reprdict[label] = number
                number += 1
        for i in range(len(repr)):
            repr[i] = reprdict[repr[i]]
        return repr

    '''
    Description: generates a random bitmask of a given length

    In: size - the length of the bitmask

    Out: bitmask - the computed bitmask
    '''
    @staticmethod
    def generateBitMask(size):
        bitMask = []
        for _ in range(size):
            bitMask.append(randint(0,1))
        return bitMask
            
    
    '''
    The crossover operation between two chromosomes

    In: c - other chromosome

    Out: offspring - the newborn chromosome
    '''
    def crossover(self, c):
        self.__repres = Chromosome.renumbering(self.__repres)
        c.__repres = Chromosome.renumbering(c.__repres)
        r = randint(0, len(self.__repres) - 1)
        newrepres = []
        for i in range(r):
            newrepres.append(self.__repres[i])
        for i in range(r, len(self.__repres)):
            newrepres.append(c.__repres[i])
        
        # bitmask = Chromosome.generateBitMask(len(self.__repres))
        # newrepres = []
        # for i in range(len(self.__repres)):
        #     if bitmask[i] == 0:
        #         newrepres.append(self.__repres[i])
        #     else: newrepres.append(c.__repres[i])
        offspring = Chromosome(c.__problParam)
        # offspring.repres = Chromosome.renumbering(newrepres)
        offspring.repres = newrepres
        return offspring
    
    '''
    Description: mutates the chromosome
    '''
    def mutation(self):
        pos = randint(0, len(self.__repres) - 1)
        neighbors = []
        for i in range(0,self.__problParam['max']):
            if self.__problParam['mat'][pos, i] > 0 :
                neighbors.append(i)
        respos = randint(0, len(neighbors)-1)
        self.__repres[pos] = self.__repres[neighbors[respos]]
        # self.__repres = Chromosome.renumbering(self.__repres)

    '''
    Description: mutates the chromosome using differential evolution principle
    '''
    def mutation2(self, rep1, rep2, rep3):
        pos = randint(0, len(self.__repres) - 1)
        f = uniform(0,1)
        
        newval = abs(int(rep1[pos] + f * (rep2[pos] - rep3[pos])))

        if newval > self.__problParam['max']:
            newval = int(uniform(self.__problParam['min'], self.__problParam['max']))

        self.__repres[pos] = newval
        # self.__repres = Chromosome.renumbering(newRepres)

        
    def __str__(self):
        return '\nChromosome: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness