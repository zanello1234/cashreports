from odoo import api, fields, models
from odoo.exceptions import UserError

class CashboxSessionReportWizard(models.TransientModel):
    _name = 'cashbox.session.report.wizard'
    _description = 'Reporte de Sesiones de Caja'

    session_ids = fields.Many2many(
        'account.cashbox.session',
        string='Sesiones de Caja',
        required=True,
        domain=[('state', 'in', ['opened', 'closing_control', 'closed'])]
    )
    journal_ids = fields.Many2many(
        'account.journal',
        string='Diarios',
        required=False,
        domain=[('type', 'in', ['cash', 'bank'])]
    )
    date_from = fields.Date(
        string='Fecha Desde',
        help='Filtrar sesiones desde esta fecha (fecha de apertura)'
    )
    date_to = fields.Date(
        string='Fecha Hasta', 
        help='Filtrar sesiones hasta esta fecha (fecha de apertura)'
    )
    
    @api.onchange('date_from', 'date_to')
    def _onchange_dates(self):
        """Update domain for sessions based on date filters"""
        domain = [('state', 'in', ['opened', 'closing_control', 'closed'])]
        
        if self.date_from:
            domain.append(('opening_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('opening_date', '<=', self.date_to))
            
        return {'domain': {'session_ids': domain}}

    @api.model
    def default_get(self, fields_list):
        """Set default dates"""
        res = super().default_get(fields_list)
        if 'date_from' in fields_list:
            # Default to beginning of current month
            today = fields.Date.today()
            res['date_from'] = today.replace(day=1)
        if 'date_to' in fields_list:
            # Default to today
            res['date_to'] = fields.Date.today()
        return res

    def action_generate_report(self):
        self.ensure_one()
        if not self.session_ids:
            raise UserError("Debe seleccionar al menos una sesión de caja para generar el reporte.")
        
        # Usar el método estándar de Odoo para reportes
        return self.env.ref('account_cashbox_reports.action_cashbox_session_report').report_action(self.session_ids) 
