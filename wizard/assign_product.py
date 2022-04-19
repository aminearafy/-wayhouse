# -*- coding: utf-8 -*-

from odoo import models, fields


class AssignProduct(models.TransientModel):
    _name = 'assign.product'
    _inherit = 'create.product.qrcode'
    _description = 'Assign Product'

    qrcode = fields.Char(string='Qrcode', required=True)

    tag = fields.Char(string='Tag', required=True)

    def action_assign_product(self):
        print('assign product')
