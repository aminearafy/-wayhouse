# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


# classes under  menu of modele

class FormatList(models.Model):
    _name = 'format.list'

    name = fields.Char(String='Format',required=True)