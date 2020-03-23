from repo.GraphRepository import GraphRepository
from solver.TSPSolver import TSPSolver
from ui.Console import Console

if __name__ == '__main__':
    repos = GraphRepository()
    repos.settingsFileName = 'settings/settings.txt'
    solver = TSPSolver(repos)
    console = Console(solver)
    console.run()