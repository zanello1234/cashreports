# © 2025 ADHOC SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Cashbox Reports",
    "summary": "Advanced reports for cashbox sessions with check details",
    "version": "18.0.1.0.0",
    "category": "Accounting",
    "website": "www.adhoc.com.ar",
    "author": "ADHOC SA",
    "license": "AGPL-3",
    "depends": [
        "account_cashbox",
        "l10n_latam_check",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/cashbox_session_report_wizard.xml",
        "reports/cashbox_session_report.xml",
        "reports/cashbox_session_report_template.xml",
        "views/account_cashbox_session.xml",
        "views/menuitem.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
