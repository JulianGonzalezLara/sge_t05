from typing import List

from modelo.Socio import Socio
class Familia:
    def __init__(self, pareja:Socio = None, hijos:List[Socio]=[]):
        self.pareja = pareja
        self. hijos = hijos