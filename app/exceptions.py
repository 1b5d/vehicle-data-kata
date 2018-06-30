class VehicleDataError(BaseException):
    """
    Base exception of all app custom exceptions.
    """
    pass


class DataReadingError(VehicleDataError):
    """
    An error that can happen during data input.
    """
    pass


class FormatNotSupportedError(VehicleDataError):
    """
    An error that can happen if wrong format is selected.
    """
    pass
