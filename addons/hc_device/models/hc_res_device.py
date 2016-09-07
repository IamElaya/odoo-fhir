# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Device(models.Model): 
    _name = "hc.res.device" 
    _description = "Device"

    identifier_ids = fields.One2many(
        comodel_name="hc.device.identifier", 
        inverse_name="device_id", 
        string="Identifiers", 
        help="Instance id from manufacturer, owner, and others.")     
    udi_carrier_id = fields.Many2one(
        comodel_name="hc.device.identifier", 
        string="UDI Carrier", 
        help="Unique Device Identifier (UDI) Barcode string.")      
    status = fields.Selection(
        string="Device Status", 
        selection=[
            ("available", "Available"), 
            ("not-available", "Not-Available"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="Status of the Device availability.")      
    type_id = fields.Many2one(
        comodel_name="hc.vs.device.type", 
        string="Type", 
        required="True", 
        help="What kind of device this is.")        
    lot_number = fields.Char(
        string="Lot Number", 
        help="Lot number of manufacture.")        
    manufacturer_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Manufacturer", 
        help="Name of device manufacturer.")       
    manufacture_date = fields.Datetime(
        string="Manufacture Date", 
        help="Manufacture date.")     
    expiration_date = fields.Datetime(
        string="Expiration Date", 
        help="Date and time of expiry of this device (if applicable).")      
    model = fields.Char(
        string="Model", 
        help="Model id assigned by the manufacturer.")      
    version = fields.Char(
        string="Version", 
        help="Version number (i.e. software).")     
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="If the resource is affixed to a person.")       
    owner_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Owner Organization", 
        help="Organization responsible for device.")       
    contact_contact_point_ids = fields.One2many(
        comodel_name="hc.device.telecom", 
        inverse_name="device_id", 
        string="Contact Contact Points", 
        help="Details for human/organization for support.")        
    location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Location", 
        help="Where the resource is found.")       
    url = fields.Char(
        string="UDI", 
        help="Network address to contact device.")      
    note_ids = fields.One2many(
        comodel_name="hc.device.note", 
        inverse_name="device_id", 
        string="Notes", 
        help="Device notes and comments.")                       

class DeviceIdentifier(models.Model):    
    _name = "hc.device.identifier"    
    _description = "Device Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

    device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Device", 
        help="Device associated with this device identifier.")                    

class DeviceTelecom(models.Model):    
    _name = "hc.device.telecom"    
    _description = "Device Telecom"        
    _inherit = ["hc.telecom.contact.point"]    
    _inherits = {"hc.telecom": "telecom_id"}

    telecom_id = fields.Many2one(
        comodel_name="hc.telecom", 
        string="Telecom", 
        required="True", 
        ondelete="restrict", 
        help="Telecom associated with this device telecom.")                    
    device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Device", 
        help="Device associated with this device telecom.")                    

class DeviceNote(models.Model):    
    _name = "hc.device.note"    
    _description = "Device Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]
    
    device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Device", 
        help="Device associated with this device telecom.")                    

class DeviceType(models.Model): 
    _name = "hc.vs.device.type" 
    _description = "Device Type"        
    _inherit = ["hc.value.set.contains"]
