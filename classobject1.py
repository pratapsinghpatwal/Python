import datetime

class cricketplayer :
    def __init__(self,fname,lname,byear,team):
        self.firstname=fname
        self.lastname=lname
        self.birthyear=byear
        self.team=team
        self.score=[]
    def getage(self) :
        now=datetime.datetime.now()
        return now.year-self.birthyear
    def addscore(self,score):
        self.score.append(score)
    def getavgscore(self) :
        return sum(self.score)/len(self.score)
    def __gt__(self,other) :
        myscore=self.getavgscore()
        otherscore=other.getavgscore()
        print(myscore)
        print(otherscore)
        return (myscore>otherscore)

virat=cricketplayer('virat','kohali',1988,'india')
virat.addscore(30)
virat.addscore(120)
virat.addscore(100)
virat.addscore(110)

david=cricketplayer('david','warner',1980,'austrailia')

david.addscore(30)
david.addscore(90)
david.addscore(80)
david.addscore(90)

print('The Age  of Virat kohali  ',virat.getage())
print('The avg score of Virat kohali  ',virat.getavgscore())

print('The Age of David warner  ',david.getage())
print('The avg score of David warner  ',david.getavgscore())

# operator overloading
print(virat>david)