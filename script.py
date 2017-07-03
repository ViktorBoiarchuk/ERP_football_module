from datetime import datetime


def onchange_age(self, cr, uid, ids, date_of_birth, context={}):
    real_age = (datetime.today() - datetime.strptime(date_of_birth, "%Y-%m-%d")).days/365.2425
    # players = self.search(cr, uid, [('name', '=', 'Viktor')])
    # if not players:
    #     return {'value': {'age': real_age.days}}
    # players_res = self.read(cr, uid, players, context=context)
    # players_obj = self.browse(cr, uid, players[0], context=context)
    # query example.
    # cr.execute('''
    # select *
    # from football_player
    # where id = (1,)
    # ''', (tuple(players),))
    # res = cr.fetchall()
    # stadium_ids = players_obj.stadium_ids
    return {'value': {'age': real_age, 'name': 'Ihor'}}