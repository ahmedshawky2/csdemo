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

class helpdeskteam (models.Model):
    _inherit = 'helpdesk.team'
    sector_id = fields.Many2one(string='Sector',comodel_name='lov',domain=[('x_type','=','SECTOR')],index=True)


   

    

    
    
    
    


    

    
   
    

    
  
    





    #_sql_constraints = [('constrainname', 'UNIQUE (name)', '[Contract] This Contract Number already exist')]
    



    
  
  
