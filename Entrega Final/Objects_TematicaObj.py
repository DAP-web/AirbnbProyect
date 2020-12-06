class TematicaObj:
    def __init__(self,tematicaname,description,id):
        self.id=id
        self.tematicaname = tematicaname
        self.description = description


    def __init__(self,tematicaname,description,id=0):
        self.id=id
        self.tematicaname = tematicaname
        self.description = description