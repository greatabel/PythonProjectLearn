from otree.api import *



doc = """
a.k.a. Keynesian beauty contest.
Players all guess a number; whoever guesses closest to
2/3 of the average wins.
See https://en.wikipedia.org/wiki/Guess_2/3_of_the_average
"""


mydict = {}

class Constants(BaseConstants):
    players_per_group = 10
    num_rounds = 10
    name_in_url = 'guess_two_thirds'
    jackpot = Currency(100)
    guess_max = 100
    instructions_template = 'guess_two_thirds/instructions.html'



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    two_thirds_avg = models.FloatField()
    best_guess = models.IntegerField()
    num_winners = models.IntegerField()


class Player(BasePlayer):
    guess = models.IntegerField(
        min=0, max=Constants.guess_max, label="Please pick a number from 0 to 100:"
    )
    is_winner = models.BooleanField(initial=False)


# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()
    guesses = [p.guess for p in players]
    two_thirds_avg = (2 / 3) * sum(guesses) / len(players)
    group.two_thirds_avg = round(two_thirds_avg, 2)
    group.best_guess = min(guesses, key=lambda guess: abs(guess - group.two_thirds_avg))
    winners = [p for p in players if p.guess == group.best_guess]
    group.num_winners = len(winners)
    for p in winners:
        p.is_winner = True
        p.payoff = Constants.jackpot / group.num_winners


def two_thirds_avg_history(group: Group):
    return [g.two_thirds_avg for g in group.in_previous_rounds()]


# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        global mydict
        flag = True
        for k, v in mydict.items():
            if len(v) < Constants.num_rounds:
                flag = False
        if flag:
            mydict = {}
            print('Introduction -> '*2, 'clear mydict')
        return player.round_number == 1


class Guess(Page):
    form_model = 'player'
    form_fields = ['guess']

    def vars_for_template(player: Player):
        group = player.group

        return dict(two_thirds_avg_history=two_thirds_avg_history(group))


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        global mydict
        group = player.group
        print('player=',player, 'mydict=', mydict)
        if player.id_in_group  in mydict and not (mydict[player.id_in_group] is None):
            old = mydict[player.id_in_group]
            print('#'*10, 'mydict['+str(player.id_in_group)+']=', old)
            print('#'*20, 'dict=',mydict)

            old.append(str(player.payoff))
            mydict[player.id_in_group] = old
        else:
            mydict[player.id_in_group] = [str(player.payoff)]
            print('@'*20, 'dict=', mydict)
        s  = mydict[player.id_in_group]

        sorted_guesses = sorted(p.guess for p in group.get_players())
        return dict(sorted_guesses=sorted_guesses, s=s)


page_sequence = [Introduction, Guess, ResultsWaitPage, Results]