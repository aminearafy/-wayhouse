# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime, timedelta


class CreateProductQrcode(models.TransientModel):
    _name = 'create.product.qrcode'
    _description = 'Create Product QR Code'

    """reference = fields.Selection(string='Reference',
                                 selection=[('MADRID 03 BEIGE 30', 'MADRID 03 BEIGE 30'),
                                            ('TANGER PLT HA 30M3', 'TANGER PLT HA 30M3'),
                                            ('CASTOR MARRO 30 M3', 'CASTOR MARRO 30 M3'),
                                            ('PERLA MARFIL 30 M3', 'PERLA MARFIL 30 M3'),
                                            ('TANGER 30 M3', 'TANGER 30 M3'),
                                            ('MADRID 04GRI CLR30', 'MADRID 04GRI CLR30')],
                                 required=True)

    caliber = fields.Selection(string='Calibre',
                               selection=[
                                            ('1', '1'),
                                            ('2', '2'),
                                            ('3', '3'),
                                            ('4', '4'),
                                        ],
                               required=True)"""
    caliber = fields.Integer(string='Calibre')                           

    shade = fields.Char(string='Nuance') 
    """shade = fields.Selection(string='Nuance',
                             selection=[
                                            ('N1', 'N1'),
                                            ('N2', 'N2'),
                                            ('N3', 'N3'),
                                        ],
                             required=True)"""

    metrage = fields.Float(string='Métrage', required=True)

    """choice = fields.Selection(string='Choix',
                              selection=[
                                            ('Premier', 'Premier'),
                                            ('Deusieme', 'Deusieme'),
                                        ],
                              required=True)"""
    choice = fields.Many2one('choix.list', string="Choix", required=True)

    affich_nuance_calibre = fields.Boolean(compute='compute_affich_nuance_calibre')

    manufacturing_date = fields.Selection(string='Date de fabrication',
                                     selection='_get_manufacturing_date_options',
                                     required=True)

    format = fields.Many2one('format.list', string="Format", required=True)
    """reference = fields.Many2one(string="Reference", compute='_get_ref_format_ids', required=True, domain="[('name', '=', self.format)]"""
    reference = fields.Many2one('article.format', string="Référence", required=True, domain="[('format_id', '=', format)]")

    """production_line = fields.Selection(string='Ligne de production',
                                       selection=[
                                           ('M3', 'M3'), ('M4', 'M4'), ('M1 L2', 'M1 L2')],
                                       required=True)"""
    production_line = fields.Char("Ligne de production", default=lambda self: self.env.user.name, required=True)
    
    #selection_field= fields.Selection(selection=lambda self: self.dynamic_selection())
    
    """manufacturing_date = fields.Selection([(num, str(num)) for num in range(1900, (datetime.now())-1 )],
                                            string='Date de fabrication', default=datetime.now())"""

    def action_create_product_qrcode(self):
        print('generate product qrcode')

    @api.onchange('reference')
    def _onchange_reference(self):
        if self.reference:
            self.metrage = self.reference.palette

    def compute_affich_nuance_calibre(self):
        if self.choice:
            self.affich_nuance_calibre=self.choice.nuance_calibre
            print(self.affich_nuance_calibre)
        else:
            self.affich_nuance_calibre = False

    @api.onchange('choice')
    def _onchange_choice(self):
        if self.choice:
            self.affich_nuance_calibre=self.choice.nuance_calibre
            print(self.affich_nuance_calibre)
            if self.affich_nuance_calibre == True:
                self.shade = ""
                self.caliber = ""
        else:
            self.affich_nuance_calibre = False

    @api.model
    def _get_manufacturing_date_options(self):
        #yesterday = datetime.today() - timedelta(days=2, hours=6)
        yesterday = datetime.today() - timedelta(days=1, hours=6)
        d1 = yesterday.strftime('%d/%m/%Y')

        #today = datetime.today() - timedelta(days=1, hours=6)
        today = datetime.today()
        d2 = today.strftime('%d/%m/%Y')

        value_list = [(d1, d1), (d2, d2)]
        return value_list

    @api.onchange('shade')
    def set_upper(self):
        if self.shade:
            self.shade = str(self.shade).upper()
        return

"""def dynamic_selection(self):
      #select = [('yes', 'Yes'), ('no', 'No')]
      select = []
      today = date.today()
      yesterday = today - timedelta(days = 2)
      select.append(yeterday)
      select.append(today)
      #select = self.env['article.format'].search([('name', '=', [self.format])])
      return select
                                                                             
    
        
    @api.onchange('format')
    def _onchange_format(self):
        self.dynamic_selection()

    
            
    @api.depends('format') 
    def _get_ref_format_ids(self):
        for rec in self:
            others = self.env['article.format'].search(
                [('name', '=', [rec.format])],
                limit=1)                                  
            if others.reference:
                rec.reference = others.reference.id
            else:
                rec.reference = []
                
    
        
    @api.onchange('format')
    def _onchange_format(self):
        if self.format:
            if self.format.reference:
                self.reference = self.format.reference
            if self.format.palette:
                self.metrage = self.format.palette
        else:
            self.reference = ''
            self.metrage = 100"""        
