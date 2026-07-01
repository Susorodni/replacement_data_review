"""exceptions.py

This module contains all custom exceptions used.
"""

class NoFlagApplicationException(Exception):
    """Raised when no flag category could be applied.

    Args:
        Exception (Exception): base Exception
    """
    def __init__(self, service_address: str, message: str | None = None):
        self.service_address = service_address
        
        if message is None:
            message = (
                f"No flag category could be applied to service address {self.service_address}."
            )
            
        super().__init__(message)

class InvalidDiameterException(Exception):
    """Raised when a string value from a DataFrame contains a complex integer
    or fraction integer meant to convey a length in inches that could not 
    successfully be converted.

    Args:
        Exception (Exception): base exception type
    """
    def __init__(self, diameter: str, message: str | None = None):
        self.diameter = diameter
        if message is None:
            message = (
                f"An imported diameter value ({diameter}) could not be successfully converted."
            )
        super().__init__(message)

