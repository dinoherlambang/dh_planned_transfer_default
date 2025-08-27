from odoo import models, fields, api
from ast import literal_eval


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    default_planned_transfer = fields.Boolean(
        string='Default to Planned Transfer',
        default=False,
        help='If checked, new transfers of this type will default to planned transfer mode instead of immediate transfer. '
             'Planned transfers show the Demand column which is required for serial number imports and better inventory control. '
             'Immediate transfers skip the demand step and go directly to done quantities.'
    )

    def _get_action(self, action_xmlid):
        """Override to use operation type specific default transfer mode"""
        action = self.env.ref(action_xmlid).read()[0]
        if self:
            action['display_name'] = self.display_name

        # Check if this operation type should default to planned transfer
        if self.default_planned_transfer:
            default_immediate_tranfer = False
        else:
            # Use original logic: check system parameter
            default_immediate_tranfer = True
            if self.env['ir.config_parameter'].sudo().get_param('stock.no_default_immediate_tranfer'):
                default_immediate_tranfer = False

        context = {
            'search_default_picking_type_id': [self.id],
            'default_picking_type_id': self.id,
            'default_immediate_transfer': default_immediate_tranfer,
            'default_company_id': self.company_id.id,
        }

        action_context = literal_eval(action['context'])
        context = {**action_context, **context}
        action['context'] = context

        return action
