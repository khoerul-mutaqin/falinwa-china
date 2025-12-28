from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_studio_report_selection = fields.Selection([
        ('address', 'Address'),
        ('company_details', 'Company Details')
    ], string="Report Header Selection", default='address', help="Choose what to display in the report header")