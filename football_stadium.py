from openerp.osv import osv, fields


class football_stadium(osv.osv):
    _name = 'football.stadium'
    _columns = {
        'stadium_name': fields.char('stadium name', size=32, required=True),
        'country': fields.char('country', size=32, required=True),
        'date_of_foundation': fields.date('foundation', required=True),
        'capacity': fields.integer('capacity of the stadium', required=True),
        'compliance_with_UEFA': fields.boolean('UEFA requirements'),
        #'player_id': fields.many2one('football.player', 'Player', ),
        'team_ids': fields.one2many('football.team', 'stadium_id', 'teams played at the stadium')
    }
football_stadium()
