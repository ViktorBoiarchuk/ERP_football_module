from openerp.osv import osv, fields


class football_game_data(osv.osv):
    _name = 'football.game.data'

    def defining_team_satisfaction(self, cr, uid, ids, name, args, context={}):
        if not ids:
            return {}
        res = {}.fromkeys(ids, [])
        team_pool = self.read(cr, uid, ids, ['team'], context=context)
        for ind, record in enumerate(ids):
            if team_pool[ind]['team'] == '1':
                res[record] = 'Satisfied with the team !'
            else:
                res[record] = 'Disappointed with the team !'
        return res

    _columns = {
        'team': fields.selection([('1', 'Team #1 (Winners)'), ('2', 'Team #2 (Losers)')], 'Team', required=True),
        'game_id': fields.many2one('football.game', 'Game'),
        'player_id': fields.many2one('football.player', 'Player'),
        'team_satisfaction': fields.function(defining_team_satisfaction, string='Team satisfaction', method=True,
                                             type='char'),
    }
    _order = 'team'

football_game_data()
