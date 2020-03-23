class Console:

    def __init__(self, tspSolver):
        self.__solver = tspSolver
    
    '''
        Description: changes input file for the application
    '''
    def changeFile(self):
        try:
            newFileName = input("Enter file name:")
            path = 'testTSP/' + newFileName
            self.__solver.changeFile(path)
            
        except FileNotFoundError:
            print("File not found!!")
            self.changeFile()

 
    def printMenu(self):
        print("Alegeti o optiune:")
        print("1. Rezolva problema")
        print("2. Schimba fisierul de input")
        print("3. Update settings")
        print("4. Inchide aplicatia")

    def run(self):

        self.changeFile()

        while(True):
            # try:
                self.printMenu()
                option = input("Introduceti optiunea dorita:")
                if option == '1':
                    resultFile = input("Introduceti numele fisierului rezultat: ")
                    bestChromo = self.__solver.solve(resultFile)

                elif option == '2':
                    self.changeFile()

                elif option == '3':
                    self.__solver.updateSettings()

                elif option == '4':
                    break

            # except Exception as e:
            #     print(e)