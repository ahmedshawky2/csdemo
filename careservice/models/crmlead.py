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

class crmlead (models.Model):
    _inherit = ['crm.lead']

    x_area_id = fields.Many2one(string = 'Area',related='partner_id.x_area_id',readonly=True,store=True)
    sector_id = fields.Many2one(string='Sector',comodel_name='lov',domain=[('x_type','=','SECTOR')],index=True)
    sector_id2 = fields.Many2one(string='Sector L2',comodel_name='lov',index=True)
    sector_id3 = fields.Many2one(string='Sector L3',comodel_name='lov',index=True)   
    
    
    


    

    
   
    

    
  
    





    #_sql_constraints = [('constrainname', 'UNIQUE (name)', '[Contract] This Contract Number already exist')]
    



    
  
  
