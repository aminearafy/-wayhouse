# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import logging


logger = logging.getLogger(__name__)


class ProductController(http.Controller):

    @http.route(['/wayhouse/product/assign'], type='json', auth='public', methods=['POST'], csrf=False, website=True)
    def assign_product(self, **args):
        logger.info(args)

        format = args.get('format', False)
        reference = args.get('reference', False)
        metrage = args.get('metrage', 0)
        choix = args.get('choice', False)
        calibre = args.get('caliber', 0)
        nuance = args.get('shade', False)
        line_production = args.get('production_line', False)
        date_fabrication = args.get('manufacturing_date', False)
        tag = args.get('tag', False)

        product = request.env['product.template'].sudo().create({
            'name': reference,
            'format': format,
            'reference': reference,
            'metrage': metrage,
            'choix': choix,
            'calibre': calibre,
            'nuance': nuance,
            'line_production': line_production,
            'date_fabrication': date_fabrication,
            'tag': tag,
        })

        logger.info(product)

        resp = {}
        resp['error'] = False
        resp['message'] = ''
        resp['data'] = {'product_id': product.id}

        return resp

    @http.route(['/wayhouse/product/receive'], type='json', auth='public', methods=['POST'], csrf=False, website=True)
    def receive_products(self, **args):
        logger.info(args)

        product_ids = args.get('product_ids', False)
        location_dest_id = args.get('location_dest_id', False)

        company_id = 1
        location_id = 4

        data = {
            'company_id': company_id,
            'move_type': 'direct',
            'location_id': location_id,
            'location_dest_id': location_dest_id,
            'picking_type_id': 1,
            'immediate_transfer': True,
            'state': 'done',
            'move_ids_without_package': []
        }

        for product_id in product_ids:
            data['move_ids_without_package'].append([
                    0,
                    0,
                    { 
                        'name': '',
                        'location_id': location_id,
                        'location_dest_id': location_dest_id,
                        'product_id': product_id,
                        'product_uom': 1,
                        'product_uom_qty': 1,
                        'quantity_done': 1
                    }
                ]
            )
        
        logger.info(data)

        '''
        {
            'company_id': 1, 
            'move_type': 'direct', 
            'location_id': 4, 
            'location_dest_id': False, 
            'picking_type_id': 1, 
            'immediate_transfer': True, 
            'state': 'done', 
            'move_ids_without_package': [[0, 0, {'name': '', 'location_id': 4, 'location_dest_id': False, 'product_id': 15, 'product_uom': 1, 'product_uom_qty': 1, 'quantity_done': 1}]]}
        '''

        transfer = request.env['stock.picking'].sudo().create(data)
        logger.info(transfer)

        resp = {}
        resp['error'] = False
        resp['message'] = ''
        resp['data'] = transfer

        return resp
