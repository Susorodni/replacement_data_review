"""asset_manager.py
"""
import re
import pandas as pd
from replacement_data_review.models.asset import Asset, ContactAttempt
from replacement_data_review.util import parse_inches, parse_map_indy
from replacement_data_review.config import Flag, FILTER_COLUMNS
from replacement_data_review.exceptions import NoFlagApplicationException


def build_assets(df: pd.DataFrame) -> list[Asset]:
    df = df.filter(FILTER_COLUMNS, axis=1)
    
    records = df.to_dict("records")
    
    assets = []
    
    for r in records:
        try:
            asset = Asset(
                service_address=str(r.get("Service Address")),
                project_number=str(r.get("Project Number")),
                service_replacement_project_category=str(r.get("Type of Service Replacement (Project Category)")),
                service_replacement_required=str(r.get("Type of Service Replacement Required")),
                property_owner_name=str(r.get("Property Owner Name")),
                property_owner_phone=str(r.get("Property Owner Phone Number")),
                property_owner_phone_alt=str(r.get("Additional Property Owner Phone")),
                property_owner_email=str(r.get("Property Owner Email")),
                property_owner_address=str(r.get("Property Owner Address")),
                city_state_zip=str(r.get("City,State,ZIP")),
                primary_tenant_name=str(r.get("Primary Tenant Name")),
                primary_tenant_phone=str(r.get("Primary Tenant Phone Number")),
                primary_tenant_email=str(r.get("Primary Tenant Email")),
                preferred_contact_method=str(r.get("Preferred Form of Contact")),
                building_tenant_count=str(r.get("Number of Building Tenants (Building Units)")),
                contact_comments=str(r.get("Contact Comments ( End Users) ( Name, Contact Info)")),
                initial_mailer_date=str(r.get("Date of Initial Mailer")),
                initial_mailer_notes=str(r.get("Notes from Initial Mailer")),
                final_mailer_date=str(r.get("Date of Final Mailer")),
                final_mailer_notes=str(r.get("Notes from Final Mailer")),
                contact_attempts=populate_contact_attempts(r),
                public_material=str(r.get("Public Material")),
                public_material_confirm_date=str(r.get("Public Date of Material Confirmation")),
                public_diameter=parse_inches(r.get("Public Diameter")),
                public_tap_depth_in=str(r.get("Public Depth at Tap (Inches)")),
                public_data_source=str(r.get("Public Data Source")),
                private_material=str(r.get("Private Material")),
                private_material_confirm_date=str(r.get("Private Date of Material Confirmation")),
                private_diameter=parse_inches(r.get("Private Diameter")),
                roe_signed_date=str(r.get("Right of Entry Date Signed by Owner")),
                contractor_name=str(r.get("Service Line Contractor Name")),
                contractor_primary_contact=str(r.get("Service Line Contractor Primary Contact")),
                inspector_name=str(r.get("Inspector Name")),
                replacement_extent=str(r.get("Extent of Replacement")),
                new_public_service_row_date=str(r.get("Date of New Public Service Main to Right of Way")),
                new_public_tap_size=str(r.get("New Public Service Tap Size")),
                new_tap_house_side_ft=str(r.get("New Tap House Side Measurement (ft)")),
                new_tap_house_dir=str(r.get("New Tap House Side Direction")),
                new_tap_house_centerline=str(r.get("New Tap House Side Street Centerline")),
                new_tap_cross_st_ft=str(r.get("New Tap Cross Street Measurement (ft)")),
                new_tap_cross_st_dir=str(r.get("New Tap Cross Street Direction")),
                new_tap_cross_st_centerline=str(r.get("New Tap Cross Street Street Centerline")),
                new_public_line_diameter=str(r.get("New Public Service Line Diameter")),
                new_public_line_material=str(r.get("New Public Service Line Material")),
                new_public_line_length_ft=str(r.get("New Public Service Line Length (ft)")),
                reconnection_point=str(r.get("Reconnection Point")),
                reconnection_comments=str(r.get("Reconnection Point Comments ( i.e. Shared Service, T Fitting, N/A)")),
                reconnection_house_side_ft=str(r.get("Reconnection Point House Side Measurement (ft)")),
                reconnection_house_side_dir=str(r.get("Reconnection Point House Side Direction")),
                reconnection_house_centerline=str(r.get("Reconnection Point House Side StreetCenterline")),
                reconnection_cross_st_ft=str(r.get("Reconnection Point Cross Street Measurement (ft)")),
                reconnection_cross_st_dir=str(r.get("Reconnection Point Cross Street Direction")),
                reconnection_cross_st_centerline=str(r.get("Reconnection Point Cross Street StreetCenterline")),
                new_private_service_date=str(r.get("Date of New Private Service Right of Way to Building")),
                new_private_line_material=str(r.get("New Private Service Line Material")),
                new_private_line_diameter=str(r.get("New Private Service Line Diameter")),
                new_private_line_length=str(r.get("New Private Service Line Length")),
                meter_moved_to_pit=str(r.get("Meter Moved Outside to new Pit ?")),
                new_meter_request_date=str(r.get("Date of New Meter Request")),
                lead_remaining=str(r.get("Any Lead or Galvanized Requiring Replacement Remaining ?")),
                lead_remaining_location=str(r.get("Where is Lead Remaining ?")),
                retired_service_date=str(r.get("Retired Service Date")),
                original_install_year=str(r.get("Orginal Service Installation Year")),
                retired_tap_size=str(r.get("Retired Service Tap Size")),
                retired_public_material=str(r.get("Retired Public Material")),
                retired_private_material=str(r.get("Retired Private Material")),
                retired_service_diameter=str(r.get("Retired Service Diameter")),
                other_retired_public_material=str(r.get("Other Retired Public Material")),
                other_retired_private_material=str(r.get("Other Private Retired Material")),
                public_material_retirement_method=str(r.get("How was Public Material Retired?")),
                retired_service_length_row_ft=str(r.get("Retired Service Length (Right-of-Way Only)")),
                construction_comments=str(r.get("Construction Comments")),
                map_indy_year_built=parse_map_indy(str(r.get("Map Indy Year Built"))),
                private_property_access=str(r.get("Private Property Access")),
                grantor_access_name_construction=str(r.get("Grantor Access Name Construction")),
                grantor_access_name_precon=str(r.get("Grantor Access Name Preconstruction")),
                grantor_access_date_precon=str(r.get("Grantor Access Date Preconstruction")),
                meter_location=str(r.get("Meter Location")),
                meter_location_notes=str(r.get("Meter Location Notes")),
                decliner_name=str(r.get("Name of Decliner")),
                flags=list()
                )
            assets.append(asset)
        except Exception as e:
            print(f"Error for value {r}")
            raise e
        
    return assets

def populate_contact_attempts(r: dict) -> list[ContactAttempt]:
    
    ret_list = []
    
    for i in range(4):
        
        match i + 1:
            case 1:
                prefix = "st"
            case 2:
                prefix = "nd"
            case 3:
                prefix = "rd"
            case _:
                prefix = "th"
        
        ret_list.append(ContactAttempt(
            contact_date=r.get(f"Date of Contact {i + 1}{prefix} Attempt"),
            notes=r.get(f"Notes and Contact with Whom {i + 1}{prefix} Attempt")
        ))
    
    return ret_list