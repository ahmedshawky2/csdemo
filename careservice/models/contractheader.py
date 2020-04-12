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

class contractheader (models.Model):
    _name = 'contractheader'
    _inherit = ['myfn','mail.thread','mail.activity.mixin']

    name = fields.Char(string='Contract number',index=True)
    contype = fields.Selection([('OPEN', 'Open'),('TEMP', 'Temp'),('PERM', 'Permanent'),], string='Contract Type',index=True)
    increaseprecentage = fields.Integer(string='Increase Prcentage',index=True)
    conperiodday = fields.Integer(string='Contract Period Days',index=True)
    conperiodmonth = fields.Integer(string='Contract Period Months',index=True)
    conperiodyears = fields.Integer(string='Contract Period Years',index=True)
    customer_id = fields.Many2one(string='customer',comodel_name='res.partner',index=True)
    alarmPeriod = fields.Integer(string='Contract Alarm months',index=True,)
    state = fields.Selection([('PENDING', 'Pending'),('ACTIVE', 'Active'),('DEACTIVE', 'Deactive'),('CANCELLED', 'Cancelled')], string='Status',index=True,default='PENDING')
    total =  fields.Float(string='Total',index=True,)
    discount =  fields.Float(string='discount',index=True,)
    startdate = fields.Date(string='Start Date',index=True)
    expiredate = fields.Date(string='Expire Date',index=True,compute='_compute_expiredate' ,store=True )
    parent_customer_id = fields.Many2one(string = 'Parent Customer',related='customer_id.parent_id',readonly=True,store=True)
    sector_id = fields.Many2one(string='Sector',comodel_name='lov',domain=[('x_type','=','SECTOR')],index=True)

    
    lineitem_ids = fields.One2many(string='lineitem',comodel_name='contractlineitem',inverse_name='contractheader_id',index=True)

    amount_untaxed= fields.Float(string='Amount untaxed',index=True )
    amount_tax= fields.Float(string='Tax',index=True )
    quote_id = fields.Many2one(
        string='Quote',
        comodel_name='sale.order',
        index=True
    )

    x_area_id = fields.Many2one(string = 'Area',related='customer_id.x_area_id',readonly=True,store=True)
    
    
    

    
    
    
    


    

    
   
    

    
  
    





    
    
    


    ##############Releated########################
    customer_ref =  fields.Char(string='Customer Reference ',index=True ,related='customer_id.ref',readonly=True)

    
    @api.depends('conperiodday','conperiodmonth','conperiodyears','startdate')
    def _compute_expiredate(self):
        for record in self:
            if record.startdate:
                record.expiredate =  record.startdate + timedelta(days=(record.conperiodday +record.conperiodmonth*30 +record.conperiodyears*365.2425 ))
            else:
                record.expiredate = False
    
    #############################################

    def setactive(self):
        if not self.name :
            raise ValidationError("Contract Number is mandatory")
        self.state = 'ACTIVE'

    def setdeactive(self):
        self.state = 'DEACTIVE'
    
    
    


    

    
   
    

    
  
    





#_sql_constraints = [('constrainname', 'UNIQUE (name)', '[Contract] This Contract Number already exist')]
_sql_constraints = [('constrainname', 'UNIQUE (quote_id)', '[Contract] This Quote already assigned to another Contract ')]   



    
  
  
