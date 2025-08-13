from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    # Point 6 - Manufacturing orders created from sale order should not allowed to change the qty after the confirmation.
    def write(self, vals):
        if 'move_raw_ids' in vals:
            for record in self:
                if (
                    record.state not in ['draft', 'cancel']
                    and record.origin
                    and record.origin.startswith('S')
                ):
                    for command in vals['move_raw_ids']:
                        if (
                            len(command) == 3
                            and isinstance(command[2], dict)
                            and 'quantity' in command[2]
                        ):
                            new_qty = command[2]['quantity']
                            existing_qty = sum(record.move_raw_ids.mapped('product_uom_qty'))
                            if existing_qty != new_qty:
                                raise UserError(_("You cannot change Quantity on a Manufacturing Order created from a Sale Order after confirmation."))
        return super().write(vals)
