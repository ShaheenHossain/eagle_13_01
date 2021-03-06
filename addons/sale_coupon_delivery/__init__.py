# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.
from eagle import api, SUPERUSER_ID

from . import models


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['delivery.carrier'].search([
        ('delivery_type', '=', 'temando')
    ]).write({'delivery_type': 'fixed', 'fixed_price': 0})
