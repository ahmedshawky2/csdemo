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
        comodel_name='contractlineitem',
            
    )


    

   

    

    
    
    
    


    

    
   
    

    
  
    





    #_sql_constraints = [('constrainname', 'UNIQUE (name)', '[Contract] This Contract Number already exist')]
    



    
  
  
