from odoo import models, fields, api


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    serial_number = fields.Char(
        string="Serial",
        related="production_id.lot_producing_id.name",
        store=True
    )

    piece_name = fields.Char(
        string="Peça",
        compute="_compute_piece",
        store=True
    )

    process_name = fields.Char(
        string="Processo",
        compute="_compute_piece",
        store=True
    )

    @api.depends('name')
    def _compute_piece(self):
        for rec in self:
            if rec.name and '-' in rec.name:
                parts = rec.name.split('-')
                rec.piece_name = parts[0].strip()
                rec.process_name = parts[1].strip()
            else:
                rec.piece_name = ''
                rec.process_name = rec.name
