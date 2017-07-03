from openerp.osv import osv, fields


class football_fans(osv.osv):
    _name = 'football.fans'
    _columns = {
        'name': fields.char('Ultras name', size=32, required=True),
        'country': fields.char('Country', size=32, required=True),
        'date_of_foundation': fields.date('Foundation', required=True),
        'number': fields.integer('The number of fans'),
        'sights': fields.boolean('Radical sights'),
        'team_id': fields.many2one('football.team', 'Supported team'),
        'team_ids': fields.one2many('football.team', 'fans_id', 'Ultras brotherhood'),
    }
football_fans()
