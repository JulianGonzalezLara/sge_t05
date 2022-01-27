class Usuario:
    def __init__(this, dni = None, contrasenna = None, ultimoAcceso = None, es_admin = None):
        this._dni = dni
        this._contrasenna = contrasenna
        this._ultimoAcceso = ultimoAcceso
        this._es_admin = es_admin

    def getInfo(this):
        return "Dni: {}. \n\tContraseña:  {}. \n\tUltimo Acceso:  {}. \n\tEs Admin:  {}.".format(this._dni,this._contrasenna,this._ultimoAcceso,this._es_admin)