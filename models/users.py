from odoo import fields, models, api


class User(models.Model):
    _inherit = 'res.users'

    tag_ids = fields.Many2many('product.tag', string='Tag Pyme')

    @api.constrains('share')
    def _updateUser(self):
        for record in self:
            if not record.share:
                record.env.cr.execute('update res_partner set create_uid=%s where id = %s', [record.id, record.partner_id.id])
                record.env['res.partner'].invalidate_cache()






