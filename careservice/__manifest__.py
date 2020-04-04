{
    'name': 'careservice',
    'description': 'careservice',
    'author': 'Minds',
    'depends': ['base','crm','sale_management','helpdesk','l10n_generic_coa'],
    'application': True,
    'data': [

    'views/ir_ui_view.xml',
    #'views/ir_actions_act_window.xml',
    'views/ir_ui_menu.xml',
    #'views/ir_seq.xml',
    'security/ir.model.access.csv',
        ],
    'installable':True
}
