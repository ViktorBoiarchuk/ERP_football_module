from openerp.osv import osv, fields


class football_team(osv.osv):
    _name = 'football.team'
    _columns = {
        'name': fields.char('Team name', size=128, required=True),
        'foundation_date': fields.date('Foundation date', size=4),
        'starting_date': fields.date('First official match'),
        'colours': fields.text('Team colours'),
        'player_ids': fields.one2many('football.player', 'team_id', 'Players'),
        'stadium_id': fields.many2one('football.stadium', 'Home stadium'),
        'fans_id': fields.many2one('football.fans', 'Ultras name'),
        # 'team_id': fields.many2one('football.player', ''),
    }
football_team()
