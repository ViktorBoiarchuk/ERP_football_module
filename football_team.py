from openerp.osv import osv, fields


class football_team(osv.osv):
    _name = 'football.team'
    _columns = {
        'team_name': fields.char('Team name', size=128, required=True),
        'foundation_year': fields.integer('Foundation year', size=4, required=True),
        'starting_date': fields.date('First official match'),
        'colours': fields.text('Team colours'),
        # 'player_ids': fields.one2many('football.player', 'player_id', 'Players'),
        'stadium_id': fields.many2one('football.stadium', 'home stadium')
    }
football_team()
