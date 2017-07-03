from openerp.osv import osv, fields


class football_stadium(osv.osv):
    _name = 'football.stadium'
    _columns = {
        'name': fields.char('Stadium name', size=32, required=True),
        'country': fields.char('Country', size=32, required=True),
        'date_of_foundation': fields.date('Foundation', required=True),
        'capacity': fields.integer('Capacity of the stadium', required=True),
        'compliance_with_UEFA': fields.boolean('UEFA requirements'),
        'team_id': fields.many2one('football.team', 'Home team'),
        'player_ids': fields.many2many('football.player', 'player_stadium_rel',
                                       'player_id', 'stadium_id', 'Player'),
        # 'team_ids': fields.one2many('football.team', 'stadium_id', 'teams played at this stadium'),
    }
football_stadium()

# 'sponsor_ids': fields.many2many('res.partner','idea_sponsor_rel','idea_id','sponsor_id','Sponsors'),
