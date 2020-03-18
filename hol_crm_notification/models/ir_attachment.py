from odoo import models, fields, api, _


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def create(self, values):
        res = super(IrAttachment, self).create(values)
        if res.res_model == 'crm.lead':
            crm = self.env[res.res_model].search([('id', '=', res.res_id)])
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            body = ""
            if crm:
                if res.index_content == 'image':
                    url = str(base_url) + '/web/image/%s' % (res.id)
                    body += "<ul><li>Image: <a href=%s/?download=1>%s</a></li>" % (url, res.name)
                    body += "<a href=%s><img src=%s/150x150></img></a><ul>" % (url, url)
                else:
                    url = str(base_url) + '/web/content/%s' % (res.id)
                    body += "<ul><li>Attachment:</li>"
                    body += "<a href=%s>%s</a></ul>" % (url, res.name)
                crm.message_post(body=body)
        return res
