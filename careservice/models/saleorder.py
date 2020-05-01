# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
from datetime import date
import string
import requests
from datetime import timedelta

import logging
_logger = logging.getLogger(__name__)


#TODO
#

class saleorder (models.Model):
    
    _inherit = 'sale.order'


    offertype_id = fields.Many2one(string='offertype',comodel_name='lov',domain=[('x_type','=','QUOTE_OFFER_TYPE')],index=True)

    contract_id = fields.One2many('contractheader', 'quote_id', string='Contract',index=True)
    x_area_id = fields.Many2one(string = 'Area',related='partner_id.x_area_id',readonly=True,store=True)
    offertype_id = fields.Many2one(string='Offer Type',comodel_name='lov',domain=[('x_type','=','QUOTE_OFFER_TYPE')],index=True)
    x_surveyby_id = fields.Many2one(string='Survey by',comodel_name='lov',domain=[('x_type','=','SURVEYBY')],index=True)
    x_surveyon =  fields.Datetime(string='Survey on',index=True)
    sector_id = fields.Many2one(string='Sector',comodel_name='lov',domain=[('x_type','=','SECTOR')],index=True)
    sector_id2 = fields.Many2one(string='Sector L2',comodel_name='lov',index=True)
    sector_id3 = fields.Many2one(string='Sector L3',comodel_name='lov',index=True)   

    


    def createcontract(self):
        for r in self :
            recs = self.env['contractheader'].search([('quote_id','=',r.id)])
            if len(recs)>0:
                 raise ValidationError("Quote already has a Contract")

            coid = self.env['contractheader'].create({'customer_id':r.partner_id.id,
            'total':r.amount_total,
            'amount_untaxed':r.amount_untaxed,
            'amount_tax':r.amount_tax,
            'quote_id':r.id,
            'sector_id':r.sector_id.id,
            'sector_id2':r.sector_id2.id,
            'sector_id3':r.sector_id3.id,
            'team_id':r.team_id.id})
        for l in r.order_line:
                self.env['contractlineitem'].create({'contractheader_id':coid.id,
                'Product_id':l.product_id.id,
                'x_days':l.x_days,
                'x_hourperday':l.x_hourperday,
                'name':l.name,
                'product_uom_qty':l.product_uom_qty,
                'product_uom':l.product_uom.name,
                'price_unit':l.price_unit,
                'price_subtotal':l.price_subtotal
                
                
                })

    
    @api.onchange('sector_id')
    def _onchange_sector_id(self):
        self.team_id = False
        self.sector_id2 = False
        self.sector_id3 = False


    @api.onchange('team_id')
    def _onchange_team_id(self):
        
        self.sector_id2 = False
        self.sector_id3 = False

    @api.onchange('sector_id2')
    def _onchange_sector_id2(self):
        self.sector_id3 = False    



    
