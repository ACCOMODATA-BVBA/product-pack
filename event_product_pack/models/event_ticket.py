from odoo import models, fields, api


class EventTicket(models.Model):
    _inherit = "event.event.ticket"

    total_pack_price = fields.Float('Total Pack Price',
                                    compute='_compute_total_pack_price', digits='Product Price', store=True)
    pack_ok = fields.Boolean(related='product_id.pack_ok')

    @api.depends('product_id',
                 'product_id.lst_price',
                 'product_id.pack_line_ids',
                 'product_id.pack_line_ids.product_id.lst_price',
                 'product_id.pack_line_ids.quantity')
    def _compute_total_pack_price(self):
        for rec in self:
            rec.total_pack_price = rec.product_id.lst_price + sum([pack.product_id.lst_price * pack.quantity for pack in rec.product_id.pack_line_ids])
