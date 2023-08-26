from odoo import api, fields, models


class StockMove(models.Model):

    _inherit = "stock.move"
    _name = "stock.move"

    qty_not_reserved = fields.Float(
        string="Not Reserved",
        compute="_compute_available_qty",
        store=True,
        readonly=True,
    )

    @api.depends("product_id", "state")
    def _compute_available_qty(self):
        for record in self:
            if record.product_id and record.state != "done":
                actual_qty = record.product_id.with_context(
                    {"location": record.location_id.id}
                ).qty_available
                outgoing_qty = record.product_id.with_context(
                    {"location": record.location_id.id}
                ).outgoing_qty
                record.qty_not_reserved = actual_qty - outgoing_qty

class StockMoveLine(models.Model):

    _inherit = "stock.move.line"
    _name = "stock.move.line"

    qty_not_reserved = fields.Float(
        string="Not Reserved",
        compute="_compute_available_qty",
        store=True,
        readonly=True,
    )

    @api.depends("product_id","lot_id")
    def _compute_available_qty(self):
        for record in self:
            if record.product_id and record.move_id.state != "done":
                id_lot = record.lot_id.id if record.lot_id else None
                actual_qty = record.product_id.with_context(
                    {"location": record.location_id.id, "lot_id": id_lot}
                ).qty_available
                outgoing_qty = record.product_id.with_context(
                    {"location": record.location_id.id, "lot_id": id_lot}
                ).outgoing_qty
                record.qty_not_reserved = actual_qty - outgoing_qty
