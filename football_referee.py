from openerp.osv import osv, fields


class football_referee(osv.osv):
    _name = 'football.referee'
    _columns = {
        'name': fields.char('Referee name', size=32, required=True),
        'surname': fields.char('Referee surname', size=32, required=True),
        'date_of_birth': fields.date('Date of birth'),
        'age': fields.integer('Age'),
        'team_id': fields.many2one('football.team', 'Lovely team'),
    }
football_referee()
