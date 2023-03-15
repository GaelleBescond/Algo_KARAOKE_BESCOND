import random

# name, liste de scores
class Player:
    def __init__ (self, name):
        self._name = name
        self._score = [55,62,60,85,52]
        self._bestScore = 0
        self._bestSong = 0
        self._worstScore = 100
        self._worstSong = 0
        self._moyenne = 0
    
    def getName(self):
        return self._name

    def getMoyenne(self):
        return self._moyenne

    def getScoreMax(self):     
        return self._bestScore
    
    def getScoreMin(self):      
        return self._worstScore

    def compareScores(self, i):        
        if self._bestScore < self._score[i]:
            self._bestScore = self._score[i]
            self._bestSong = i 
            print("Nouveau record pour cette chanson!")
        else :
            print("On a vu mieux")

        if self._worstScore > self._score[i]:
            self._worstScore = self._score[i]    
            self._worstSong = i   
            print("Vraiment c'était nul mais wow!")         
        
    def checkScores(self):
        for i in range (len(self._score)):
            if self._bestScore < self._score[i]:
                self._bestScore = self._score[i]
                self._bestSong = i+1 
            if (self._worstScore > self._score[i]) and (self._score[i] > 0):
                self._worstScore = self._score[i]    
                self._worstSong = i+1   
            self._moyenne += self._score[i]
        self._moyenne = self._moyenne/(len(self._score))

    def getBestChanson(self):
        return self._bestSong

    def getWorstChanson(self):
        return self._worstSong

    def sing(self, x):
        scoreChanson = random.randint(50,100)
        if scoreChanson > self._score[x-1]:
            self._score[x-1] = scoreChanson
        return scoreChanson

game = True
x = 0

gaelle = Player("Gaelle")
listeJoueurs = [gaelle]


while game:
    listeJoueurs[x].checkScores()
    print("C'est à ", listeJoueurs[x].getName(), "de chanter")
    print("Le score max de", listeJoueurs[x].getName(), "est", listeJoueurs[x].getScoreMax(), "sur la chanson", listeJoueurs[x].getBestChanson())
    print("Le score min de", listeJoueurs[x].getName(), "est", listeJoueurs[x].getScoreMin(), "sur la chanson", listeJoueurs[x].getWorstChanson())
    print("La moyenne de", listeJoueurs[x].getName(), "est", listeJoueurs[x].getMoyenne())
    choixChanson =int(input(" Sur quelle chanson? (1 à 5)"))
    print(listeJoueurs[x].getName(), "marque", listeJoueurs[x].sing(choixChanson), "points sur la chanson", choixChanson)
    listeJoueurs[x].compareScores((choixChanson-1))

