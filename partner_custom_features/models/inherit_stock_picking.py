from odoo import models, fields, api
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    tag_ids = fields.Many2many('crm.tag', string='Tags') # Point 3
    copy_text = fields.Char(string='Copy Text')  # Point 10
    is_notified = fields.Boolean(string="Salesperson Notified", default=False) # Point 8

    # point 3 - Copy all the tags from sale order to Delivery orders created from sale order. (for existing records)
    @api.model
    def cron_copy_sale_order_tags(self):
        pickings = self.search([
            ('origin', '!=', False),
            ('tag_ids', '=', False),
        ])
        for picking in pickings:
            sale = self.env['sale.order'].search([('name', '=', picking.origin)], limit=1)
            if sale and sale.tag_ids:
                picking.tag_ids = sale.tag_ids

    # point 8 - Please add the automated action for sending mail to responsible(salesperson) of sale order when the delivery order is delivered.
    @api.model
    def cron_notify_salesperson_delivery_done(self):
        deliveries = self.search([
            ('state', '=', 'done'),
            ('picking_type_id.code', '=', 'outgoing'),
            ('is_notified', '=', False),
            ('origin', '!=', False)
        ])
        for delivery in deliveries:
            sale_order = self.env['sale.order'].search([('name', '=', delivery.origin)], limit=1)
            if sale_order and sale_order.user_id.email:
                template = self.env.ref('partner_custom_features.delivery_done_email_template')
                template.send_mail(delivery.id, force_send=True)
                delivery.is_notified = True
