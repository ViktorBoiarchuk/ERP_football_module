from openerp.osv import osv, fields
from datetime import datetime


class football_player(osv.osv):
    _name = 'football.player'
    _columns = {
        'name': fields.char('Player name', size=32, required=True),
        'surname': fields.char('Player surname', size=32, required=True),
        'date_of_birth': fields.date('Date of birth'),
        'age': fields.integer('Age'),
        'team_id': fields.many2one('football.team', 'Players team'),
        'stadium_ids': fields.many2many('football.stadium', 'player_stadium_rel',
                                        'stadium_id', 'player_id', 'Lucky stadiums'),
    }

    def onchange_age(self, cr, uid, ids, date_of_birth, context={}):
        real_age = (datetime.today() - datetime.strptime(date_of_birth, "%Y-%m-%d")).days / 365.2425
        return {'value': {'age': real_age}}

football_player()
