from odoo import api, models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Point 1 - Partner should be search on the Ref field from all Many2one widgets.
    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if not args:
            args = []
        if name:
            partners = self.search([
                '|', ('name', operator, name),
                     ('ref', operator, name)
            ] + args, limit=limit)
        else:
            partners = self.search(args, limit=limit)
        return partners.name_get()

    # Point 2 - In Many2one field of partner, it should include Ref in the format PARTNER NAME [REF].
    def name_get(self):
        result = []
        for partner in self:
            name = partner.name or ''
            if partner.ref:
                name = f"{name} [{partner.ref}]"
            result.append((partner.id, name))
        return result
