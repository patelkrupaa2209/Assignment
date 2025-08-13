from odoo import models

class StockRule(models.Model):
    _inherit = 'stock.rule'

    # def _prepare_procurement_grouping_key(self, procurements):
    #     print("_prepare_procurement_grouping_key ***********************")
    #     """
    #     Extend the procurement grouping key to include product category,
    #     so that POs are split by product category.
    #     """
    #     key = super()._prepare_procurement_grouping_key(procurements)
    #     product = procurements[0].product_id
    #     category_id = product.categ_id.id or 0
    #     return key + (category_id,)
