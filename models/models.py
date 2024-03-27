# -*- coding: utf-8 -*-

from odoo import models, fields, api
#variable's name must be be connected by using _

class task(models.Model): #All classes inherit from the models.Model class.
   #required fields
   _name = 'manage.task' # module.class(or model)
   _description = 'manage.task' # whatever we want

   name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre") #if there is no label assigned to the field it will take the name we provided
   description = fields.Text()
   creation_date = fields.Date()
   start_date = fields.Datetime()
   end_date  = fields.Datetime()
   is_paused  = fields.Boolean()
   sprint = fields.Many2one('manage.sprint', 
   ondelete='set null', 
   help='Sprint Relacionado'
   )
   techs = fields.Many2many(comodel_name="manage.tech",
   relation_name="tech_task",
   column1 = "task_id",
   column2="tech_id")

class sprint(models.Model): 
   _name = 'manage.sprint'
   _description = 'manage.sprint' 
   
   name  = fields.Char()
   description = fields.Text()
   start_date = fields.Datetime()
   end_date = fields.Datetime()
   task = fields.One2many(string="Tareas",
   comodel_name='manage.task', 
   inverse_name='sprint') # the field sprint in manage.task
# A task has many sprints
# A sprint has many task


class tech(models.Model): 
   _name = 'manage.tech'
   _description = 'manage.tech' 
   
   name  = fields.Char()
   description = fields.Text()
   photo = fields.Image(max_width=200, max_height=200) #binary is a file
   task = fields.Many2many(comodel_name="manage.task",
   relation_name="teck_task",
   column1="tech_id",
   column2="task_id")