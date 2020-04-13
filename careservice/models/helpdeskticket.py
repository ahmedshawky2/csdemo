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

class helpdeskticket (models.Model):
    _inherit = 'helpdesk.ticket'


 
    contract_id = fields.Many2one(
        string='Contract',
        comodel_name='contractheader',
            
    )

    contractlineitem = fields.Many2one(
        string='Product',
        comodel_name='contractlineitem'
            
    )
    sector_id = fields.Many2one(
        string='Sector',
        
        related='contract_id.sector_id',
        readonly=True
        
            
    )
    sector_id2 = fields.Many2one(string='Sector L2', related='contract_id.sector_id2',readonly=True)
    sector_id3 = fields.Many2one(string='Sector L3', related='contract_id.sector_id3',readonly=True)   
    x_area_id = fields.Many2one(string = 'Area',related='partner_id.x_area_id',readonly=True,store=True)





    

   

    

    
    
    
    


    

    
   
    

    
  
    





    #_sql_constraints = [('constrainname', 'UNIQUE (name)', '[Contract] This Contract Number already exist')]
    



    
  
  
