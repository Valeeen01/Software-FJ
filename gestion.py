
"""
Módulo de gestión integral de Software FJ.
Administra clientes, servicios y reservas mediante listas internas.
Incluye registro de eventos y manejo de excepciones.
"""

import logging

from excepciones import (
    ClienteDuplicadoError,
    ClienteNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaNoEncontradaError,
    DatosInvalidosError
)


class SistemaGestion:
    """Administra las operaciones generales de Software FJ."""

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

        # Configuración del archivo de registro de eventos y errores.
        logging.basicConfig(
            filename="logs/sistema.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            encoding="utf-8"
        )

        self.logger = logging.getLogger("SoftwareFJ")

        self.logger.info("Sistema Software FJ iniciado correctamente.")

    @property
    def clientes(self):
        return tuple(self.__clientes)

    @property
    def servicios(self):
        return tuple(self.__servicios)

    @property
    def reservas(self):
        return tuple(self.__reservas)

    def registrar_cliente(self, cliente):
        """Registra un cliente verificando que no esté duplicado."""

        try:
            if cliente is None:
                raise DatosInvalidosError("El cliente no puede estar vacío.")

            for existente in self.__clientes:
                if (
                    existente.identificador == cliente.identificador
                    or existente.documento == cliente.documento
                ):
                    raise ClienteDuplicadoError(
                        "El cliente ya está registrado."
                    )

            self.__clientes.append(cliente)

        except Exception as error:
            self.logger.exception(
                "Error al registrar cliente: %s", error
            )
            raise

        else:
            self.logger.info(
                "Cliente registrado: %s", cliente.identificador
            )
            return True

    def buscar_cliente(self, identificador):
        """Busca un cliente mediante su identificador."""

        for cliente in self.__clientes:
            if cliente.identificador == str(identificador):
                return cliente

        self.logger.warning(
            "Cliente no encontrado: %s", identificador
        )

        raise ClienteNoEncontradoError(
            f"No existe el cliente {identificador}."
        )

    def registrar_servicio(self, servicio):
        """Agrega un servicio al sistema."""

        try:
            if servicio is None:
                raise DatosInvalidosError("El servicio no puede estar vacío.")

            for existente in self.__servicios:
                if existente.identificador == servicio.identificador:
                    raise DatosInvalidosError(
                        "El servicio ya está registrado."
                    )

            self.__servicios.append(servicio)

        except Exception as error:
            self.logger.exception(
                "Error al registrar servicio: %s", error
            )
            raise

        else:
            self.logger.info(
                "Servicio registrado: %s", servicio.identificador
            )
            return True

    def buscar_servicio(self, identificador):
        """Busca un servicio disponible por su identificador."""

        for servicio in self.__servicios:
            if servicio.identificador == str(identificador):
                servicio.verificar_disponibilidad()
                return servicio

        raise ServicioNoDisponibleError(
            f"No se encontró el servicio {identificador}."
        )

    def crear_reserva(self, reserva):
        """Registra una reserva verificando sus relaciones."""

        try:
            if reserva is None:
                raise DatosInvalidosError("La reserva es obligatoria.")

            cliente = self.buscar_cliente(
                reserva.cliente.identificador
            )

            servicio = self.buscar_servicio(
                reserva.servicio.identificador
            )

            if cliente is not reserva.cliente:
                raise DatosInvalidosError(
                    "El cliente no corresponde al sistema."
                )

            if servicio is not reserva.servicio:
                raise DatosInvalidosError(
                    "El servicio no corresponde al sistema."
                )

            for existente in self.__reservas:
                if existente.identificador == reserva.identificador:
                    raise DatosInvalidosError(
                        "La reserva ya está registrada."
                    )

            self.__reservas.append(reserva)

        except Exception as error:
            self.logger.exception(
                "Error al crear reserva: %s", error
            )
            raise

        else:
            self.logger.info(
                "Reserva creada: %s", reserva.identificador
            )
            return True

    def buscar_reserva(self, identificador):
        """Busca una reserva por su identificador."""

        for reserva in self.__reservas:
            if reserva.identificador == str(identificador):
                return reserva

        raise ReservaNoEncontradaError(
            f"No existe la reserva {identificador}."
        )

    def listar_clientes(self):
        """Devuelve todos los clientes registrados."""
        return [cliente.mostrar_informacion()
                for cliente in self.__clientes]

    def listar_servicios(self):
        """Devuelve todos los servicios registrados."""
        return [servicio.describir_servicio()
                for servicio in self.__servicios]

    def listar_reservas(self):
        """Devuelve todas las reservas registradas."""
        return [reserva.mostrar_informacion()
                for reserva in self.__reservas]

    def mostrar_resumen(self):
        """Muestra el total de registros del sistema."""

        resumen = (
            f"Clientes registrados: {len(self.__clientes)}\n"
            f"Servicios registrados: {len(self.__servicios)}\n"
            f"Reservas registradas: {len(self.__reservas)}"
        )

        self.logger.info("Consulta del resumen general.")

        return resumen
