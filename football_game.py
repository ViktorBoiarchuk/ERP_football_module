from openerp.osv import osv, fields


class football_game(osv.osv):
    _name = 'football.game'
    _columns = {
        'name': fields.char('Games name', size=32, required=True),
        'datetime': fields.datetime('Game start time'),
        'stadium_id': fields.many2one('football.stadium', 'Stadium for the game'),
        'duration': fields.float('Duration of the match'),
        # 'player_ids': fields.many2many('football.player', 'game_player_rel', 'game_id', 'player_id', 'Players'),
        'game_data_ids': fields.one2many('football.game.data', 'game_id', 'Participants'),
    }

football_game()
