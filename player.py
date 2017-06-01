from openerp.osv import osv, fields


class Player(osv.osv):
    _name = 'football.player'
    _columns = {
        'name': fields.char('player name', size=32, required=True),
        'surname': fields.char('player surname', size=32, required=True),
        'date_of_birth': fields.date('date of birth'),
        'age': fields.integer('age'),
        'team_id': fields.many2one('team', 'team name', required=True),
        'favourite stadium': fields.many2one('stadium', 'lucky stadium')
    }
Player()
