from odoo import models, api, _
from odoo.exceptions import ValidationError

class ProductCategory(models.Model):
    _inherit = 'product.category'

    # point 9 - Category should have unique name.
    @api.model
    def create(self, vals):
        if 'name' in vals:
            existing = self.search([('name', '=', vals['name'])], limit=1)
            if existing:
                raise ValidationError(_("Category name must be unique."))
        return super().create(vals)

    def write(self, vals):
        if 'name' in vals:
            for rec in self:
                existing = self.search([
                    ('name', '=', vals['name']),
                    ('id', '!=', rec.id)
                ], limit=1)
                if existing:
                    raise ValidationError(_("Category name must be unique."))
        return super().write(vals)
