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

class salesorderline (models.Model):

    _inherit ='sale.order.line'

   
    x_days = fields.Integer(string='Days')
    x_hourperday = fields.Integer(string='Hours/Day')
    
    
    @api.onchange('x_days','x_hourperday')
    def _onchange_field(self):
        #if self.product_uom and self.product_uom == 'Hours':
        self.product_uom_qty = self.x_days*self.x_hourperday
    
    

    
    
    
    


    

    
   
    

    
  
    





    #_sql_constraints = [('constrainname', 'UNIQUE (name)', '[Contract] This Contract Number already exist')]
    



    
  
  
