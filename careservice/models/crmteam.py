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

class crmteam (models.Model):
    _inherit = 'crm.team'
    sector_id = fields.Many2one(string='Sector',comodel_name='lov',domain=[('x_type','=','SECLVL3')],index=True)



   

    

    
    
    
    


    

    
   
    

    
  
    





    #_sql_constraints = [('constrainname', 'UNIQUE (name)', '[Contract] This Contract Number already exist')]
    



    
  
  
