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

class contractlineitem (models.Model):
    _name = 'contractlineitem'
    _inherit = ['myfn','mail.thread','mail.activity.mixin']

   
    contractheader_id = fields.Many2one(string='contract',comodel_name='contractheader',index=True)
    Product_id = fields.Many2one(string='Product',comodel_name='product.template',index=True)
    x_days = fields.Integer(string='Days',index=True)
    x_hourperday = fields.Integer(string='Hours/Day',index=True)
    name = fields.Char(string='Descrption',index=True)
    product_uom_qty = fields.Integer(string='Quantity',index=True)
    product_uom =fields.Char(string='UOM',index=True)
    price_unit = fields.Float(string='Unit Price',index=True )
    price_subtotal= fields.Float(string='Subtotal',index=True )
    




    
  
  
