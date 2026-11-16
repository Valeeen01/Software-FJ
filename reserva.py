
"""
Módulo de reservas de Software FJ.
Gestiona la creación, confirmación, cancelación y procesamiento
de reservas mediante programación orientada a objetos.
"""

from entidades import Entidad
from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    ServicioNoDisponibleError,
    CalculoInvalidoError
)


class Reserva(Entidad):
    """Representa una reserva realizada por un cliente."""

    ESTADOS_VALIDOS = ("Pendiente", "Confirmada", "Cancelada", "Procesada")

    def __init__(
        self,
        identificador,
        cliente,
        servicio,
        duracion,
        descuento=0,
        impuesto=0
    ):
        super().__init__(identificador)

        if cliente is None:
            raise ReservaInvalidaError("Debe seleccionar un cliente.")

        if servicio is None:
            raise ReservaInvalidaError("Debe seleccionar un servicio.")

        try:
            duracion = float(duracion)
        except (TypeError, ValueError) as error:
            raise ReservaInvalidaError(
                "La duración debe ser numérica."
            ) from error

        if duracion <= 0:
            raise ReservaInvalidaError(
                "La duración debe ser mayor que cero."
            )

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__descuento = descuento
        self.__impuesto = impuesto
        self.__estado = "Pendiente"
        self.__costo = None

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self.__estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        try:
            self.__servicio.verificar_disponibilidad()

            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                self.__descuento,
                self.__impuesto
            )

        except ServicioNoDisponibleError:
            raise

        except (DatosInvalidosError, CalculoInvalidoError):
            raise

        else:
            self.__estado = "Confirmada"
            return True

    def cancelar(self):
        """Cancela una reserva que no haya sido procesada."""

        if self.__estado not in ("Pendiente", "Confirmada"):
            raise OperacionNoPermitidaError(
                "No se puede cancelar esta reserva."
            )

        self.__estado = "Cancelada"
        return True

    def procesar(self):
        """Procesa una reserva previamente confirmada."""

        if self.__estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada antes de procesarse."
            )

        try:
            self.__servicio.verificar_disponibilidad()

            if self.__costo is None or self.__costo <= 0:
                raise CalculoInvalidoError(
                    "El costo de la reserva no es válido."
                )

        except (ServicioNoDisponibleError, CalculoInvalidoError):
            raise

        else:
            self.__estado = "Procesada"
            return True

        finally:
            # Registra que el intento de procesamiento terminó.
            pass

    def mostrar_informacion(self):
        """Devuelve el resumen completo de la reserva."""

        costo = (
            f"${self.__costo:,.2f}"
            if self.__costo is not None
            else "Pendiente de cálculo"
        )

        return (
            f"Reserva: {self.identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: {costo}"
        )

    def __str__(self):
        return self.mostrar_informacion()
