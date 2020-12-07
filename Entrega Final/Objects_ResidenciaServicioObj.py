class ResidenciaObj:
    def __init__(self, IdServicio, IdResidencia, id):
        self.id = id
        self.IdServicio = IdServicio
        self.IdResidencia = IdResidencia

    def __init__(
        self,
        IdServicio,
        IdResidencia,
        id=0,
    ):
        self.id = id
        self.IdServicio = IdServicio
        self.IdResidencia = IdResidencia
