from odoo import api, fields, models, _
from odoo.exceptions import UserError

class JournalProdParDate(models.TransientModel):
    _name = "production.journal"

    date_deb = fields.Date(required=True, string="Date début", default=fields.Date.today())
    date_fin = fields.Date(required=True, string="Date fin", default=fields.Date.today())
    par_details = fields.Boolean(string="Détails par Nuance & Calibre")
    unite_id = fields.Many2one('res.users', string="Unité de production")
    total_tags = fields.Integer(string='Total tags')
    total_metrage = fields.Float(string='Total métrage')

    def check_report(self):
        domain= []
        if self.date_deb:
            domain += [('date_fabrication', '>=', self.date_deb)]
        if self.date_fin:
            domain += [('date_fabrication', '<=', self.date_fin)]
        if self.unite_id:
            domain += [('line_production', '=', self.unite_id.name)]
        products = self.env['product.template'].search_read(domain)
        print('user', self.unite_id)
        if products:
            print('products', products)
            compteur = 0
            toto = 0
            for i in products:
                compteur += 1
                toto += i['metrage']
            self.total_tags = compteur
            self.total_metrage = toto
            data = {
                'form': self.read()[0],
                'products': products,
            }
            print('data', data)
            if not self.par_details:
                return self.env.ref('wayhouse.action_journal_prod_par_date').report_action(self, data=data)
            else:
                return self.env.ref('wayhouse.action_journal_prod_par_date_details').report_action(self, data=data, config=False)
        else:
            raise UserError("Aucune référence pour cette période!")
        #data['form'] = self.read(['date_deb', 'date_fin'])[0]
        #return self._print_report(data)

    """def _print_report(self, data):
        #data['form'].update(self.read()[0])
        #return self.env['report'].get_action(self, 'journal_prod_par_date_report.journal_prod_par_date', data=data)
        return self.env.ref('wayhouse.action_journal_prod_par_date').report_action(self, data=data)"""