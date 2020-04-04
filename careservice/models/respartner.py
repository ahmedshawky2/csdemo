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

class respartner (models.Model):
    _inherit = ['res.partner']

    x_mailingaddress = fields.Char(string='Mailing Address',index=True)
    x_customertype = fields.Selection([('TEMP', 'Temp'),('PERM', 'Permanent')], string='Customer Type',index=True)
    x_fax = fields.Char(string='Fax',index=True)
    x_emergency_phone = fields.Char(string='Emergency Phone',index=True)
    x_authorized_person = fields.Char(string='Authorized Person Name',index=True)
    x_authorized_phone  = fields.Char(string='Authorized Person Phone',index=True)
    x_area_id = fields.Many2one(string='Area',comodel_name='lov',domain=[('x_type','=','AREA')])
   
    
    
    


    

    
   
    

    
  
    





    #_sql_constraints = [('constrainname', 'UNIQUE (name)', '[Contract] This Contract Number already exist')]
    



    
  
  
