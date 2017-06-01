from openerp.osv import osv, fields


class Referee(osv.osv):
    _name = 'football.referee'
    _columns = {
        'name': fields.char('referee name', size=32, required=True),
        'surname': fields.char('referee surname', size=32, required=True),
        'date_of_birth': fields.date('date of birth'),
        'age': fields.integer('age'),
        'team_id': fields.many2one('football.team', 'team name', required=True),
        # 'favourite team': fields.many2one('stadium', 'lovely team'),
        # 'hated team': fields.many2one('team', 'hated team')
    }
Referee()
