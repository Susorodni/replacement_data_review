import re
from fractions import Fraction
import math
from replacement_data_review.exceptions import InvalidDiameterException
from replacement_data_review.config import INVALID_VALUES

def parse_inches(value) -> float:
    """
    Convert inch values to float.

    Valid examples:
        '1 1/2"'  -> 1.5
        '2"'      -> 2.0
        '3/4"'    -> 0.75
        '0.75'    -> 0.75
        '1.25'    -> 1.25
        '  1 1/2" ' -> 1.5

    Invalid examples:
        None      -> -1.0
        ''
        'nan'
        'abc'
        
    Args:
        value (str): the raw string value of the inch length from the file.

    Raises:
        ValueError: if invalid value type is given as an argument.
        ValueError: if the format of the inch increment is not correct.
            (needs to be in whole numbers, fractions, and with an " marking).

    Returns:
        float: the length in inches
    """

    # Handle None
    if value is None:
        return -1.0

    # Handle numeric inputs directly
    if isinstance(value, (int, float)):
        if isinstance(value, float) and math.isnan(value):
            return -1.0
        return float(value)

    # Convert to string and normalize
    s = str(value).strip()

    if not s:
        return -1.0

    if s.lower() in {"nan", "none", "null", "<null>"}:
        return -1.0

    # Remove inch mark if present
    s = s.rstrip('"').strip()

    try:
        # Mixed fraction: e.g. "1 1/2"
        if re.fullmatch(r"\d+\s+\d+/\d+", s):
            whole, frac = s.split()
            return float(int(whole) + Fraction(frac))

        # Simple fraction: e.g. "3/4"
        if re.fullmatch(r"\d+/\d+", s):
            return float(Fraction(s))

        # Integer or decimal
        if re.fullmatch(r"\d+(\.\d+)?", s):
            return float(s)

    except Exception as e:
        raise InvalidDiameterException(value) from e

    return -1.0

def address_sort_key(asset: Asset) -> tuple[str, int]:
    """

    Handle function for pandas to sort a dataframe by the
    alphabetical order of street names, then by street numbers.

    Args:
        asset (Asset): the asset to be checked when iterated through
            the handle function.

    Returns:
        tuple[str, int]: the address and order of the asset, respectively.
    """
    address = asset.service_address.strip()

    # Match: number + rest of address
    match = re.match(r"(\d+)\s+(.*)", address)

    if match:
        number = int(match.group(1))
        street_name = match.group(2).strip()
    else:
        # fallback if format is unexpected
        number = 0  # push to end
        street_name = address

    return (street_name, number)

def parse_map_indy(value: str) -> int:
    """Checks the MapIndy home construction value and returns the integer
    equivalent.
    
    - if "XXXX" -> returns -1 for explicitly missing year
    - if an invalid value (nan, null, "") -> returns 0 for implicitly missing year
    - else -> returns the integer equivalent of the string

    Args:
        value (str): the MapIndy string value to be converted

    Returns:
        int: the integer representation of the home construction year
    """
    v = re.sub(r"\s+", "", value).lower()

    if v == "xxxx":
        return -1
    elif is_invalid_value(v):
        return 0
    else:
        return int(v)

def is_invalid_value(val: str) -> bool:
    """Helper function to determine if a string is an invalid value

    Args:
        val (str): string to compare

    Returns:
        bool: whether or not the given string is an invalid value.
    """
    return val.lower() in INVALID_VALUES