# -*- coding: utf-8 -*-

from openerp import models, fields, api

class BodySite(models.Model):
    _name = "hc.res.body.site"
    _description = "Body Site"

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        required="True", 
        help="Patient.")
    identifier_ids = fields.One2many(
        comodel_name="hc.body.site.identifier", 
        inverse_name="body_site_id", 
        string="Identifiers", 
        help="Body Site identifier.")
    code_id = fields.Many2one(
        comodel_name="hc.vs.body.site.code", 
        string="Code", 
        help="Named anatomical location.")
    modifier_ids = fields.Many2many(
        comodel_name="hc.vs.body.site.relative.location", 
        string="Modifiers", 
        help="Modification to location code.")
    description = fields.Char(
        string="Description", 
        help="The Description of anatomical location.")
    image_ids = fields.One2many(
        comodel_name="hc.body.site.image", 
        inverse_name="body_site_id", 
        string="Images", 
        help="Attached images.")

class BodySiteIdentifier(models.Model):
    _name = "hc.body.site.identifier"
    _description = "Body Site Identifier"
    _inherit = ["hc.basic.association", "hc.identifier"]

    body_site_id = fields.Many2one(
        comodel_name="hc.res.body.site", 
        string="Body Site", 
        help="Body Site associated with this body site identifier." )

class BodySiteImage(models.Model):
    _name = "hc.body.site.image"
    _description = "Body Site Image"
    _inherit = ["hc.basic.association", "hc.attachment"]

    body_site_id = fields.Many2one(
        comodel_name="hc.res.body.site", 
        string="Body Site", 
        help="Body Site associated with this body site image." )

class BodySiteRelativeLocation(models.Model):
    _name = "hc.vs.body.site.relative.location"
    _description = "Body Site Relative Location"
    _inherit = ["hc.value.set.contains"]

class BodySiteCode(models.Model):
    _name = "hc.vs.body.site.code"
    _description = "Body Site Code"
    _inherit = ["hc.value.set.contains"]
