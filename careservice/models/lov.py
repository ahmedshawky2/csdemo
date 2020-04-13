# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string
import requests

import logging
_logger = logging.getLogger(__name__)


class lov (models.Model):
    _name = 'lov'
  
    
    name = fields.Char(string='Name' ,index=True, required=True)
    x_type = fields.Char(string='Type' ,index=True, required=True)
    x_val = fields.Char(string='Val' ,index=True, required=True)
    active = fields.Boolean(string='Active' ,index=True, required=True, default=True)
    x_parent= fields.Many2one(string='Parent',comodel_name='lov')
    
    

    
  
    





    _sql_constraints = [('constrainname', 'UNIQUE (name, x_type, x_val,x_parent)', 'This List already exists')]
    



    
  
  
