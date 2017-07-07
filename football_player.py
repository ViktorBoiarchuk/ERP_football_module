from openerp.osv import osv, fields
from datetime import datetime
from random import sample


class football_player(osv.osv):
    _name = 'football.player'



    _columns = {
        'name': fields.char('Player name', size=32, required=True),
        'surname': fields.char('Player surname', size=32, required=True),
        'date_of_birth': fields.date('Date of birth'),
        'age': fields.integer('Age'),
        'team_id': fields.many2one('football.team', 'Players team'),
        'stadium_ids': fields.many2many('football.stadium', 'player_stadium_rel',
                                        'player_id', 'stadium_id', 'Lucky stadiums'),
        'game_id': fields.many2one('football.game', 'Player\'s game participation'),
        # 'team_1_ids': fields.one2many('wizard/football.wizard', 'team_1_id', 'Team #1'),
    }

    def onchange_age(self, cr, uid, ids, date_of_birth, context={}):
        real_age = (datetime.today() - datetime.strptime(date_of_birth, "%Y-%m-%d")).days / 365.2425
        return {'value': {'age': real_age}}

    def name_get(self, cr, user, ids, context={}):
        if not ids:
            return []
        res = []
        for record in self.read(cr, user, ids, ['name', 'surname'], context=context):
            name = record['name']
            if record['surname']:
                name += ' ' + record['surname']
            res.append((record['id'], name))
        return res

    def resulted_table_creating(self, cr, uid, ids, context={}):
        stadium = self.pool.get('football.stadium').search(cr, uid, [('name', '=', 'Markevich football center')],
                                                           context=context)
        game_player_pool = self.pool.get('football.game.data')
        happiness = game_player_pool.read(cr, uid, ids, ['team_satisfaction'], context=context)
        default_game = {'name': 'Weekly Enapps\'s game', 'datetime': datetime.today().date(), 'stadium_id': stadium and stadium[0],
                        'duration': 1.5}
        game = self.pool.get('football.game').create(cr, uid, default_game, context=context)
        team_gen = [str(2) for dummy_x in range(len(ids))]
        for i in sample(range(len(ids)), len(ids)/2):
            team_gen[i] = '1'
        for ind, player_id in enumerate(ids):
            game_player_pool.create(cr, uid, {'game_id': game, 'player_id': player_id, 'team': team_gen[ind],
                                              'team_satisfaction': happiness[ind]['team_satisfaction']},
                                    context=context)
        return {'name': 'football game',
                'view_mode': 'form',
                'view_type': 'form',
                'view_id': False,
                'res_id': game,
                'res_model': 'football.game',
                'type': 'ir.actions.act_window',
                'nodestroy': True,
                'views': [(False, 'form')]
                }

football_player()
