# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class school_student(models.Model):
    _name = 'school.student'
    _description = 'school_student'

    name = fields.Char(string="Name", required=True)
    school_id = fields.Many2one("school.profile", string="School", required=True, default=1)


class SchoolProfile(models.Model):
    _inherit = "school.profile"

    school_list = fields.One2many("school.student", "school_id", string="School List", required=True)

    @api.model
    def create(self, vals):
        rtn = super(SchoolProfile, self).create(vals)
        if not rtn.school_list:
            raise UserError(_("Student list is empty!"))
        return rtn


class Hobbies(models.Model):
    _name = "hobby"

    name = fields.Char(string="Hobby")
