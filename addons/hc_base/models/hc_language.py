# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Language(models.Model): 
    _name = "hc.vs.language"    
    _description = "Language"
    _inherit = ["hc.value.set.contains"]
    _inherits = {"res.lang": "language_id"}

    language_id = fields.Many2one(
        comodel_name="res.lang", 
        string="Language",
        required=True,
        ondelete="restrict", 
        help="Human Language based on ISO-639.")

# External Reference

class lang(models.Model):
    _inherit = ["res.lang"]

<<<<<<< HEAD
    iso3_code_id = fields.Many2one(
        comodel_name="hc.vs.language.iso3.code", 
=======
    iso3_code = fields.Char(
>>>>>>> upstream/master
        string="ISO3 code",
        help="A 3-character representation of the ISO language code.")
    country_id = fields.Many2one(
        comodel_name="res.country", 
        string="Country",
        help="Country that the ISO language belongs to.")
    language_id = fields.Many2one(
        comodel_name="hc.vs.language.name", 
        string="Language",
        help="Human Language based on ISO-639.")

class LanguageIso3Code(models.Model):
    _name = "hc.vs.language.iso3.code"
    _description = "Language ISO3 code"
    _inherit = ["hc.value.set.contains"]

    iso3_code_id = fields.Many2one(
        comodel_name="hc.vs.language.iso3.code", 
        string="ISO3 code",
        help="A 3-character representation of the ISO language code.")
    language_id = fields.Many2one(
        comodel_name="hc.vs.language.name", 
        string="Language",
        help="Human Language based on ISO-639.")

class LanguageName(models.Model):
    _name = "hc.vs.language.name"
    _description = "Language name"
    _inherit = ["hc.value.set.contains"]

    language_id = fields.Many2one(
        comodel_name="hc.vs.language.name", 
        string="Language",
        help="Human Language based on ISO-639.")

class LanguageProficiency(models.Model): 
    _name = "hc.vs.language.proficiency"   
    _description = "Language Proficiency"
    _inherit = ["hc.value.set.contains"]

    parent_id = fields.Many2one(
        comodel_name="hc.vs.language.proficiency", 
        string="Parent",
        help="Parent Concept.")

class LanguageSkill(models.Model): 
    _name = "hc.vs.language.skill"   
    _description = "Language Skill"
<<<<<<< HEAD
    _inherit = ["hc.value.set.contains"]

    parent_id = fields.Many2one(
        comodel_name="hc.vs.language.skill", 
        string="Parent",
        help="Parent Concept.")

# External Reference

# class lang(models.Model):
#     _inherit = ["res.lang"]

#     iso3_code = fields.Char(
#         string="ISO3 code",
#         size=16, 
#         help="A 3-character representation of the ISO language code.")

#     country_id = fields.Many2one(
#         comodel_name="res.country", 
#         string="Country", 
#         help="Country that the ISO language belongs to.")

=======
    _inherit = ["hc.value.set.contains"]
>>>>>>> upstream/master
