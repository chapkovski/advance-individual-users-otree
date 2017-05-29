from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import csv
import json
from otree.models_concrete import ParticipantToPlayerLookup, RoomToSession
from App2.models import Player as App2Player

# from otree.models.session import Session as BaseSession
author = 'Philipp Chapkovski, University of Zurich'

doc = """
    app1
"""


class Constants(BaseConstants):
    name_in_url = 'app1'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):
    def before_session_starts(self):
        allapp2 = App2Player.objects.all()
        for a in allapp2:
            print('APP2:', a.pk, ' round:: ', a.round_number)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    decision = models.IntegerField()
