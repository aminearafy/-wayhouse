# -*- coding: utf-8 -*-

from odoo import models, fields


class ProdIndividual(models.Model):
    _inherits = 'res.users'

    up_user = fields.Boolean(string="Cet utilisateur est une unité de production")