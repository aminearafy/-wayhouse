# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


# classes under  menu of modele

class ChoixList(models.Model):
    _name = 'choix.list'

    name = fields.Char(String='Choix',required=True)
    nuance_calibre = fields.Boolean(string='Nuance et calibre en lecture seule ?')