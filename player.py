from openerp.osv import osv, fields


class Player(osv.osv):
    _name = 'football.player'
    _columns = {
        'name': fields.char('player name', size=32, required=True),
        'surname': fields.char('player surname', size=32, required=True),
        'date_of_birth': fields.date('date of birth'),
        'age': fields.integer('age'),
        'team_id': fields.many2one('football.team', 'team name', required=True),
        # 'stadium_ids': fields.one2many('football.stadium', 'lucky stadium')
    }
Player()
