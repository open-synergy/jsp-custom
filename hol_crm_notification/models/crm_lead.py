from odoo import models, fields, api, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    # Form
    name = fields.Char(track_visibility='onchange')
    planned_revenue = fields.Float(track_visibility='onchange')
    probability = fields.Float(track_visibility='onchange')
    partner_id = fields.Many2one(track_visibility='onchange')
    email_from = fields.Char(track_visibility='onchange')
    phone = fields.Char(track_visibility='onchange')
    date_deadline = fields.Date(track_visibility='onchange')
    user_id = fields.Many2one(track_visibility='onchange')
    team_id = fields.Many2one(track_visibility='onchange')
    priority = fields.Selection(track_visibility='onchange')
    tag_ids = fields.Many2many(track_visibility='onchange')
    # Internal Notes
    description = fields.Text(track_visibility='onchange')
    # Contact Information
    partner_name = fields.Char(track_visibility='onchange')
    street = fields.Char(track_visibility='onchange')
    street2 = fields.Char(track_visibility='onchange')
    city = fields.Char(track_visibility='onchange')
    state_id = fields.Many2one(track_visibility='onchange')
    zip = fields.Char(track_visibility='onchange')
    country_id = fields.Many2one(track_visibility='onchange')
    website = fields.Char(track_visibility='onchange')
    contact_name = fields.Char(track_visibility='onchange')
    title = fields.Many2one(track_visibility='onchange')
    function = fields.Char(track_visibility='onchange')
    mobile = fields.Char(track_visibility='onchange')
    opt_out = fields.Boolean(track_visibility='onchange')
    # Marketing
    campaign_id = fields.Many2one(track_visibility='onchange')
    medium_id = fields.Many2one(track_visibility='onchange')
    source_id = fields.Many2one(track_visibility='onchange')
    # Misc
    day_open = fields.Float(track_visibility='onchange')
    day_closed = fields.Float(track_visibility='onchange')
    referred = fields.Char(track_visibility='onchange')
