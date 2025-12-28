# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.company'


    x_studio_company_details = fields.Many2one(
        'res.company',
         "Company Details",
    )    