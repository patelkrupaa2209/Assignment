from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # point 3 - Copy all the tags from sale order to Delivery orders created from sale order.
    def _action_confirm(self):
        res = super()._action_confirm()
        for order in self:
            for picking in order.picking_ids:
                picking.tag_ids = order.tag_ids
        return res
