class PartyAnimal():
    x = 0
    def party (self):
        self.x = self.x + 1
        if self.x == 1:
            print(self.x, ' animal')
        else:
            print(self.x, ' animals')  
  
an = PartyAnimal()
an.party()
an.party()
an.party()