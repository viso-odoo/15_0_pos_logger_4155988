from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class ConsoleTraceController(http.Controller):

    @http.route('/console_trace/log_trace', type='json', auth='user')
    def log_console_trace(self, trace):
        """
        Endpoint to receive console traces from the frontend and log them in the backend.
        """
        _logger.info("Received console trace from frontend:\n%s", trace)
        return {'status': 'success', 'message': 'Trace logged successfully'}
