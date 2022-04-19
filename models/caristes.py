# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


# classes under  menu of modele

class CaristeList(models.Model):
    _name = 'cariste.list'

    name = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    tel = fields.Char(string='Téléphone')
    email = fields.Char(string='Email')