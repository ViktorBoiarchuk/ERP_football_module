from openerp.osv import osv, fields


class Fans(osv.osv):
    _name = 'football.fans'
    _columns = {
        'name': fields.char('ultras name', size=32, required=True),
        'country': fields.char('country', size=32, required=True),
        'date_of_foundation': fields.date('foundation', required=True),
        'number': fields.integer('the number of fans'),
        'sights': fields.boolean('Radicals sights'),
        'team_id': fields.many2one('team', 'supported team', required=True),
        'team_ids': fields.one2many('team', 'team_id', 'ultras brotherhood')
    }
Fans()
