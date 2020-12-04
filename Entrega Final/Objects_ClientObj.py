class ClientObj:
    def __init__(self,name,lastname, telephone, country, email, pswd, user,id):
        self.id=id
        self.name = name
        self.lastname = lastname
        self.telephone = telephone
        self.country = country
        self.email = email
        self.pswd = pswd
        self.user = user
    
    def __init__(self,name,lastname, telephone, country, email, pswd, user,id=0):
        self.id=id
        self.name = name
        self.lastname = lastname
        self.telephone = telephone
        self.country = country
        self.email = email
        self.pswd = pswd
        self.user = user
