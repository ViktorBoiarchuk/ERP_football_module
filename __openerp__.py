{
    'name': 'football',
    'version': '1.0',
    'author': 'Viktor Boiarchuk',
    'description': 'this module shows in which way the football life is designed',
    'category': 'sports & events',
    'complexity': 'easy',
    'website': 'http://www.odoo.com',

    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'team_view.xml',
        'stadium_view.xml',
        'fans_view.xml',
        'referee_view.xml',
        'player_view.xml',
        'game_view.xml',
        'football_game_data.xml',
        # 'wizard/football_wizard_view.xml',
        'data/ir_actions_object.xml',
    ],
    'installable': True,
}
