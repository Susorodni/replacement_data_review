"""constants.py
"""
from enum import Enum
from typing import List

INVALID_VALUES = [
    "null",
    "<null>",
    "nan"
]

SUPPORTED_FILE_EXTENSIONS = [
    "*.xls",
    "*.xlsx",
    "*.xlsm",
    "*.xlsb",
    "*.odf",
    "*.ods",
    "*.odt",
    "*.csv"
]

SUPPORTED_FILETYPE_DROPDOWNS: List[tuple[str, str | list[str] | tuple[str, ...]]] = [
    ("All supported filetypes", SUPPORTED_FILE_EXTENSIONS),
    ("Excel Files", SUPPORTED_FILE_EXTENSIONS[0:-1]),
    ("CSV Files", SUPPORTED_FILE_EXTENSIONS[-1])
]

class Flag(Enum):
    FOLLOW_UP = object
    FIRE_LINE = object
    REVIEW_REPLACEMENT = object
    POTENTIALLY_ORIGINAL_COPPER = object
    INSPECTIONS_NEEDED = object
    GA_ROE_NEEDED = object
    NONE = object

FILTER_COLUMNS = [
    "Service Address",
    "Project Number",
    "Type of Service Replacement (Project Category)",
    "Type of Service Replacement Required",
    "Property Owner Name",
    "Property Owner Phone Number",
    "Additional Property Owner Phone",
    "Property Owner Email",
    "Property Owner Address"
    "City,State,ZIP",
    "Primary Tenant Name",
    "Primary Tenant Phone Number",
    "Primary Tenant Email",
    "Preferred Form of Contact",
    "Number of Building Tenants (Building Units)",
    "Contact Comments ( End Users) ( Name, Contact Info)",
    "Date of Initial Mailer",
    "Notes from Initial Mailer",
    "Date of Final Mailer",
    "Notes from Final Mailer",
    "Date of Contact 1st Attempt",
    "Notes and Contact with Whom 1st Attempt",
    "Date of Contact 2nd Attempt",
    "Notes and Contact with Whom 2nd Attempt",
    "Date of Contact 3rd Attempt",
    "Notes and Contact with Whom 3rd Attempt",
    "Date of Contact 4th Attempt",
    "Notes and Contact with Whom 4th Attempt",
    "Date of Contact 5th Attempt",
    "Notes and Contact with Whom 5th Attempt",
    "Public Material",
    "Public Date of Material Confirmation",
    "Public Diameter",
    "Public Depth at Tap (Inches)",
    "Public Data Source",
    "Private Material",
    "Private Date of Material Confirmation",
    "Private Diameter",
    "Right of Entry Date Signed by Owner",
    "Service Line Contractor Name",
    "Service Line Contractor Primary Contact",
    "Inspector Name",
    "Extent of Replacement",
    "Date of New Public Service Main to Right of Way",
    "New Public Service Tap Size",
    "New Tap House Side Measurement (ft)",
    "New Tap House Side Direction",
    "New Tap House Side Street Centerline",
    "New Tap Cross Street Measurement (ft)",
    "New Tap Cross Street Direction",
    "New Tap Cross Street Street Centerline",	
    "New Public Service Line Diameter",	
    "New Public Service Line Material",	
    "New Public Service Line Length (ft)",	
    "Reconnection Point",	
    "Reconnection Point Comments ( i.e. Shared Service, T Fitting, N/A)",	
    "Reconnection Point House Side Measurement (ft)",	
    "Reconnection Point House Side Direction",	
    "Reconnection Point House Side StreetCenterline",	
    "Reconnection Point Cross Street Measurement (ft)",	
    "Reconnection Point Cross Street Direction",	
    "Reconnection Point Cross Street StreetCenterline",	
    "Date of New Private Service Right of Way to Building",	
    "New Private Service Line Material",	
    "New Private Service Line Diameter",	
    "New Private Service Line Length	Meter Moved Outside to new Pit ?",
    "Date of New Meter Request",	
    "Any Lead or Galvanized Requiring Replacement Remaining ?",
    "Where is Lead Remaining ?",
    "Retired Service Date",
    "Orginal Service Installation Year",	
    "Retired Service Tap Size",
    "Retired Public Material",	
    "Retired Private Material",	
    "Retired Service Diameter",
    "Other Retired Public Material",
    "Other Private Retired Material",
    "How was Public Material Retired?",
    "Retired Service Length (Right-of-Way Only)",
    "Construction Comments",
    "Map Indy Year Built",
    "Private Property Access",
    "Grantor Access Name Construction",
    "Grantor Access Name Preconstruction",
    "Grantor Access Date Preconstruction",
    "Meter Location",
    "Meter Location Notes",
    "Name of Decliner"
]