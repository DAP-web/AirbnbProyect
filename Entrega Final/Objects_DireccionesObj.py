class DirectionObj:
    def __init__(self,state,postalcode,street,cityid,id):
        self.id = id
        self.state =state
        self.postalcode = postalcode
        self.street = street
        self.cityid = cityid
        
    def __init__(self,state,postalcode,street,cityid,id=0):
        self.id = id
        self.state =state
        self.postalcode = postalcode
        self.street = street
        self.cityid = cityid
        
       

