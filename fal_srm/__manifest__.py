# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SRM',
    'version': '12.5.0.0.0',
    'category': 'Purchases',
    'sequence': 5,
    'summary': 'Track proposal and close supplier opportunities',
    'description': "",
    'website': 'https://falinwa.com',
    'depends': [
        'purchase_requisition',
        'base_setup',
        'mail',
        'calendar',
        'resource',
        'fetchmail',
        'utm',
        'web_tour',
        'contacts',
        'digest',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/srm_security.xml',
        'data/srm_data.xml',
        'data/srm_stage_data.xml',
        'data/srm_lead_data.xml',
        'data/digest_data.xml',
        'wizard/srm_proposal_lost_views.xml',
        'wizard/srm_merge_agreements_views.xml',
        'wizard/srm_proposal_to_agreement_views.xml',
        'views/res_config_settings_views.xml',
        'views/digest_views.xml',
        'views/srm_team_views.xml',
        'views/srm_views.xml',
        'views/srm_proposal_views.xml',
        'views/srm_stage_views.xml',
        'views/calendar_views.xml',
        'views/res_partner_views.xml',
        'report/srm_activity_report_views.xml',
        'report/srm_opportunity_report_views.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
