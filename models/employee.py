from odoo import models, fields

class Employee(models.Model):
    _name = 'employee.management'
    _description = 'Employee Management'

    name = fields.Char(string='Employee Name', required=True)
    employee_code = fields.Char(string='Empoyee Code', required=True,copy=False)
    age = fields.Integer(string='Age')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    salary = fields.Float(string='Salary')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    joining_date = fields.Date( string='Joining Date',default=fields.Date.today)
    active = fields.Boolean(string='Active',
        default=True)
