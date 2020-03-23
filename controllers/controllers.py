# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class plant(http.Controller):
    @http.route('/get_plant',type='json',auth='user')
    def get_plant(self):
        plants_rec=request.env['nursery.plant'].search([])
        plants=[]
        for rec in plants_rec:
            vals={
                'name':rec.name,
                'price':rec.price,
                'order_ids':rec.order_ids
            }
            plants.append(vals)
        data={'status':200,'response':plants,'message':'done all plants record'}
        return data
    @http.route('/create_plant',type='json',auth='user')
    def create_plant(self,**rec):
        if request.jsonrequest:
            if rec['name']:
                vals={
                    'name':rec['name'],
                    'price':rec['price'],
                    'number_in_stock':rec['number_in_stock']
                }
                new_plant=request.env['nursery.plant'].sudo().create(vals)
                args={'id':new_plant.id}
        return args