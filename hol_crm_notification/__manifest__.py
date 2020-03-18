# -*- coding: utf-8 -*-

##############################################################################
#
#   Odoo, Open Source Management Solution
#   Copyright (C) 2018 Port Cities International
#   Author : Portcities
#
##############################################################################
{
    'name': 'Hukum Online CRM Notification',
    'summary': 'Create Log Message When Update Fields In The Form',
    'description': """
This module is used to create a log message when there are some changes on the form.

v1.0.0
------
* Initial version
* Add log messages in all fields
* Add log when create a quotation
* Add log when attach an attachment

    Author: Reynaldi Yosfino
    """,
    'author': 'Portcities',
    'website': 'http://www.portcities.net',
    'category': 'CRM',
    'version': '11.0.0.0.0',
    'depends': ['base','crm','sale'],
    'sequence': 1,
    'data': [
        'data/mail_message_subtype.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3'
}
