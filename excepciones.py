
"""
Módulo de excepciones personalizadas del sistema Software FJ.
Permite identificar y controlar errores específicos de la aplicación.
"""


class ErrorSoftwareFJ(Exception):
    """Excepción base para los errores del sistema."""
    pass


class DatosInvalidosError(ErrorSoftwareFJ):
    """Se genera cuando los datos ingresados no son válidos."""
    pass


class ClienteNoEncontradoError(ErrorSoftwareFJ):
    """Se genera cuando un cliente no existe en el sistema."""
    pass


class ClienteDuplicadoError(ErrorSoftwareFJ):
    """Se genera cuando se intenta registrar un cliente repetido."""
    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Se genera cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(ErrorSoftwareFJ):
    """Se genera cuando una reserva contiene datos incorrectos."""
    pass


class ReservaNoEncontradaError(ErrorSoftwareFJ):
    """Se genera cuando no se encuentra una reserva."""
    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Se genera cuando se intenta realizar una operación no permitida."""
    pass


class CalculoInvalidoError(ErrorSoftwareFJ):
    """Se genera cuando un cálculo produce un resultado inconsistente."""
    pass


class ParametroFaltanteError(ErrorSoftwareFJ):
    """Se genera cuando falta un parámetro obligatorio."""
    pass
