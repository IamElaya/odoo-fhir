# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Timing(models.Model):    
    _name = "hc.timing"    
    _description = "Timing"        

    event_ids = fields.One2many(
        comodel_name="hc.timing.event", 
        inverse_name="timing_id", 
        string="Events", 
        help="When the event occurs.")                
    code = fields.Selection(
        string="Timing Code", 
        selection=[
            ("bid", "Bid"), 
            ("tid", "Tid"), 
            ("qid", "Qid"), 
            ("am", "Am"), 
            ("pm +", "Pm +")], 
        help="A code for the timing pattern.")                
    repeat_ids = fields.One2many(
        comodel_name="hc.timing.repeat", 
        inverse_name="timing_id", 
        string="Repeats", 
        help="When the event is to occur.")                

class TimingRepeat(models.Model):   
    _name = "hc.timing.repeat"  
    _description = "Timing Repeat"
    
    timing_id = fields.Many2one(
        comodel_name="hc.timing", 
        string="Timing", 
        required="True", 
        help="Timing associated with this repeat." )        
    bounds_type = fields.Selection(
        string="Bounds Type", 
        required="True", 
        selection=[
            ("duration", "Duration"), 
            ("range", "Range"), 
            ("period", "Period")], 
        help="Type of bounds.")       
    bounds_name = fields.Char(
        string="Bounds", 
        compute="compute_bounds_name", 
        help="Length/Range of lengths, or (Start and/or end) limit.")        
    bounds_duration = fields.Float(
        string="Bounds Duration", 
        help="Bounds length of time.")     
    bounds_duration_uom = fields.Selection(
        string="Bounds Duration UOM", 
        selection=[
            ("s", "S"), 
            ("min", "Min"), 
            ("h", "H"), 
            ("d", "D"), 
            ("wk", "Wk"), 
            ("mo", "Mo"), 
            ("a", "A")], 
        help="Unit of time (UCUM)")        
    bounds_range_low = fields.Float(
        string="Bounds Range Low", 
        help="Low limit of bounds range.")       
    bounds_range_high = fields.Float(
        string="Bounds Range High", 
        help="High limit of bounds range.")        
    bounds_period_start_date = fields.Datetime(
        string="Bounds Period Start Date", 
        help="Start of the bounds period.")       
    bounds_period_end_date = fields.Datetime(
        string="Bounds Period End Date", 
        help="End of the bounds period.")     
    count = fields.Integer(
        string="Count", 
        help="Number of times to repeat.")       
    count_max = fields.Integer(
        string="Count Max", 
        help="Maximum number of times to repeat.")       
    duration = fields.Float(
        string="Repeat Duration", 
        help="How long when it happens.")     
    duration_max = fields.Float(
        string="Duration Max", 
        help="How long when it happens (Max).")      
    duration_units = fields.Selection(
        string="Repeat Duration Units", 
        selection=[
            ("s", "S"), 
            ("min", "Min"), 
            ("h", "H"), 
            ("d", "D"), 
            ("wk", "Wk"), 
            ("mo", "Mo"), 
            ("a", "A")], 
        help="Unit of time (UCUM)")       
    frequency = fields.Integer(
        string="Frequency", 
        help="Event occurs frequency times per duration.")       
    frequency_max = fields.Integer(
        string="Frequency Max", 
        help="Event occurs frequency times per duration.")       
    period = fields.Float(
        string="Period", 
        help="Event occurs frequency times per period.")     
    period_max = fields.Float(
        string="Period Max", 
        help="Upper limit of period (3-4 hours).")       
    period_units = fields.Selection(
        string="Repeat Period Units", 
        selection=[
            ("s", "S"), 
            ("min", "Min"), 
            ("h", "H"), 
            ("d", "D"), 
            ("wk", "Wk"), 
            ("mo", "Mo"), 
            ("a", "A")], 
        help="Unit of time (UCUM)")       
    when_id = fields.Many2one(
        comodel_name="hc.vs.event.timing", 
        string="When", 
        help="Regular life events the event is tied to.")    
    offset = fields.Integer(
        string="Offset", 
        help="Minutes from event (before or after).")                      

class TimingEvent(models.Model):    
    _name = "hc.timing.event"    
    _description = "Timing Event"        

    timing_id = fields.Many2one(
        comodel_name="hc.timing", 
        string="Timing", 
        required="True", 
        help="Timing associated with this event.")    
    event_date = fields.Datetime(
        string="Event Date", 
        help="When the event occurs.")                

class EventTiming(models.Model):    
    _name = "hc.vs.event.timing"    
    _description = "Event Timing"        
    _inherit = ["hc.value.set.contains"]
