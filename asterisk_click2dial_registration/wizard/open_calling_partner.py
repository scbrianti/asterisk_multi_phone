# -*- encoding: utf-8 -*-
##############################################################################
#
#    Asterisk Click2dial Registration module for OpenERP
#    Copyright (C) 2013 Invitu (http://www.invitu.com/)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm


class wizard_open_calling_partner(orm.TransientModel):
    _inherit = "wizard.open.calling.partner"

    def open_registrations(self, cr, uid, ids, context=None):
        '''Function called by the related button of the wizard'''
        return self.open_filtered_object(
            cr, uid, ids, self.pool.get('event.registration'), context=context)
