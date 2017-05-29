from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
import random
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        if self.player.eg and self.player.wu and views.page_sequence == sum(views.w, []):
            yield (views.EGTrainingsphase1, {'egtestquestion1': 45, 'egtestquestion2': random.randint(1, 50),
                                             'egtestquestion3': random.randint(1, 50)})
            yield (views.EGTrainingsphase2,
                   {'egtestquestion4': random.randint(1, 50), 'egtestquestion5': random.randint(1, 50),
                    'egtestquestion6': random.randint(1, 50)})
            yield (views.Letsgetstarted)
            yield (views.EGBallpreupdate,
                   {'egballquestion1': random.randint(1, 60), 'egballquestion2': random.randint(1, 40),
                    'egballquestion3': random.randint(20, 60)})
            yield (views.WTPBall1, {'wtp_ball1': 10})
            yield (views.EGBallpostweakupdate,
                   {'egballquestion4': random.randint(1, 60), 'egballquestion5': random.randint(1, 40),
                    'egballquestion6': random.randint(20, 60)})
            yield (views.WTPBall2, {'wtp_ball2': 40})
            yield (views.EGBallweakresults)
            yield (views.EGDicepreupdate,
                   {'egdicequestion1': random.randint(10, 60), 'egdicequestion2': random.randint(10, 50),
                    'egdicequestion3': random.randint(20, 60)})
            yield (views.WTPDice1, {'wtp_dice1': 10})
            yield (views.EGDicepostweakupdate,
                   {'egdicequestion4': random.randint(10, 60), 'egdicequestion5': random.randint(10, 50),
                    'egdicequestion6': random.randint(20, 60)})
            yield (views.WTPDice2, {'wtp_dice2': 40})
            yield (views.EGDiceweakresults)
            yield (views.EGCloudpreupdate,
                   {'egcloudquestion1': random.randint(20, 40), 'egcloudquestion2': random.randint(20, 35),
                    'egcloudquestion3': random.randint(25, 40)})
            yield (views.WTPCloud1, {'wtp_cloud1': 120})
            yield (views.EGCloudpostweakupdate,
                   {'egcloudquestion4': random.randint(20, 40), 'egcloudquestion5': random.randint(20, 35),
                    'egcloudquestion6': random.randint(25, 40)})
            yield (views.WTPCloud2, {'wtp_cloud2': 180})
            yield (views.EGCloudweakresults)
            yield (views.EGTemperaturepreupdate,
                   {'egtemperaturequestion1': random.randint(20, 40), 'egtemperaturequestion2': random.randint(20, 40),
                    'egtemperaturequestion3': random.randint(20, 40)})
            yield (views.WTPTemperature1, {'wtp_temperature1': 30})
            yield (views.EGTemperaturepostweakupdate,
                   {'egtemperaturequestion4': random.randint(20, 40), 'egtemperaturequestion5': random.randint(20, 40),
                    'egtemperaturequestion6': random.randint(20, 40)})
            yield (views.WTPTemperature2,
                   {'wtp_temperature2': 10})
            yield (views.EGTemperatureweakresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '10.01.1900', 'gender': 'weiblich', 'fieldofstudy': 'Psychologie',
                                        'profession': 'Student', 'moneyathand': 'weniger als 250',
                                        'probabilityexp1': '1',
                                        'probabilityexp2': '5', 'probabilityexp3': 'Ja',
                                        'cse1': 'Ich stimme eindeutig zu',
                                        'cse2': 'Ich stimme eindeutig zu', 'cse3': 'Ich stimme eindeutig zu', 'cse4':
                                            'Ich stimme eindeutig zu', 'cse5': 'Ich stimme eindeutig zu', 'cse6':
                                            'Ich stimme eindeutig zu', 'cse7': 'Ich stimme eindeutig zu', 'cse8':
                                            'Ich stimme eindeutig zu', 'cse9': 'Ich stimme eindeutig zu', 'cse10':
                                            'Ich stimme eindeutig zu', 'cse11': 'Ich stimme eindeutig zu', 'cse12':
                                            'Ich stimme eindeutig zu'})

        elif self.player.eg and self.player.wu and views.page_sequence == sum(views.x, []):
            yield (views.EGTrainingsphase1, {'egtestquestion1': 45, 'egtestquestion2': random.randint(1, 50),
                                                 'egtestquestion3': random.randint(1, 50)})
            yield (views.EGTrainingsphase2,
                       {'egtestquestion4': random.randint(1, 50), 'egtestquestion5': random.randint(1, 50),
                        'egtestquestion6': random.randint(1, 50)})
            yield (views.Letsgetstarted)
            yield (views.EGDicepreupdate,
                       {'egdicequestion1': random.randint(10, 60), 'egdicequestion2': random.randint(10, 50),
                        'egdicequestion3': random.randint(20, 60)})
            yield (views.WTPDice1, {'wtp_dice1': 10})
            yield (views.EGDicepostweakupdate,
                       {'egdicequestion4': random.randint(10, 60), 'egdicequestion5': random.randint(10, 50),
                        'egdicequestion6': random.randint(20, 60)})
            yield (views.WTPDice2, {'wtp_dice2': 40})
            yield (views.EGDiceweakresults)
            yield (views.EGCloudpreupdate,
                       {'egcloudquestion1': random.randint(20, 40), 'egcloudquestion2': random.randint(20, 35),
                        'egcloudquestion3': random.randint(25, 40)})
            yield (views.WTPCloud1, {'wtp_cloud1': 120})
            yield (views.EGCloudpostweakupdate,
                       {'egcloudquestion4': random.randint(20, 40), 'egcloudquestion5': random.randint(20, 35),
                        'egcloudquestion6': random.randint(25, 40)})
            yield (views.WTPCloud2, {'wtp_cloud2': 180})
            yield (views.EGCloudweakresults)
            yield (views.EGTemperaturepreupdate,
                       {'egtemperaturequestion1': random.randint(20, 40),
                        'egtemperaturequestion2': random.randint(20, 40),
                        'egtemperaturequestion3': random.randint(20, 40)})
            yield (views.WTPTemperature1, {'wtp_temperature1': 30})
            yield (views.EGTemperaturepostweakupdate,
                       {'egtemperaturequestion4': random.randint(20, 40),
                        'egtemperaturequestion5': random.randint(20, 40),
                        'egtemperaturequestion6': random.randint(20, 40)})
            yield (views.WTPTemperature2,
                       {'wtp_temperature2': 10})
            yield (views.EGTemperatureweakresults)
            yield (views.EGBallpreupdate,
                       {'egballquestion1': random.randint(1, 60), 'egballquestion2': random.randint(1, 40),
                        'egballquestion3': random.randint(20, 60)})
            yield (views.WTPBall1, {'wtp_ball1': 10})
            yield (views.EGBallpostweakupdate,
                       {'egballquestion4': random.randint(1, 60), 'egballquestion5': random.randint(1, 40),
                        'egballquestion6': random.randint(20, 60)})
            yield (views.WTPBall2, {'wtp_ball2': 40})
            yield (views.EGBallweakresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (
                views.Demographics, {'birthday': '21.01.1900', 'gender': 'weiblich', 'fieldofstudy': 'Psychologie',
                                     'profession': 'Student', 'moneyathand': 'weniger als 250', 'probabilityexp1': '1',
                                     'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1': 'Ich stimme eindeutig zu',
                                     'cse2': 'Ich stimme eindeutig zu', 'cse3': 'Ich stimme eindeutig zu', 'cse4':
                                         'Ich stimme eindeutig zu', 'cse5': 'Ich stimme eindeutig zu', 'cse6':
                                         'Ich stimme eindeutig zu', 'cse7': 'Ich stimme eindeutig zu', 'cse8':
                                         'Ich stimme eindeutig zu', 'cse9': 'Ich stimme eindeutig zu', 'cse10':
                                         'Ich stimme eindeutig zu', 'cse11': 'Ich stimme eindeutig zu', 'cse12':
                                         'Ich stimme eindeutig zu'})

        elif self.player.eg and self.player.wu and views.page_sequence == sum(views.y, []):
            yield (views.EGTrainingsphase1, {'egtestquestion1': 45, 'egtestquestion2': random.randint(1, 50),
                                                 'egtestquestion3': random.randint(1, 50)})
            yield (views.EGTrainingsphase2,
                       {'egtestquestion4': random.randint(1, 50), 'egtestquestion5': random.randint(1, 50),
                        'egtestquestion6': random.randint(1, 50)})
            yield (views.Letsgetstarted)
            yield (views.EGCloudpreupdate,
                   {'egcloudquestion1': random.randint(20, 40), 'egcloudquestion2': random.randint(20, 35),
                    'egcloudquestion3': random.randint(25, 40)})
            yield (views.WTPCloud1, {'wtp_cloud1': 120})
            yield (views.EGCloudpostweakupdate,
                   {'egcloudquestion4': random.randint(20, 40), 'egcloudquestion5': random.randint(20, 35),
                    'egcloudquestion6': random.randint(25, 40)})
            yield (views.WTPCloud2, {'wtp_cloud2': 180})
            yield (views.EGCloudweakresults)
            yield (views.EGTemperaturepreupdate,
                   {'egtemperaturequestion1': random.randint(20, 40),
                    'egtemperaturequestion2': random.randint(20, 40),
                    'egtemperaturequestion3': random.randint(20, 40)})
            yield (views.WTPTemperature1, {'wtp_temperature1': 30})
            yield (views.EGTemperaturepostweakupdate,
                   {'egtemperaturequestion4': random.randint(20, 40),
                    'egtemperaturequestion5': random.randint(20, 40),
                    'egtemperaturequestion6': random.randint(20, 40)})
            yield (views.WTPTemperature2,
                   {'wtp_temperature2': 10})
            yield (views.EGTemperatureweakresults)
            yield (views.EGBallpreupdate,
                       {'egballquestion1': random.randint(1, 60), 'egballquestion2': random.randint(1, 40),
                        'egballquestion3': random.randint(20, 60)})
            yield (views.WTPBall1, {'wtp_ball1': 10})
            yield (views.EGBallpostweakupdate,
                       {'egballquestion4': random.randint(1, 60), 'egballquestion5': random.randint(1, 40),
                        'egballquestion6': random.randint(20, 60)})
            yield (views.WTPBall2, {'wtp_ball2': 40})
            yield (views.EGBallweakresults)
            yield (views.EGDicepreupdate,
                   {'egdicequestion1': random.randint(10, 60), 'egdicequestion2': random.randint(10, 50),
                    'egdicequestion3': random.randint(20, 60)})
            yield (views.WTPDice1, {'wtp_dice1': 10})
            yield (views.EGDicepostweakupdate,
                   {'egdicequestion4': random.randint(10, 60), 'egdicequestion5': random.randint(10, 50),
                    'egdicequestion6': random.randint(20, 60)})
            yield (views.WTPDice2, {'wtp_dice2': 40})
            yield (views.EGDiceweakresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900', 'gender': 'weiblich', 'fieldofstudy': 'Psychologie',
                                         'profession': 'Student', 'moneyathand': 'weniger als 250',
                                         'probabilityexp1': '1',
                                         'probabilityexp2': '5', 'probabilityexp3': 'Ja',
                                         'cse1': 'Ich stimme eindeutig zu',
                                         'cse2': 'Ich stimme eindeutig zu', 'cse3': 'Ich stimme eindeutig zu', 'cse4':
                                             'Ich stimme eindeutig zu', 'cse5': 'Ich stimme eindeutig zu', 'cse6':
                                             'Ich stimme eindeutig zu', 'cse7': 'Ich stimme eindeutig zu', 'cse8':
                                             'Ich stimme eindeutig zu', 'cse9': 'Ich stimme eindeutig zu', 'cse10':
                                             'Ich stimme eindeutig zu', 'cse11': 'Ich stimme eindeutig zu', 'cse12':
                                             'Ich stimme eindeutig zu'})

        elif self.player.eg and self.player.wu and views.page_sequence == sum(views.z, []):
            yield (views.EGTrainingsphase1, {'egtestquestion1': 45, 'egtestquestion2': random.randint(1, 50),
                                             'egtestquestion3': random.randint(1, 50)})
            yield (views.EGTrainingsphase2,
                   {'egtestquestion4': random.randint(1, 50), 'egtestquestion5': random.randint(1, 50),
                    'egtestquestion6': random.randint(1, 50)})
            yield (views.Letsgetstarted)
            yield (views.EGTemperaturepreupdate,
                   {'egtemperaturequestion1': random.randint(20, 40),
                    'egtemperaturequestion2': random.randint(20, 40),
                    'egtemperaturequestion3': random.randint(20, 40)})
            yield (views.WTPTemperature1, {'wtp_temperature1': 30})
            yield (views.EGTemperaturepostweakupdate,
                   {'egtemperaturequestion4': random.randint(20, 40),
                    'egtemperaturequestion5': random.randint(20, 40),
                    'egtemperaturequestion6': random.randint(20, 40)})
            yield (views.WTPTemperature2,
                   {'wtp_temperature2': 10})
            yield (views.EGTemperatureweakresults)
            yield (views.EGBallpreupdate,
                   {'egballquestion1': random.randint(1, 60), 'egballquestion2': random.randint(1, 40),
                    'egballquestion3': random.randint(20, 60)})
            yield (views.WTPBall1, {'wtp_ball1': 10})
            yield (views.EGBallpostweakupdate,
                   {'egballquestion4': random.randint(1, 60), 'egballquestion5': random.randint(1, 40),
                    'egballquestion6': random.randint(20, 60)})
            yield (views.WTPBall2, {'wtp_ball2': 40})
            yield (views.EGBallweakresults)
            yield (views.EGDicepreupdate,
                   {'egdicequestion1': random.randint(10, 60), 'egdicequestion2': random.randint(10, 50),
                    'egdicequestion3': random.randint(20, 60)})
            yield (views.WTPDice1, {'wtp_dice1': 10})
            yield (views.EGDicepostweakupdate,
                   {'egdicequestion4': random.randint(10, 60), 'egdicequestion5': random.randint(10, 50),
                    'egdicequestion6': random.randint(20, 60)})
            yield (views.WTPDice2, {'wtp_dice2': 40})
            yield (views.EGDiceweakresults)
            yield (views.EGCloudpreupdate,
                   {'egcloudquestion1': random.randint(20, 40), 'egcloudquestion2': random.randint(20, 35),
                    'egcloudquestion3': random.randint(25, 40)})
            yield (views.WTPCloud1, {'wtp_cloud1': 120})
            yield (views.EGCloudpostweakupdate,
                   {'egcloudquestion4': random.randint(20, 40), 'egcloudquestion5': random.randint(20, 35),
                    'egcloudquestion6': random.randint(25, 40)})
            yield (views.WTPCloud2, {'wtp_cloud2': 180})
            yield (views.EGCloudweakresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900', 'gender': 'weiblich', 'fieldofstudy': 'Psychologie',
                                        'profession': 'Student', 'moneyathand': 'weniger als 250',
                                        'probabilityexp1': '1',
                                        'probabilityexp2': '5', 'probabilityexp3': 'Ja',
                                        'cse1': 'Ich stimme eindeutig zu',
                                        'cse2': 'Ich stimme eindeutig zu', 'cse3': 'Ich stimme eindeutig zu', 'cse4':
                                            'Ich stimme eindeutig zu', 'cse5': 'Ich stimme eindeutig zu', 'cse6':
                                            'Ich stimme eindeutig zu', 'cse7': 'Ich stimme eindeutig zu', 'cse8':
                                            'Ich stimme eindeutig zu', 'cse9': 'Ich stimme eindeutig zu', 'cse10':
                                            'Ich stimme eindeutig zu', 'cse11': 'Ich stimme eindeutig zu', 'cse12':
                                            'Ich stimme eindeutig zu'})



        elif not self.player.eg and self.player.wu and views.page_sequence == sum(views.w, []):
            yield(views.QSRTrainingsphase1, {'qsrtestquestion1': random.uniform(0,2)})
            yield(views.QSRTrainingsphase2, {'qsrtestquestion2': random.uniform(0,2)})
            yield(views.QSRTrainingsphase3, {'qsrtestquestion3': random.uniform(0,2)})
            yield (views.Letsgetstarted)
            yield (views.QSRBallpreupdate,
           {'qsrballquestion1': 0, 'qsrballquestion2': 20, 'qsrballquestion3': 60, 'qsrballquestion4': 20})
            yield (views.WTPBall1,{'wtp_ball1': 4})
            yield (views.QSRBallpostweakupdate,
           {'qsrballquestion5': 0, 'qsrballquestion6': 0, 'qsrballquestion7': 0, 'qsrballquestion8': 100})
            yield (views.WTPBall2, {'wtp_ball2': 35})
            yield (views.QSRBallweakresults)
            yield (views.QSRDicepreupdate,
           {'qsrdicequestion1': 0, 'qsrdicequestion2': 20, 'qsrdicequestion3': 60, 'qsrdicequestion4': 20})
            yield (views.WTPDice1,{'wtp_dice1': 10})
            yield (views.QSRDicepostweakupdate,
           {'qsrdicequestion5': 0, 'qsrdicequestion6': 0, 'qsrdicequestion7': 0, 'qsrdicequestion8': 100})
            yield (views.WTPDice2,{'wtp_dice2': 30})
            yield (views.QSRDiceweakresults)
            yield (views.QSRCloudpreupdate,
           {'qsrcloudquestion1': 0, 'qsrcloudquestion2': 20, 'qsrcloudquestion3': 60, 'qsrcloudquestion4': 20})
            yield (views.WTPCloud1,
           {'wtp_cloud1': 120})
            yield (views.QSRCloudpostweakupdate,
           {'qsrcloudquestion5': 0, 'qsrcloudquestion6': 0, 'qsrcloudquestion7': 0, 'qsrcloudquestion8': 100})
            yield (views.WTPCloud2,
           {'wtp_cloud2': 170})
            yield (views.QSRCloudweakresults)
            yield(views.QSRTemperaturepreupdate, {'qsrtemperaturequestion1': 0, 'qsrtemperaturequestion2': 20, 'qsrtemperaturequestion3': 60, 'qsrtemperaturequestion4': 20})
            yield (views.WTPTemperature1,
                   {'wtp_temperature1': 20})
            yield(views.QSRTemperaturepostweakupdate, {'qsrtemperaturequestion5': 0, 'qsrtemperaturequestion6': 0, 'qsrtemperaturequestion7': 0, 'qsrtemperaturequestion8': 100})
            yield (views.WTPTemperature2,{'wtp_temperature2': 30})
            yield (views.QSRTemperatureweakresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900',
           'gender':'weiblich', 'fieldofstudy': 'Psychologie', 'profession': 'Student', 'moneyathand': 'weniger als 250'
            , 'probabilityexp1': '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1': 'Ich stimme eindeutig zu'
            , 'cse2': 'Ich stimme eindeutig zu', 'cse3': 'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu',
            'cse5': 'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7': 'Ich stimme eindeutig zu',
            'cse8': 'Ich stimme eindeutig zu', 'cse9': 'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu',
            'cse11': 'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})

        elif not self.player.eg and self.player.wu and views.page_sequence == sum(views.x, []):
            yield(views.QSRTrainingsphase1, {'qsrtestquestion1': random.uniform(0,2)})
            yield(views.QSRTrainingsphase2, {'qsrtestquestion2': random.uniform(0,2)})
            yield(views.QSRTrainingsphase3, {'qsrtestquestion3': random.uniform(0,2)})
            yield (views.Letsgetstarted)
            yield (views.QSRDicepreupdate,
           {'qsrdicequestion1': 0, 'qsrdicequestion2': 20, 'qsrdicequestion3': 60, 'qsrdicequestion4': 20})
            yield (views.WTPDice1,{'wtp_dice1': 10})
            yield (views.QSRDicepostweakupdate,
           {'qsrdicequestion5': 0, 'qsrdicequestion6': 0, 'qsrdicequestion7': 0, 'qsrdicequestion8': 100})
            yield (views.WTPDice2,{'wtp_dice2': 30})
            yield (views.QSRDiceweakresults)
            yield (views.QSRCloudpreupdate,
           {'qsrcloudquestion1': 0, 'qsrcloudquestion2': 20, 'qsrcloudquestion3': 60, 'qsrcloudquestion4': 20})
            yield (views.WTPCloud1,
           {'wtp_cloud1': 120})
            yield (views.QSRCloudpostweakupdate,
           {'qsrcloudquestion5': 0, 'qsrcloudquestion6': 0, 'qsrcloudquestion7': 0, 'qsrcloudquestion8': 100})
            yield (views.WTPCloud2,
           {'wtp_cloud2': 170})
            yield (views.QSRCloudweakresults)
            yield(views.QSRTemperaturepreupdate, {'qsrtemperaturequestion1': 0, 'qsrtemperaturequestion2': 20, 'qsrtemperaturequestion3': 60, 'qsrtemperaturequestion4': 20})
            yield (views.WTPTemperature1,
                   {'wtp_temperature1': 20})
            yield(views.QSRTemperaturepostweakupdate, {'qsrtemperaturequestion5': 0, 'qsrtemperaturequestion6': 0, 'qsrtemperaturequestion7': 0, 'qsrtemperaturequestion8': 100})
            yield (views.WTPTemperature2,{'wtp_temperature2': 30})
            yield (views.QSRTemperatureweakresults)
            yield (views.QSRBallpreupdate,
                   {'qsrballquestion1': 0, 'qsrballquestion2': 20, 'qsrballquestion3': 60, 'qsrballquestion4': 20})
            yield (views.WTPBall1, {'wtp_ball1': 4})
            yield (views.QSRBallpostweakupdate,
                   {'qsrballquestion5': 0, 'qsrballquestion6': 0, 'qsrballquestion7': 0, 'qsrballquestion8': 100})
            yield (views.WTPBall2, {'wtp_ball2': 35})
            yield (views.QSRBallweakresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900',
           'gender':'weiblich', 'fieldofstudy': 'Psychologie', 'profession': 'Student', 'moneyathand': 'weniger als 250'
            , 'probabilityexp1': '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1': 'Ich stimme eindeutig zu'
            , 'cse2': 'Ich stimme eindeutig zu', 'cse3': 'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu',
            'cse5': 'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7': 'Ich stimme eindeutig zu',
            'cse8': 'Ich stimme eindeutig zu', 'cse9': 'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu',
            'cse11': 'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})

        elif not self.player.eg and self.player.wu and views.page_sequence == sum(views.y, []):
            yield(views.QSRTrainingsphase1, {'qsrtestquestion1': random.uniform(0,2)})
            yield(views.QSRTrainingsphase2, {'qsrtestquestion2': random.uniform(0,2)})
            yield(views.QSRTrainingsphase3, {'qsrtestquestion3': random.uniform(0,2)})
            yield (views.Letsgetstarted)
            yield (views.QSRCloudpreupdate,
           {'qsrcloudquestion1': 0, 'qsrcloudquestion2': 20, 'qsrcloudquestion3': 60, 'qsrcloudquestion4': 20})
            yield (views.WTPCloud1,
           {'wtp_cloud1': 120})
            yield (views.QSRCloudpostweakupdate,
           {'qsrcloudquestion5': 0, 'qsrcloudquestion6': 0, 'qsrcloudquestion7': 0, 'qsrcloudquestion8': 100})
            yield (views.WTPCloud2,
           {'wtp_cloud2': 170})
            yield (views.QSRCloudweakresults)
            yield(views.QSRTemperaturepreupdate, {'qsrtemperaturequestion1': 0, 'qsrtemperaturequestion2': 20, 'qsrtemperaturequestion3': 60, 'qsrtemperaturequestion4': 20})
            yield (views.WTPTemperature1,
                   {'wtp_temperature1': 20})
            yield(views.QSRTemperaturepostweakupdate, {'qsrtemperaturequestion5': 0, 'qsrtemperaturequestion6': 0, 'qsrtemperaturequestion7': 0, 'qsrtemperaturequestion8': 100})
            yield (views.WTPTemperature2,{'wtp_temperature2': 30})
            yield (views.QSRTemperatureweakresults)
            yield (views.QSRBallpreupdate,
                   {'qsrballquestion1': 0, 'qsrballquestion2': 20, 'qsrballquestion3': 60, 'qsrballquestion4': 20})
            yield (views.WTPBall1, {'wtp_ball1': 4})
            yield (views.QSRBallpostweakupdate,
                   {'qsrballquestion5': 0, 'qsrballquestion6': 0, 'qsrballquestion7': 0, 'qsrballquestion8': 100})
            yield (views.WTPBall2, {'wtp_ball2': 35})
            yield (views.QSRBallweakresults)
            yield (views.QSRDicepreupdate,
                   {'qsrdicequestion1': 0, 'qsrdicequestion2': 20, 'qsrdicequestion3': 60, 'qsrdicequestion4': 20})
            yield (views.WTPDice1, {'wtp_dice1': 10})
            yield (views.QSRDicepostweakupdate,
                   {'qsrdicequestion5': 0, 'qsrdicequestion6': 0, 'qsrdicequestion7': 0, 'qsrdicequestion8': 100})
            yield (views.WTPDice2, {'wtp_dice2': 30})
            yield (views.QSRDiceweakresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900',
           'gender':'weiblich', 'fieldofstudy': 'Psychologie', 'profession': 'Student', 'moneyathand': 'weniger als 250'
            , 'probabilityexp1': '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1': 'Ich stimme eindeutig zu'
            , 'cse2': 'Ich stimme eindeutig zu', 'cse3': 'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu',
            'cse5': 'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7': 'Ich stimme eindeutig zu',
            'cse8': 'Ich stimme eindeutig zu', 'cse9': 'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu',
            'cse11': 'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})

        elif not self.player.eg and self.player.wu and views.page_sequence == sum(views.z, []):
            yield(views.QSRTrainingsphase1, {'qsrtestquestion1': random.uniform(0,2)})
            yield(views.QSRTrainingsphase2, {'qsrtestquestion2': random.uniform(0,2)})
            yield(views.QSRTrainingsphase3, {'qsrtestquestion3': random.uniform(0,2)})
            yield (views.Letsgetstarted)
            yield(views.QSRTemperaturepreupdate, {'qsrtemperaturequestion1': 0, 'qsrtemperaturequestion2': 20, 'qsrtemperaturequestion3': 60, 'qsrtemperaturequestion4': 20})
            yield (views.WTPTemperature1,
                   {'wtp_temperature1': 20})
            yield(views.QSRTemperaturepostweakupdate, {'qsrtemperaturequestion5': 0, 'qsrtemperaturequestion6': 0, 'qsrtemperaturequestion7': 0, 'qsrtemperaturequestion8': 100})
            yield (views.WTPTemperature2,{'wtp_temperature2': 30})
            yield (views.QSRTemperatureweakresults)
            yield (views.QSRBallpreupdate,
                   {'qsrballquestion1': 0, 'qsrballquestion2': 20, 'qsrballquestion3': 60, 'qsrballquestion4': 20})
            yield (views.WTPBall1, {'wtp_ball1': 4})
            yield (views.QSRBallpostweakupdate,
                   {'qsrballquestion5': 0, 'qsrballquestion6': 0, 'qsrballquestion7': 0, 'qsrballquestion8': 100})
            yield (views.WTPBall2, {'wtp_ball2': 35})
            yield (views.QSRBallweakresults)
            yield (views.QSRDicepreupdate,
                   {'qsrdicequestion1': 0, 'qsrdicequestion2': 20, 'qsrdicequestion3': 60, 'qsrdicequestion4': 20})
            yield (views.WTPDice1, {'wtp_dice1': 10})
            yield (views.QSRDicepostweakupdate,
                   {'qsrdicequestion5': 0, 'qsrdicequestion6': 0, 'qsrdicequestion7': 0, 'qsrdicequestion8': 100})
            yield (views.WTPDice2, {'wtp_dice2': 30})
            yield (views.QSRDiceweakresults)
            yield (views.QSRCloudpreupdate,
                   {'qsrcloudquestion1': 0, 'qsrcloudquestion2': 20, 'qsrcloudquestion3': 60, 'qsrcloudquestion4': 20})
            yield (views.WTPCloud1,
                   {'wtp_cloud1': 120})
            yield (views.QSRCloudpostweakupdate,
                   {'qsrcloudquestion5': 0, 'qsrcloudquestion6': 0, 'qsrcloudquestion7': 0, 'qsrcloudquestion8': 100})
            yield (views.WTPCloud2,
                   {'wtp_cloud2': 170})
            yield (views.QSRCloudweakresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900',
           'gender':'weiblich', 'fieldofstudy': 'Psychologie', 'profession': 'Student', 'moneyathand': 'weniger als 250'
            , 'probabilityexp1': '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1': 'Ich stimme eindeutig zu'
            , 'cse2': 'Ich stimme eindeutig zu', 'cse3': 'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu',
            'cse5': 'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7': 'Ich stimme eindeutig zu',
            'cse8': 'Ich stimme eindeutig zu', 'cse9': 'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu',
            'cse11': 'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})




        elif self.player.eg and not self.player.wu and views.page_sequence == sum(views.w, []):
            yield (views.EGTrainingsphase1, {'egtestquestion1': 45, 'egtestquestion2': random.randint(1, 50),
                                             'egtestquestion3': random.randint(1, 50)})
            yield (views.EGTrainingsphase2,
                       {'egtestquestion4': random.randint(1, 50), 'egtestquestion5': random.randint(1, 50),
                        'egtestquestion6': random.randint(1, 50)})
            yield (views.Letsgetstarted)
            yield (views.EGBallpreupdate,
                   {'egballquestion1': random.randint(1, 60), 'egballquestion2': random.randint(1, 40),
                    'egballquestion3': random.randint(20, 60)})
            yield (views.WTPBall1,
                   {'wtp_ball1': 20})
            yield (views.EGBallpoststrongupdate,
                   {'egballquestion4': random.randint(1, 60), 'egballquestion5': random.randint(1, 40),
                    'egballquestion6': random.randint(20, 60)})
            yield (views.WTPBall2,
                   {'wtp_ball2': 50})
            yield (views.EGBallstrongresults)
            yield (views.EGDicepreupdate,
                   {'egdicequestion1': random.randint(10, 60), 'egdicequestion2': random.randint(10, 50),
                    'egdicequestion3': random.randint(20, 60)})
            yield (views.WTPDice1,
                   {'wtp_dice1': 20})
            yield (views.EGDicepoststrongupdate,
                   {'egdicequestion4': random.randint(10, 60), 'egdicequestion5': random.randint(10, 50),
                    'egdicequestion6': random.randint(20, 60)})
            yield (views.WTPDice2,
                   {'wtp_dice2': 40})
            yield (views.EGDicestrongresults)
            yield (views.EGCloudpreupdate,
                   {'egcloudquestion1': random.randint(20, 40), 'egcloudquestion2': random.randint(20, 35),
                    'egcloudquestion3': random.randint(25, 40)})
            yield (views.WTPCloud1,
                   {'wtp_cloud1': 100})
            yield (views.EGCloudpoststrongupdate,
                   {'egcloudquestion4': random.randint(20, 40), 'egcloudquestion5': random.randint(20, 35),
                    'egcloudquestion6': random.randint(25, 40)})
            yield (views.WTPCloud2,
                   {'wtp_cloud2': 200})
            yield (views.EGCloudstrongresults)
            yield (views.EGTemperaturepreupdate, {'egtemperaturequestion1': random.randint(20, 40),
                                                      'egtemperaturequestion2': random.randint(20, 40),
                                                      'egtemperaturequestion3': random.randint(20, 40)})
            yield (views.WTPTemperature1,
                       {'wtp_temperature1':10})
            yield (views.EGTemperaturepoststrongupdate, {'egtemperaturequestion4': random.randint(20, 40),
                                                           'egtemperaturequestion5': random.randint(20, 40),
                                                           'egtemperaturequestion6': random.randint(20, 40)})
            yield (views.WTPTemperature2,
                       {'wtp_temperature2':40})
            yield (views.EGTemperaturestrongresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900', 'gender':'weiblich', 'fieldofstudy': 'Psychologie',
                                        'profession': 'Student', 'moneyathand': 'weniger als 250', 'probabilityexp1':
                                        '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1':
                                        'Ich stimme eindeutig zu', 'cse2': 'Ich stimme eindeutig zu', 'cse3':
                                        'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu', 'cse5':
                                        'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7':
                                        'Ich stimme eindeutig zu', 'cse8': 'Ich stimme eindeutig zu', 'cse9':
                                        'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu', 'cse11':
                                        'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})

        elif self.player.eg and not self.player.wu and views.page_sequence == sum(views.x, []):
            yield (views.EGTrainingsphase1, {'egtestquestion1': 45, 'egtestquestion2': random.randint(1, 50),
                                             'egtestquestion3': random.randint(1, 50)})
            yield (views.EGTrainingsphase2,
                       {'egtestquestion4': random.randint(1, 50), 'egtestquestion5': random.randint(1, 50),
                        'egtestquestion6': random.randint(1, 50)})
            yield (views.Letsgetstarted)
            yield (views.EGDicepreupdate,
                   {'egdicequestion1': random.randint(10, 60), 'egdicequestion2': random.randint(10, 50),
                    'egdicequestion3': random.randint(20, 60)})
            yield (views.WTPDice1,
                   {'wtp_dice1': 20})
            yield (views.EGDicepoststrongupdate,
                   {'egdicequestion4': random.randint(10, 60), 'egdicequestion5': random.randint(10, 50),
                    'egdicequestion6': random.randint(20, 60)})
            yield (views.WTPDice2,
                   {'wtp_dice2': 40})
            yield (views.EGDicestrongresults)
            yield (views.EGCloudpreupdate,
                   {'egcloudquestion1': random.randint(20, 40), 'egcloudquestion2': random.randint(20, 35),
                    'egcloudquestion3': random.randint(25, 40)})
            yield (views.WTPCloud1,
                   {'wtp_cloud1': 100})
            yield (views.EGCloudpoststrongupdate,
                   {'egcloudquestion4': random.randint(20, 40), 'egcloudquestion5': random.randint(20, 35),
                    'egcloudquestion6': random.randint(25, 40)})
            yield (views.WTPCloud2,
                   {'wtp_cloud2': 200})
            yield (views.EGCloudstrongresults)
            yield (views.EGTemperaturepreupdate, {'egtemperaturequestion1': random.randint(20, 40),
                                                      'egtemperaturequestion2': random.randint(20, 40),
                                                      'egtemperaturequestion3': random.randint(20, 40)})
            yield (views.WTPTemperature1,
                       {'wtp_temperature1':10})
            yield (views.EGTemperaturepoststrongupdate, {'egtemperaturequestion4': random.randint(20, 40),
                                                           'egtemperaturequestion5': random.randint(20, 40),
                                                           'egtemperaturequestion6': random.randint(20, 40)})
            yield (views.WTPTemperature2,
                       {'wtp_temperature2':40})
            yield (views.EGTemperaturestrongresults)
            yield (views.EGBallpreupdate,
                   {'egballquestion1': random.randint(1, 60), 'egballquestion2': random.randint(1, 40),
                    'egballquestion3': random.randint(20, 60)})
            yield (views.WTPBall1,
                   {'wtp_ball1': 20})
            yield (views.EGBallpoststrongupdate,
                   {'egballquestion4': random.randint(1, 60), 'egballquestion5': random.randint(1, 40),
                    'egballquestion6': random.randint(20, 60)})
            yield (views.WTPBall2,
                   {'wtp_ball2': 50})
            yield (views.EGBallstrongresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900', 'gender':'weiblich', 'fieldofstudy': 'Psychologie',
                                        'profession': 'Student', 'moneyathand': 'weniger als 250', 'probabilityexp1':
                                        '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1':
                                        'Ich stimme eindeutig zu', 'cse2': 'Ich stimme eindeutig zu', 'cse3':
                                        'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu', 'cse5':
                                        'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7':
                                        'Ich stimme eindeutig zu', 'cse8': 'Ich stimme eindeutig zu', 'cse9':
                                        'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu', 'cse11':
                                        'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})

        elif self.player.eg and not self.player.wu and views.page_sequence == sum(views.y, []):
            yield (views.EGTrainingsphase1, {'egtestquestion1': 45, 'egtestquestion2': random.randint(1, 50),
                                             'egtestquestion3': random.randint(1, 50)})
            yield (views.EGTrainingsphase2,
                       {'egtestquestion4': random.randint(1, 50), 'egtestquestion5': random.randint(1, 50),
                        'egtestquestion6': random.randint(1, 50)})
            yield (views.Letsgetstarted)
            yield (views.EGCloudpreupdate,
                   {'egcloudquestion1': random.randint(20, 40), 'egcloudquestion2': random.randint(20, 35),
                    'egcloudquestion3': random.randint(25, 40)})
            yield (views.WTPCloud1,
                   {'wtp_cloud1': 100})
            yield (views.EGCloudpoststrongupdate,
                   {'egcloudquestion4': random.randint(20, 40), 'egcloudquestion5': random.randint(20, 35),
                    'egcloudquestion6': random.randint(25, 40)})
            yield (views.WTPCloud2,
                   {'wtp_cloud2': 200})
            yield (views.EGCloudstrongresults)
            yield (views.EGTemperaturepreupdate, {'egtemperaturequestion1': random.randint(20, 40),
                                                      'egtemperaturequestion2': random.randint(20, 40),
                                                      'egtemperaturequestion3': random.randint(20, 40)})
            yield (views.WTPTemperature1,
                       {'wtp_temperature1':10})
            yield (views.EGTemperaturepoststrongupdate, {'egtemperaturequestion4': random.randint(20, 40),
                                                           'egtemperaturequestion5': random.randint(20, 40),
                                                           'egtemperaturequestion6': random.randint(20, 40)})
            yield (views.WTPTemperature2,
                       {'wtp_temperature2':40})
            yield (views.EGTemperaturestrongresults)
            yield (views.EGBallpreupdate,
                   {'egballquestion1': random.randint(1, 60), 'egballquestion2': random.randint(1, 40),
                    'egballquestion3': random.randint(20, 60)})
            yield (views.WTPBall1,
                   {'wtp_ball1': 20})
            yield (views.EGBallpoststrongupdate,
                   {'egballquestion4': random.randint(1, 60), 'egballquestion5': random.randint(1, 40),
                    'egballquestion6': random.randint(20, 60)})
            yield (views.WTPBall2,
                   {'wtp_ball2': 50})
            yield (views.EGBallstrongresults)
            yield (views.EGDicepreupdate,
                   {'egdicequestion1': random.randint(10, 60), 'egdicequestion2': random.randint(10, 50),
                    'egdicequestion3': random.randint(20, 60)})
            yield (views.WTPDice1,
                   {'wtp_dice1': 20})
            yield (views.EGDicepoststrongupdate,
                   {'egdicequestion4': random.randint(10, 60), 'egdicequestion5': random.randint(10, 50),
                    'egdicequestion6': random.randint(20, 60)})
            yield (views.WTPDice2,
                   {'wtp_dice2': 40})
            yield (views.EGDicestrongresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900', 'gender':'weiblich', 'fieldofstudy': 'Psychologie',
                                        'profession': 'Student', 'moneyathand': 'weniger als 250', 'probabilityexp1':
                                        '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1':
                                        'Ich stimme eindeutig zu', 'cse2': 'Ich stimme eindeutig zu', 'cse3':
                                        'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu', 'cse5':
                                        'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7':
                                        'Ich stimme eindeutig zu', 'cse8': 'Ich stimme eindeutig zu', 'cse9':
                                        'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu', 'cse11':
                                        'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})

        elif self.player.eg and not self.player.wu and views.page_sequence == sum(views.z, []):
            yield (views.EGTrainingsphase1, {'egtestquestion1': 45, 'egtestquestion2': random.randint(1, 50),
                                             'egtestquestion3': random.randint(1, 50)})
            yield (views.EGTrainingsphase2,
                       {'egtestquestion4': random.randint(1, 50), 'egtestquestion5': random.randint(1, 50),
                        'egtestquestion6': random.randint(1, 50)})
            yield (views.Letsgetstarted)
            yield (views.EGTemperaturepreupdate, {'egtemperaturequestion1': random.randint(20, 40),
                                                      'egtemperaturequestion2': random.randint(20, 40),
                                                      'egtemperaturequestion3': random.randint(20, 40)})
            yield (views.WTPTemperature1,
                       {'wtp_temperature1':10})
            yield (views.EGTemperaturepoststrongupdate, {'egtemperaturequestion4': random.randint(20, 40),
                                                           'egtemperaturequestion5': random.randint(20, 40),
                                                           'egtemperaturequestion6': random.randint(20, 40)})
            yield (views.WTPTemperature2,
                       {'wtp_temperature2':40})
            yield (views.EGTemperaturestrongresults)
            yield (views.EGBallpreupdate,
                   {'egballquestion1': random.randint(1, 60), 'egballquestion2': random.randint(1, 40),
                    'egballquestion3': random.randint(20, 60)})
            yield (views.WTPBall1,
                   {'wtp_ball1': 20})
            yield (views.EGBallpoststrongupdate,
                   {'egballquestion4': random.randint(1, 60), 'egballquestion5': random.randint(1, 40),
                    'egballquestion6': random.randint(20, 60)})
            yield (views.WTPBall2,
                   {'wtp_ball2': 50})
            yield (views.EGBallstrongresults)
            yield (views.EGDicepreupdate,
                   {'egdicequestion1': random.randint(10, 60), 'egdicequestion2': random.randint(10, 50),
                    'egdicequestion3': random.randint(20, 60)})
            yield (views.WTPDice1,
                   {'wtp_dice1': 20})
            yield (views.EGDicepoststrongupdate,
                   {'egdicequestion4': random.randint(10, 60), 'egdicequestion5': random.randint(10, 50),
                    'egdicequestion6': random.randint(20, 60)})
            yield (views.WTPDice2,
                   {'wtp_dice2': 40})
            yield (views.EGDicestrongresults)
            yield (views.EGCloudpreupdate,
                   {'egcloudquestion1': random.randint(20, 40), 'egcloudquestion2': random.randint(20, 35),
                    'egcloudquestion3': random.randint(25, 40)})
            yield (views.WTPCloud1,
                   {'wtp_cloud1': 100})
            yield (views.EGCloudpoststrongupdate,
                   {'egcloudquestion4': random.randint(20, 40), 'egcloudquestion5': random.randint(20, 35),
                    'egcloudquestion6': random.randint(25, 40)})
            yield (views.WTPCloud2,
                   {'wtp_cloud2': 200})
            yield (views.EGCloudstrongresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900', 'gender':'weiblich', 'fieldofstudy': 'Psychologie',
                                        'profession': 'Student', 'moneyathand': 'weniger als 250', 'probabilityexp1':
                                        '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1':
                                        'Ich stimme eindeutig zu', 'cse2': 'Ich stimme eindeutig zu', 'cse3':
                                        'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu', 'cse5':
                                        'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7':
                                        'Ich stimme eindeutig zu', 'cse8': 'Ich stimme eindeutig zu', 'cse9':
                                        'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu', 'cse11':
                                        'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})




        elif not self.player.eg and not self.player.wu and views.page_sequence == sum(views.w, []):
            yield (views.QSRTrainingsphase1, {'qsrtestquestion1': random.uniform(0, 2)})
            yield (views.QSRTrainingsphase2, {'qsrtestquestion2': random.uniform(0, 2)})
            yield (views.QSRTrainingsphase3, {'qsrtestquestion3': random.uniform(0, 2)})
            yield (views.Letsgetstarted)
            yield (views.QSRBallpreupdate,
                   {'qsrballquestion1': 0, 'qsrballquestion2': 20, 'qsrballquestion3': 60, 'qsrballquestion4': 20})
            yield (views.WTPBall1,
                   {'wtp_ball1': 5})
            yield (views.QSRBallpoststrongupdate,
                   {'qsrballquestion5': 0, 'qsrballquestion6': 0, 'qsrballquestion7': 0, 'qsrballquestion8': 100})
            yield (views.WTPBall2, {'wtp_ball2': 45})
            yield (views.QSRBallstrongresults)
            yield (views.QSRDicepreupdate,
                   {'qsrdicequestion1': 0, 'qsrdicequestion2': 20, 'qsrdicequestion3': 60, 'qsrdicequestion4': 20})
            yield (views.WTPDice1,
                   {'wtp_dice1': 10})
            yield (views.QSRDicepoststrongupdate,
                   {'qsrdicequestion5': 0, 'qsrdicequestion6': 0, 'qsrdicequestion7': 0, 'qsrdicequestion8': 100})
            yield (views.WTPDice2,
                   {'wtp_dice2': 50})
            yield (views.QSRDicestrongresults)
            yield (views.QSRCloudpreupdate,
                   {'qsrcloudquestion1': 0, 'qsrcloudquestion2': 20, 'qsrcloudquestion3': 60, 'qsrcloudquestion4': 20})
            yield (views.WTPCloud1,
                   {'wtp_cloud1': 10})
            yield (views.QSRCloudpoststrongupdate,
                   {'qsrcloudquestion5': 0, 'qsrcloudquestion6': 0, 'qsrcloudquestion7': 0, 'qsrcloudquestion8': 100})
            yield (views.WTPCloud2,
                   {'wtp_cloud2': 30})
            yield (views.QSRCloudstrongresults)
            yield (views.QSRTemperaturepreupdate,
                   {'qsrtemperaturequestion1': 0, 'qsrtemperaturequestion2': 20, 'qsrtemperaturequestion3': 60,
                    'qsrtemperaturequestion4': 20})
            yield (views.WTPTemperature1,
                   {'wtp_temperature1': 20})
            yield (views.QSRTemperaturepoststrongupdate,
                   {'qsrtemperaturequestion5': 0, 'qsrtemperaturequestion6': 0, 'qsrtemperaturequestion7': 0,
                    'qsrtemperaturequestion8': 100})
            yield (views.WTPTemperature2,
                   {'wtp_temperature2': 40})
            yield (views.QSRTemperaturestrongresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900', 'gender':'weiblich', 'fieldofstudy': 'Psychologie',
                                        'profession': 'Student', 'moneyathand': 'weniger als 250', 'probabilityexp1':
                                            '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1':
                                            'Ich stimme eindeutig zu', 'cse2': 'Ich stimme eindeutig zu', 'cse3':
                                            'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu', 'cse5':
                                            'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7':
                                            'Ich stimme eindeutig zu', 'cse8': 'Ich stimme eindeutig zu', 'cse9':
                                            'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu', 'cse11':
                                            'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})

        elif not self.player.eg and not self.player.wu and views.page_sequence == sum(views.x, []):
            yield (views.QSRTrainingsphase1, {'qsrtestquestion1': random.uniform(0, 2)})
            yield (views.QSRTrainingsphase2, {'qsrtestquestion2': random.uniform(0, 2)})
            yield (views.QSRTrainingsphase3, {'qsrtestquestion3': random.uniform(0, 2)})
            yield (views.Letsgetstarted)
            yield (views.QSRDicepreupdate,
                   {'qsrdicequestion1': 0, 'qsrdicequestion2': 20, 'qsrdicequestion3': 60, 'qsrdicequestion4': 20})
            yield (views.WTPDice1,
                   {'wtp_dice1': 10})
            yield (views.QSRDicepoststrongupdate,
                   {'qsrdicequestion5': 0, 'qsrdicequestion6': 0, 'qsrdicequestion7': 0, 'qsrdicequestion8': 100})
            yield (views.WTPDice2,
                   {'wtp_dice2': 50})
            yield (views.QSRDicestrongresults)
            yield (views.QSRCloudpreupdate,
                   {'qsrcloudquestion1': 0, 'qsrcloudquestion2': 20, 'qsrcloudquestion3': 60, 'qsrcloudquestion4': 20})
            yield (views.WTPCloud1,
                   {'wtp_cloud1': 10})
            yield (views.QSRCloudpoststrongupdate,
                   {'qsrcloudquestion5': 0, 'qsrcloudquestion6': 0, 'qsrcloudquestion7': 0, 'qsrcloudquestion8': 100})
            yield (views.WTPCloud2,
                   {'wtp_cloud2': 30})
            yield (views.QSRCloudstrongresults)
            yield (views.QSRTemperaturepreupdate,
                   {'qsrtemperaturequestion1': 0, 'qsrtemperaturequestion2': 20, 'qsrtemperaturequestion3': 60,
                    'qsrtemperaturequestion4': 20})
            yield (views.WTPTemperature1,
                   {'wtp_temperature1': 20})
            yield (views.QSRTemperaturepoststrongupdate,
                   {'qsrtemperaturequestion5': 0, 'qsrtemperaturequestion6': 0, 'qsrtemperaturequestion7': 0,
                    'qsrtemperaturequestion8': 100})
            yield (views.WTPTemperature2,
                   {'wtp_temperature2': 40})
            yield (views.QSRTemperaturestrongresults)
            yield (views.QSRBallpreupdate,
                   {'qsrballquestion1': 0, 'qsrballquestion2': 20, 'qsrballquestion3': 60, 'qsrballquestion4': 20})
            yield (views.WTPBall1,
                   {'wtp_ball1': 5})
            yield (views.QSRBallpoststrongupdate,
                   {'qsrballquestion5': 0, 'qsrballquestion6': 0, 'qsrballquestion7': 0, 'qsrballquestion8': 100})
            yield (views.WTPBall2, {'wtp_ball2': 45})
            yield (views.QSRBallstrongresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900', 'gender':'weiblich', 'fieldofstudy': 'Psychologie',
                                        'profession': 'Student', 'moneyathand': 'weniger als 250', 'probabilityexp1':
                                            '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1':
                                            'Ich stimme eindeutig zu', 'cse2': 'Ich stimme eindeutig zu', 'cse3':
                                            'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu', 'cse5':
                                            'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7':
                                            'Ich stimme eindeutig zu', 'cse8': 'Ich stimme eindeutig zu', 'cse9':
                                            'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu', 'cse11':
                                            'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})

        elif not self.player.eg and not self.player.wu and views.page_sequence == sum(views.y, []):
            yield (views.QSRTrainingsphase1, {'qsrtestquestion1': random.uniform(0, 2)})
            yield (views.QSRTrainingsphase2, {'qsrtestquestion2': random.uniform(0, 2)})
            yield (views.QSRTrainingsphase3, {'qsrtestquestion3': random.uniform(0, 2)})
            yield (views.Letsgetstarted)
            yield (views.QSRCloudpreupdate,
                   {'qsrcloudquestion1': 0, 'qsrcloudquestion2': 20, 'qsrcloudquestion3': 60, 'qsrcloudquestion4': 20})
            yield (views.WTPCloud1,
                   {'wtp_cloud1': 10})
            yield (views.QSRCloudpoststrongupdate,
                   {'qsrcloudquestion5': 0, 'qsrcloudquestion6': 0, 'qsrcloudquestion7': 0, 'qsrcloudquestion8': 100})
            yield (views.WTPCloud2,
                   {'wtp_cloud2': 30})
            yield (views.QSRCloudstrongresults)
            yield (views.QSRTemperaturepreupdate,
                   {'qsrtemperaturequestion1': 0, 'qsrtemperaturequestion2': 20, 'qsrtemperaturequestion3': 60,
                    'qsrtemperaturequestion4': 20})
            yield (views.WTPTemperature1,
                   {'wtp_temperature1': 20})
            yield (views.QSRTemperaturepoststrongupdate,
                   {'qsrtemperaturequestion5': 0, 'qsrtemperaturequestion6': 0, 'qsrtemperaturequestion7': 0,
                    'qsrtemperaturequestion8': 100})
            yield (views.WTPTemperature2,
                   {'wtp_temperature2': 40})
            yield (views.QSRTemperaturestrongresults)
            yield (views.QSRBallpreupdate,
                   {'qsrballquestion1': 0, 'qsrballquestion2': 20, 'qsrballquestion3': 60, 'qsrballquestion4': 20})
            yield (views.WTPBall1,
                   {'wtp_ball1': 5})
            yield (views.QSRBallpoststrongupdate,
                   {'qsrballquestion5': 0, 'qsrballquestion6': 0, 'qsrballquestion7': 0, 'qsrballquestion8': 100})
            yield (views.WTPBall2, {'wtp_ball2': 45})
            yield (views.QSRBallstrongresults)
            yield (views.QSRDicepreupdate,
                   {'qsrdicequestion1': 0, 'qsrdicequestion2': 20, 'qsrdicequestion3': 60, 'qsrdicequestion4': 20})
            yield (views.WTPDice1,
                   {'wtp_dice1': 10})
            yield (views.QSRDicepoststrongupdate,
                   {'qsrdicequestion5': 0, 'qsrdicequestion6': 0, 'qsrdicequestion7': 0, 'qsrdicequestion8': 100})
            yield (views.WTPDice2,
                   {'wtp_dice2': 50})
            yield (views.QSRDicestrongresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900', 'gender':'weiblich', 'fieldofstudy': 'Psychologie',
                                        'profession': 'Student', 'moneyathand': 'weniger als 250', 'probabilityexp1':
                                            '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1':
                                            'Ich stimme eindeutig zu', 'cse2': 'Ich stimme eindeutig zu', 'cse3':
                                            'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu', 'cse5':
                                            'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7':
                                            'Ich stimme eindeutig zu', 'cse8': 'Ich stimme eindeutig zu', 'cse9':
                                            'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu', 'cse11':
                                            'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})

        elif not self.player.eg and not self.player.wu and views.page_sequence == sum(views.z, []):
            yield (views.QSRTrainingsphase1, {'qsrtestquestion1': random.uniform(0, 2)})
            yield (views.QSRTrainingsphase2, {'qsrtestquestion2': random.uniform(0, 2)})
            yield (views.QSRTrainingsphase3, {'qsrtestquestion3': random.uniform(0, 2)})
            yield (views.Letsgetstarted)
            yield (views.QSRTemperaturepreupdate,
                   {'qsrtemperaturequestion1': 0, 'qsrtemperaturequestion2': 20, 'qsrtemperaturequestion3': 60,
                    'qsrtemperaturequestion4': 20})
            yield (views.WTPTemperature1,
                   {'wtp_temperature1': 20})
            yield (views.QSRTemperaturepoststrongupdate,
                   {'qsrtemperaturequestion5': 0, 'qsrtemperaturequestion6': 0, 'qsrtemperaturequestion7': 0,
                    'qsrtemperaturequestion8': 100})
            yield (views.WTPTemperature2,
                   {'wtp_temperature2': 40})
            yield (views.QSRTemperaturestrongresults)
            yield (views.QSRBallpreupdate,
                   {'qsrballquestion1': 0, 'qsrballquestion2': 20, 'qsrballquestion3': 60, 'qsrballquestion4': 20})
            yield (views.WTPBall1,
                   {'wtp_ball1': 5})
            yield (views.QSRBallpoststrongupdate,
                   {'qsrballquestion5': 0, 'qsrballquestion6': 0, 'qsrballquestion7': 0, 'qsrballquestion8': 100})
            yield (views.WTPBall2, {'wtp_ball2': 45})
            yield (views.QSRBallstrongresults)
            yield (views.QSRDicepreupdate,
                   {'qsrdicequestion1': 0, 'qsrdicequestion2': 20, 'qsrdicequestion3': 60, 'qsrdicequestion4': 20})
            yield (views.WTPDice1,
                   {'wtp_dice1': 10})
            yield (views.QSRDicepoststrongupdate,
                   {'qsrdicequestion5': 0, 'qsrdicequestion6': 0, 'qsrdicequestion7': 0, 'qsrdicequestion8': 100})
            yield (views.WTPDice2,
                   {'wtp_dice2': 50})
            yield (views.QSRDicestrongresults)
            yield (views.QSRCloudpreupdate,
                   {'qsrcloudquestion1': 0, 'qsrcloudquestion2': 20, 'qsrcloudquestion3': 60, 'qsrcloudquestion4': 20})
            yield (views.WTPCloud1,
                   {'wtp_cloud1': 10})
            yield (views.QSRCloudpoststrongupdate,
                   {'qsrcloudquestion5': 0, 'qsrcloudquestion6': 0, 'qsrcloudquestion7': 0, 'qsrcloudquestion8': 100})
            yield (views.WTPCloud2,
                   {'wtp_cloud2': 30})
            yield (views.QSRCloudstrongresults)
            yield (views.RiskAversion, {'riskaversion': 3})
            yield (views.Demographics, {'birthday': '21.01.1900', 'gender':'weiblich', 'fieldofstudy': 'Psychologie',
                                        'profession': 'Student', 'moneyathand': 'weniger als 250', 'probabilityexp1':
                                            '1', 'probabilityexp2': '5', 'probabilityexp3': 'Ja', 'cse1':
                                            'Ich stimme eindeutig zu', 'cse2': 'Ich stimme eindeutig zu', 'cse3':
                                            'Ich stimme eindeutig zu', 'cse4': 'Ich stimme eindeutig zu', 'cse5':
                                            'Ich stimme eindeutig zu', 'cse6': 'Ich stimme eindeutig zu', 'cse7':
                                            'Ich stimme eindeutig zu', 'cse8': 'Ich stimme eindeutig zu', 'cse9':
                                            'Ich stimme eindeutig zu', 'cse10': 'Ich stimme eindeutig zu', 'cse11':
                                            'Ich stimme eindeutig zu', 'cse12': 'Ich stimme eindeutig zu'})

