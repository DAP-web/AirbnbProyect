class CountryObj:
    def __init__(self,countryname,code,id):
        self.id=id
        self.countryname = countryname
        self.code = code
    
    def __init__(self,countryname,code,id=0):
        self.id=id
        self.countryname = countryname
        self.code = code
