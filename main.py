
"""
Programa principal del Sistema Integral de Gestión
de Clientes, Servicios y Reservas de Software FJ.

Ejecuta pruebas de funcionamiento y demuestra
los conceptos de programación orientada a objetos.
"""

import logging

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipos, AsesoriaEspecializada
from reserva import Reserva
from gestion import SistemaGestion
from excepciones import (
    DatosInvalidosError,
    ClienteDuplicadoError,
    ClienteNoEncontradoError,
    ServicioNoDisponibleError,
    OperacionNoPermitidaError,
    ReservaInvalidaError
)


def ejecutar_pruebas():
    """Ejecuta las operaciones de demostración del sistema."""

    sistema = SistemaGestion()

    print("=" * 65)
    print("       SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("=" * 65)

    # ---------------------------------------------------------
    # OPERACIÓN 1: Registrar un cliente correctamente.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 1: Registro de cliente")

    cliente1 = Cliente(
        "C001",
        "Laura Rodriguez",
        "1020304050",
        "laura@gmail.com",
        "3001234567"
    )

    sistema.registrar_cliente(cliente1)
    print("Resultado:", cliente1.mostrar_informacion())

    # ---------------------------------------------------------
    # OPERACIÓN 2: Registrar un segundo cliente.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 2: Registro de segundo cliente")

    cliente2 = Cliente(
        "C002",
        "Carlos Martinez",
        "1098765432",
        "carlos@gmail.com",
        "3109876543"
    )

    sistema.registrar_cliente(cliente2)
    print("Cliente registrado:", cliente2.nombre)

    # ---------------------------------------------------------
    # OPERACIÓN 3: Intentar registrar un cliente duplicado.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 3: Prueba de cliente duplicado")

    try:
        cliente_duplicado = Cliente(
            "C003",
            "Maria Lopez",
            "1020304050",
            "maria@gmail.com",
            "3201234567"
        )

        sistema.registrar_cliente(cliente_duplicado)

    except ClienteDuplicadoError as error:
        print("Error controlado:", error)

    # ---------------------------------------------------------
    # OPERACIÓN 4: Intentar registrar datos inválidos.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 4: Prueba de datos inválidos")

    try:
        Cliente(
            "C004",
            "",
            "123",
            "correo_incorrecto",
            "123"
        )

    except DatosInvalidosError as error:
        print("Error controlado:", error)

    # ---------------------------------------------------------
    # OPERACIÓN 5: Registrar los servicios disponibles.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 5: Registro de servicios")

    sala = ReservaSala(
        "S001",
        "Sala de reuniones",
        50000,
        10
    )

    equipos = AlquilerEquipos(
        "S002",
        "Computador portátil",
        80000,
        "Computador"
    )

    asesoria = AsesoriaEspecializada(
        "S003",
        "Asesoría tecnológica",
        100000,
        "Ingeniería de sistemas"
    )

    sistema.registrar_servicio(sala)
    sistema.registrar_servicio(equipos)
    sistema.registrar_servicio(asesoria)

    print("Servicios registrados correctamente.")

    # ---------------------------------------------------------
    # OPERACIÓN 6: Buscar un cliente.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 6: Búsqueda de cliente")

    cliente_encontrado = sistema.buscar_cliente("C001")
    print("Cliente encontrado:", cliente_encontrado.nombre)

    # ---------------------------------------------------------
    # OPERACIÓN 7: Intentar buscar un cliente inexistente.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 7: Búsqueda de cliente inexistente")

    try:
        sistema.buscar_cliente("C999")

    except ClienteNoEncontradoError as error:
        print("Error controlado:", error)

    # ---------------------------------------------------------
    # OPERACIÓN 8: Crear una reserva correctamente.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 8: Creación de reserva")

    reserva1 = Reserva(
        "R001",
        cliente1,
        sala,
        2,
        descuento=10,
        impuesto=19
    )

    sistema.crear_reserva(reserva1)
    print("Reserva creada correctamente.")

    # ---------------------------------------------------------
    # OPERACIÓN 9: Confirmar la reserva.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 9: Confirmación de reserva")

    reserva1.confirmar()

    print("Reserva confirmada.")
    print("Costo total:", f"${reserva1.costo:,.2f}")

    # ---------------------------------------------------------
    # OPERACIÓN 10: Procesar la reserva.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 10: Procesamiento de reserva")

    reserva1.procesar()

    print("Reserva procesada correctamente.")
    print("Estado:", reserva1.estado)

    # ---------------------------------------------------------
    # OPERACIÓN 11: Crear una segunda reserva.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 11: Segunda reserva")

    reserva2 = Reserva(
        "R002",
        cliente2,
        equipos,
        3
    )

    sistema.crear_reserva(reserva2)
    print("Segunda reserva creada correctamente.")

    # ---------------------------------------------------------
    # OPERACIÓN 12: Cancelar una reserva.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 12: Cancelación de reserva")

    reserva2.cancelar()

    print("Reserva cancelada.")
    print("Estado:", reserva2.estado)

    # ---------------------------------------------------------
    # OPERACIÓN 13: Intentar confirmar un servicio no disponible.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 13: Servicio no disponible")

    asesoria.cambiar_disponibilidad(False)

    try:
        reserva3 = Reserva(
            "R003",
            cliente1,
            asesoria,
            2
        )

        sistema.crear_reserva(reserva3)

    except ServicioNoDisponibleError as error:
        print("Error controlado:", error)

    # ---------------------------------------------------------
    # OPERACIÓN 14: Intentar crear una reserva con duración inválida.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 14: Reserva con duración inválida")

    try:
        Reserva(
            "R004",
            cliente1,
            sala,
            -5
        )

    except ReservaInvalidaError as error:
        print("Error controlado:", error)

    # ---------------------------------------------------------
    # OPERACIÓN 15: Intentar realizar una operación no permitida.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 15: Operación no permitida")

    try:
        reserva1.cancelar()

    except OperacionNoPermitidaError as error:
        print("Error controlado:", error)

    # ---------------------------------------------------------
    # OPERACIÓN 16: Demostrar cálculo con diferentes parámetros.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 16: Cálculo de costos")

    costo_basico = sala.calcular_costo()
    costo_descuento = sala.calcular_costo(2, 15)
    costo_completo = sala.calcular_costo(2, 10, 19)

    print("Costo básico:", f"${costo_basico:,.2f}")
    print("Costo con descuento:", f"${costo_descuento:,.2f}")
    print("Costo con descuento e impuesto:", f"${costo_completo:,.2f}")

    # ---------------------------------------------------------
    # OPERACIÓN 17: Demostrar polimorfismo.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 17: Demostración de polimorfismo")

    servicios = [sala, equipos, asesoria]

    for servicio in servicios:
        print(servicio.describir_servicio())

    # ---------------------------------------------------------
    # OPERACIÓN 18: Consultar el resumen general.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 18: Resumen general")

    print(sistema.mostrar_resumen())

    # ---------------------------------------------------------
    # OPERACIÓN 19: Consultar las reservas.
    # ---------------------------------------------------------
    print("\nOPERACIÓN 19: Listado de reservas")

    for informacion in sistema.listar_reservas():
        print("\n" + informacion)

    print("\n" + "=" * 65)
    print("       PRUEBAS DEL SISTEMA FINALIZADAS")
    print("=" * 65)


if __name__ == "__main__":

    try:
        ejecutar_pruebas()

    except Exception as error:
        logging.exception("Error inesperado en el programa principal.")
        print("\nSe presentó un error inesperado:", error)

    else:
        print("\nEjecución finalizada sin errores inesperados.")

    finally:
        print("Software FJ: finalización del programa.")
