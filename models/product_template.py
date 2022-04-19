# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = ['product.template']
    _description = 'Product Template'

    """format = fields.Char(string="format", required=True)
    reference = fields.Char(String='Référence', required=True)
    metrage = fields.Float(string="Métrage", default=0.0, required=True)
    choix = fields.Char(string="Choix", required=True)
    calibre = fields.Integer(string="Calibre")
    nuance = fields.Char(string="Nuance")
    line_production = fields.Char(string='Ligne de production', required=True)
    date_fabrication = fields.Char(string='Date de fabrication', required=True)
    unite_id = fields.Char(string='Lign production', required=True)
    tag = fields.Char(string='TAG', index=True, copy=False, required=True)"""

    format = fields.Many2one('format.list', string="Format")
    reference = fields.Char(string='Référence')
    metrage = fields.Float(string='Métrage')
    choix = fields.Many2one('choix.list', string="Choix")
    calibre = fields.Integer(string="Calibre")
    nuance = fields.Char(string="Nuance")
    line_production = fields.Many2one('res.users', string="Unité de production", domain=lambda self: [("groups_id", "=", self.env.ref("wayhouse.group_production_us").id)])
    date_fabrication = fields.Char(string='Date de fabrication')
    unite_id = fields.Char(string='Lign production')
    tag = fields.Char(string='TAG', index=True, copy=False, required=True)