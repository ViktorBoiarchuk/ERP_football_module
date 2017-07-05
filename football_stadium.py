from openerp.osv import osv, fields


class football_stadium(osv.osv):
    _name = 'football.stadium'
    _columns = {
        'name': fields.char('Stadium name', size=32, required=True),
        'country': fields.char('Country, region', size=32, required=True),
        'date_of_foundation': fields.date('Foundation', required=True),
        'capacity': fields.integer('Capacity of the stadium', required=True),
        'compliance_with_UEFA': fields.boolean('UEFA requirements'),
        'team_id': fields.many2one('football.team', 'Home team'),
        # 'team_ids': fields.one2many('football.team', 'stadium_id', 'teams played at this stadium'),
    }

football_stadium()
