class ExperienciaObj:
    def __init__(self, NombreAnfitrion, TituloExperiencia, TipoDeExperiencia,
    Ubicacion, Descripcion, Idioma, PublicoObjetivo, Organizacion,
    AnfitrionExp, ElementosANecesitar, precio, fecha, IdTematica, id):
        self.id = id
        self.host = NombreAnfitrion
        self.ExperienceTitle = TituloExperiencia
        self.TypeExperience = TipoDeExperiencia
        self.Location = Ubicacion
        self.Descrption = Descripcion
        self.Idiom = Idioma
        self.PublicObject = PublicoObjetivo
        self.Organization = Organizacion
        self.hostExperience = AnfitrionExp
        self.NeedElements = ElementosANecesitar
        self.precio = precio
        self.fecha = fecha
        self.idTematic = IdTematica
