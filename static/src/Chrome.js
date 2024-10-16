/** @odoo-module **/

import { patch } from 'web.utils';
import Chrome from 'point_of_sale.Chrome';
import ajax from 'web.ajax';

patch(Chrome.prototype, '15_0_pos_logger_4155988.chrome', {
    mounted() {
        this._super.apply(this, arguments);
        window.addEventListener('beforeunload', this.handleBeforeUnload);
    },

    willUnmount() {
        window.removeEventListener('beforeunload', this.handleBeforeUnload);
        this._super.apply(this, arguments);
    },

    handleBeforeUnload(event) {

        // Send this data to your backend
        let trace = (new Error()).stack;
        ajax.jsonRpc('/console_trace/log_trace', 'call', { trace: trace })
    },
});
