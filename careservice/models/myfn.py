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


#TODO
#JOb CancelTranlogNotTrade Descrption is database value
#Job STockMatchiong to cancel all trans if no active session


class myfn (models.AbstractModel):
    _name = 'myfn'


    def LookupValue(self ,x_type,x_name):
        recs = self.env['lov'].search([('x_type','=',x_type),('name','=',x_name)],limit=1)
        for rec in recs:
            return rec.x_val
        return None

   
    def concatString(self ,str1,str2):
        str11 =""
        str22=""
        if(str1):
            str11 = str1
        if(str2):
            str22 = str2
        return str11+str22





    


            

                


            




                
            




        



            
                



                        



                        


                    


                    

                        
                   









    
  
  
