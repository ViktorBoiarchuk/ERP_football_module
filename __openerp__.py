{
    'name': 'football',
    'version': '1.0',
    'author': 'Viktor Boiarchuk',
    'description': 'this module shows in which way the football life is designed',
    'category': 'sports & events',
    'complexity': 'easy',
    'website': 'http://www.openerp.com',

    'depends': ['base'],
    'data': [
        #'fans_view.xml',
        #'player_view.xml',
        #'referee_view.xml.xml',
        'stadium_view.xml',
        'team_view.xml'
    ],
    'installable': True,
}
