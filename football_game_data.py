from openerp.osv import osv, fields


class football_game_data(osv.osv):
    _name = 'football.game.data'
    _columns = {
        'team': fields.selection([('1', 'Team #1'), ('2', 'Team #2')], 'Team', required=True),
        'game_id': fields.many2one('football.game', 'Game'),
        'player_id': fields.many2one('football.player', 'Player'),
    }
    _order = 'team'

football_game_data()
