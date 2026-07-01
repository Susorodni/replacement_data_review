"""asset.py

Class structure of an asset

"""
from dataclasses import dataclass
from replacement_data_review.config import Flag

@dataclass(frozen=True)
class ContactAttempt:
    contact_date: str | None = None
    notes: str | None = None

@dataclass
class Asset:
    """Dataclass with all values needed for a given service address.
    """
    service_address: str
    project_number: str
    service_replacement_project_category: str
    service_replacement_required: str
    property_owner_name: str
    property_owner_phone: str
    property_owner_phone_alt: str
    property_owner_email: str
    property_owner_address: str
    city_state_zip: str
    primary_tenant_name: str
    primary_tenant_phone: str
    primary_tenant_email: str
    preferred_contact_method: str
    building_tenant_count: str
    contact_comments: str
    initial_mailer_date: str
    initial_mailer_notes: str
    final_mailer_date: str
    final_mailer_notes: str
    contact_attempts: list[ContactAttempt]
    public_material: str
    public_material_confirm_date: str
    public_diameter: float
    public_tap_depth_in: str
    public_data_source: str
    private_material: str
    private_material_confirm_date: str
    private_diameter: float
    roe_signed_date: str
    contractor_name: str
    contractor_primary_contact: str
    inspector_name: str
    replacement_extent: str
    new_public_service_row_date: str
    new_public_tap_size: str
    new_tap_house_side_ft: str
    new_tap_house_dir: str
    new_tap_house_centerline: str
    new_tap_cross_st_ft: str
    new_tap_cross_st_dir: str
    new_tap_cross_st_centerline: str
    new_public_line_diameter: str
    new_public_line_material: str
    new_public_line_length_ft: str
    reconnection_point: str
    reconnection_comments: str
    reconnection_house_side_ft: str
    reconnection_house_side_dir: str
    reconnection_house_centerline: str
    reconnection_cross_st_ft: str
    reconnection_cross_st_dir: str
    reconnection_cross_st_centerline: str
    new_private_service_date: str
    new_private_line_material: str
    new_private_line_diameter: str
    new_private_line_length: str
    meter_moved_to_pit: str
    new_meter_request_date: str
    lead_remaining: str
    lead_remaining_location: str
    retired_service_date: str
    original_install_year: str
    retired_tap_size: str
    retired_public_material: str
    retired_private_material: str
    retired_service_diameter: str
    other_retired_public_material: str
    other_retired_private_material: str
    public_material_retirement_method: str
    retired_service_length_row_ft: str
    construction_comments: str
    map_indy_year_built: int
    private_property_access: str
    grantor_access_name_construction: str
    grantor_access_name_precon: str
    grantor_access_date_precon: str
    meter_location: str
    meter_location_notes: str
    decliner_name: str
    flags: list[Flag]

