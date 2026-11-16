
"""
Módulo de gestión de clientes de Software FJ.
Implementa herencia, encapsulación y validaciones robustas.
"""

import re
from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):
    """Representa un cliente registrado en Software FJ."""

    def __init__(self, identificador, nombre, documento, correo, telefono):
        super().__init__(identificador)

        self.__nombre = self.__validar_nombre(nombre)
        self.__documento = self.__validar_documento(documento)
        self.__correo = self.__validar_correo(correo)
        self.__telefono = self.__validar_telefono(telefono)

    @staticmethod
    def __validar_nombre(nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre no puede estar vacío.")

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s'-]+", nombre.strip()):
            raise DatosInvalidosError("El nombre contiene caracteres inválidos.")

        return nombre.strip().title()

    @staticmethod
    def __validar_documento(documento):
        documento = str(documento).strip()

        if not documento.isdigit() or not 6 <= len(documento) <= 15:
            raise DatosInvalidosError(
                "El documento debe contener entre 6 y 15 dígitos."
            )

        return documento

    @staticmethod
    def __validar_correo(correo):
        if not isinstance(correo, str):
            raise DatosInvalidosError("El correo debe ser texto.")

        correo = correo.strip().lower()

        patron = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not re.fullmatch(patron, correo):
            raise DatosInvalidosError("El correo electrónico no es válido.")

        return correo

    @staticmethod
    def __validar_telefono(telefono):
        telefono = str(telefono).strip()

        if not telefono.isdigit() or not 7 <= len(telefono) <= 15:
            raise DatosInvalidosError(
                "El teléfono debe contener entre 7 y 15 dígitos."
            )

        return telefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def actualizar_correo(self, nuevo_correo):
        self.__correo = self.__validar_correo(nuevo_correo)

    def actualizar_telefono(self, nuevo_telefono):
        self.__telefono = self.__validar_telefono(nuevo_telefono)

    def mostrar_informacion(self):
        return (
            f"ID: {self.identificador} | "
            f"Nombre: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )

    def __str__(self):
        return self.mostrar_informacion()
