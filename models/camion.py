# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


# classes under  menu of modele

class CamionList(models.Model):
    _name = 'camion.list'

    name = fields.Char(string='Matricule', required=True)
    marque = fields.Char(string='Marque', required=True)