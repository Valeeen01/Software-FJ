
"""
Módulo de servicios de Software FJ.
Implementa abstracción, herencia y polimorfismo.
"""

from abc import abstractmethod
from entidades import Entidad
from excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError,
    CalculoInvalidoError
)


class Servicio(Entidad):
    """Clase abstracta que representa un servicio de Software FJ."""

    def __init__(self, identificador, nombre, precio_base):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")

        try:
            precio_base = float(precio_base)
        except (TypeError, ValueError) as error:
            raise DatosInvalidosError(
                "El precio base debe ser numérico."
            ) from error

        if precio_base <= 0:
            raise DatosInvalidosError("El precio debe ser mayor que cero.")

        self._nombre = nombre.strip()
        self._precio_base = precio_base
        self._disponible = True

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @property
    def disponible(self):
        return self._disponible

    def cambiar_disponibilidad(self, estado):
        if not isinstance(estado, bool):
            raise DatosInvalidosError(
                "La disponibilidad debe ser verdadera o falsa."
            )

        self._disponible = estado

    def verificar_disponibilidad(self):
        if not self._disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self._nombre} no está disponible."
            )

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        """
        Calcula el costo permitiendo diferentes variantes:
        costo básico, costo con descuento y costo con impuesto.
        """

        try:
            cantidad = float(cantidad)
            descuento = float(descuento)
            impuesto = float(impuesto)
        except (TypeError, ValueError) as error:
            raise CalculoInvalidoError(
                "Los parámetros del cálculo deben ser numéricos."
            ) from error

        if cantidad <= 0:
            raise CalculoInvalidoError(
                "La cantidad debe ser mayor que cero."
            )

        if not 0 <= descuento <= 100:
            raise CalculoInvalidoError(
                "El descuento debe estar entre 0 y 100."
            )

        if not 0 <= impuesto <= 100:
            raise CalculoInvalidoError(
                "El impuesto debe estar entre 0 y 100."
            )

        subtotal = self._precio_base * cantidad
        valor_descuento = subtotal * descuento / 100
        total = (subtotal - valor_descuento) * (1 + impuesto / 100)

        return round(total, 2)

    @abstractmethod
    def validar_parametros(self, cantidad):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    def mostrar_informacion(self):
        return (
            f"{self._nombre} | "
            f"Precio base: ${self._precio_base:,.2f} | "
            f"Disponible: {self._disponible}"
        )


class ReservaSala(Servicio):
    """Servicio especializado de reserva de salas."""

    def __init__(self, identificador, nombre, precio_hora, capacidad):
        super().__init__(identificador, nombre, precio_hora)

        if not isinstance(capacidad, int) or capacidad <= 0:
            raise DatosInvalidosError(
                "La capacidad debe ser un entero positivo."
            )

        self.__capacidad = capacidad

    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise DatosInvalidosError(
                "Las horas de reserva deben ser positivas."
            )

        return True

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        self.validar_parametros(cantidad)
        return super().calcular_costo(cantidad, descuento, impuesto)

    def describir_servicio(self):
        return (
            f"Reserva de sala: {self.nombre}. "
            f"Capacidad máxima: {self.__capacidad} personas."
        )


class AlquilerEquipos(Servicio):
    """Servicio especializado de alquiler de equipos."""

    def __init__(self, identificador, nombre, precio_dia, tipo_equipo):
        super().__init__(identificador, nombre, precio_dia)

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise DatosInvalidosError("El tipo de equipo es obligatorio.")

        self.__tipo_equipo = tipo_equipo.strip()

    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise DatosInvalidosError(
                "Los días de alquiler deben ser positivos."
            )

        return True

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        self.validar_parametros(cantidad)
        return super().calcular_costo(cantidad, descuento, impuesto)

    def describir_servicio(self):
        return (
            f"Alquiler de equipos: {self.nombre}. "
            f"Tipo de equipo: {self.__tipo_equipo}."
        )


class AsesoriaEspecializada(Servicio):
    """Servicio especializado de asesorías profesionales."""

    def __init__(self, identificador, nombre, precio_hora, especialidad):
        super().__init__(identificador, nombre, precio_hora)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("La especialidad es obligatoria.")

        self.__especialidad = especialidad.strip()

    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise DatosInvalidosError(
                "Las horas de asesoría deben ser positivas."
            )

        return True

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        self.validar_parametros(cantidad)
        return super().calcular_costo(cantidad, descuento, impuesto)

    def describir_servicio(self):
        return (
            f"Asesoría especializada: {self.nombre}. "
            f"Especialidad: {self.__especialidad}."
        )
