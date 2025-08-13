from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    x_category_id = fields.Many2one('product.category', string='Product Category')


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _make_po_get_domain(self, company_id, values, partner):
        """Add product category to PO grouping logic"""
        domain = super()._make_po_get_domain(company_id, values, partner)

        product = values.get('product_id')
        if product:
            domain += [('x_category_id', '=', product.categ_id.id)]
        return domain

    def _prepare_purchase_order(self, company_id, origins, values_list):
        """Add category field when creating the PO"""
        purchase_order_vals = super()._prepare_purchase_order(company_id, origins, values_list)

        if values_list and isinstance(values_list, list):
            first_vals = values_list[0]
            product = first_vals.get('product_id')
            if product:
                purchase_order_vals['x_category_id'] = product.categ_id.id

        return purchase_order_vals
