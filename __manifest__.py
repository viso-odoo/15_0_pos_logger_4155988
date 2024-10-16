{
    'name': "POS Logger",

    'summary': """
        Logger for POS restarting issue, opw-4155988. Odoo v15
    """,

    'description': """
        Forces to log POS events when the POS window is reloaded.
        The events are logged back to the server logs.
        Required because the error happens "randomly" and can't be reproduced on tech support's
        machines or in staging.
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com/",
    'category': 'Support/POS-Log',
    'version': '0.1',
    'application': False,
    'installable': True,
    'depends': ['point_of_sale'],

    'data': [],
    'assets': {
        'point_of_sale.assets': [
            '15_0_pos_logger_4155988/static/src/Chrome.js',
        ],
    },
    'license': 'AGPL-3'
}