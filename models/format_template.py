# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


# classes under  menu of modele

class ArticleFormat(models.Model):
    _name = 'article.format'

    name = fields.Char(compute="_compute_concaten")
    format_id = fields.Many2one('format.list', string="Format", required=True)
    reference = fields.Char(string='Référence', required=True)
    palette = fields.Float(string='Palette', default = 0.0, required=True)
    caisse = fields.Float(string='Caisse (m²)', default = 0.0, required=True)

    @api.depends("reference")
    def _compute_concaten(self):
        for record in self:
            record.name = record.reference