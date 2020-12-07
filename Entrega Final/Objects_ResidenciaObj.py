class ResidenciaObj:
    def __init__(self, tipoAlojamiento, habitaciones, banhos, camas, idDireccion, precio,
    FlexDeCancelacion, aPlus, pets, smokers, id):
        self.id = id
        self.tipoAlojamiento = tipoAlojamiento
        self.habitaciones = habitaciones
        self.banhos = banhos
        self.camas = camas
        self.idDireccion = idDireccion
        self.precio = precio
        self.flexDeCancelacion = FlexDeCancelacion
        self.aPlus = aPlus
        self.pets = pets
        self.smokers = smokers

    def __init__(
        self,
        tipoAlojamiento,
        habitaciones,
        banhos,
        camas,
        idDireccion,
        precio,
        FlexDeCancelacion,
        aPlus,
        pets,
        smokers,
        id=0,
    ):
        self.id = id
        self.tipoAlojamiento = tipoAlojamiento
        self.habitaciones = habitaciones
        self.banhos = banhos
        self.camas = camas
        self.idDireccion = idDireccion
        self.precio = precio
        self.flexDeCancelacion = FlexDeCancelacion
        self.aPlus = aPlus
        self.pets = pets
        self.smokers = smokers

class ResidenciaFullObj:
    def __init__(self, id, tipoAlojamiento, habitaciones, banhos, camas, precio,
    FlexDeCancelacion, aPlus, pets, smokers, estado, cp, calle, ciudad, pais):
        self.id = id
        self.tipoAlojamiento = tipoAlojamiento
        self.habitaciones = habitaciones
        self.banhos = banhos
        self.camas = camas
        self.precio = precio
        self.flexDeCancelacion = FlexDeCancelacion
        self.aPlus = aPlus
        self.pets = pets
        self.smokers = smokers
        self.estado = estado
        self.cp = cp
        self.calle  = calle
        self.ciudad = ciudad
        self.pais = pais
        