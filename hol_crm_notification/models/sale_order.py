from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, values):
        res = super(SaleOrder, self).create(values)
        crm = self.env['crm.lead'].search([('id', '=', res.opportunity_id.id)])
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        body = ""
        if crm:
            url = str(base_url) + '/web#id=%s&view_type=form&model=sale.order' % (res.id)
            body += "<ul><li>Quotation Created: <a href=%s>%s</a></li></ul>" % (url, res.name)
            crm.message_post(body=body)
        return res
