
"""
Módulo de entidades generales del sistema Software FJ.
Implementa el principio de abstracción mediante clases abstractas.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general del sistema.
    Todas las entidades tendrán identificador y fecha de creación.
    """

    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        self.__identificador = str(identificador)
        self.__fecha_creacion = datetime.now()

    @property
    def identificador(self):
        """Permite consultar el identificador sin modificarlo directamente."""
        return self.__identificador

    @property
    def fecha_creacion(self):
        """Devuelve la fecha de creación de la entidad."""
        return self.__fecha_creacion

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto que debe implementarse
        obligatoriamente en las clases derivadas.
        """
        pass

    def __str__(self):
        return f"Entidad: {self.__identificador}"
