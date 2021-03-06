# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

# </standard imports>



author = 'Curtis Kephart'

doc = """
CSR Experiment
This experiment ...
Designed by Chetan Dave and Alicja Reuben.
First implementation by Curtis Kephart (curtiskephart@gmail.com) 2016.11
Last modified 12 Nov 2017 by Sjur Hamre
"""

class Constants(BaseConstants):
    name_in_url = 'csr_realEffort'
    players_per_group = None
    task_timer = 300 #Changed to 5 mins
    num_rounds = 500 #Changed to 500


    reference_texts = [
        'uIzR',
        'o8sA',
        'dWg5',
        '6kdA',
        'ep7o',
        'zflY',
        'CwNg',
        'OhZn',
        'Xw0w',
        'GJcR',
        'OJ2D',
        'kJ03',
        'L5O8',
        '1MUj',
        'GleS',
        '4gKx',
        'mSol',
        'oWKd',
        'OFFz',
        'CdsT',
        'Mf4U',
        'sUhJ',
        '1Ltw',
        '2mrm',
        'f5UI',
        'hNqN',
        'boJa',
        '2Pqv',
        'vLuq',
        'IYYP',
        'sy3O',
        'M9X6',
        'qflm',
        'ovAU',
        '7PaW',
        'YB4F',
        '2NFP',
        'h6QM',
        'xLkH',
        'izif',
        'r7Ml',
        'ERJ8',
        'geTe',
        'L15N',
        'uTKl',
        'wRuQ',
        'MFNc',
        'YS4B',
        '80uw',
        'syXc',
        'QgvI',
        'a5bk',
        'MqCQ',
        'E0Qi',
        'NzsZ',
        '1maT',
        'mN28',
        'BJet',
        'xBhz',
        'rkn7',
        '5r3d',
        'uTM0',
        'pYQD',
        'Rkn1',
        'FJIv',
        'pZMh',
        'GobN',
        'oVis',
        '3V4w',
        'zWtd',
        '5OZz',
        'ArfP',
        'IdzS',
        'mC9T',
        '7cIv',
        'TjcG',
        'fZ15',
        'NlsB',
        'tPX4',
        '3O3c',
        'HLTg',
        'de14',
        'MbqN',
        'xywd',
        'Z3Vz',
        'XS7V',
        'ErGB',
        'HlTl',
        '9Dmt',
        'LCwT',
        'y97e',
        '6PTp',
        'vCVC',
        'MG3S',
        'kzpF',
        'Y90Z',
        'WSx7',
        '6gt6',
        '8gkm',
        'tz4h',
        'SY3B',
        'FAoj',
        '7Hoe',
        'TXVU',
        'Ig6h',
        'Lk5b',
        'bRsi',
        'jY3X',
        'e3Hs',
        'NMtM',
        'O2lG',
        'rkeg',
        'Cs7Y',
        'GpZT',
        'EJB4',
        'zRAy',
        'GSyi',
        'fZPn',
        'Cuw7',
        '7JAO',
        'BXVX',
        '7zQT',
        'M8Xx',
        'Bv4j',
        '3wdv',
        'V4x7',
        'VGcm',
        'G0VE',
        'iBvg',
        'jONE',
        'QbZh',
        'tqEd',
        '7aQa',
        'dPnk',
        'XELX',
        'H58o',
        'rlY7',
        '2DYz',
        'agK2',
        '2LNn',
        'XBcS',
        'vuss',
        'zY5r',
        'SRUA',
        'lkXq',
        'WiH6',
        'c7E6',
        '5myK',
        '8Cdl',
        'iIzV',
        '8waN',
        'fiFQ',
        'A2Ij',
        '9Wh9',
        'ciYB',
        'RICk',
        'JpFl',
        'RtHn',
        'pfS1',
        '2Kl5',
        'hsTV',
        'Y9Zt',
        'Nztu',
        'xFVr',
        'oa33',
        'iwVO',
        'HjS3',
        'purH',
        '3XCx',
        'b679',
        'pgJW',
        'swlp',
        'lwza',
        '5BK8',
        'GSzx',
        'bdNs',
        'TgEy',
        'GzCu',
        'yT7e',
        '6Q9F',
        'QHdk',
        '1rZK',
        'g4TE',
        'ANns',
        'yayS',
        'eiqM',
        'NlLZ',
        'nz8F',
        'yslg',
        'VWbF',
        'csMn',
        'CL1B',
        'v6fm',
        'UUYo',
        'kKJm',
        'K9JE',
        'j1Q8',
        'EfhZ',
        'mIvE',
        'g1aG',
        'tBIl',
        'M8qe',
        'cDGx',
        'Bvl0',
        '5IDN',
        'bs8F',
        'CAZM',
        'ejFC',
        'JoUu',
        '4J6n',
        'eW1H',
        'u4M7',
        'onjT',
        'YlWg',
        'Lard',
        'wTow',
        'MOP1',
        'AffL',
        'pwap',
        '55xM',
        'Hpnz',
        'A9WR',
        'KbAB',
        'Ovbl',
        'H0jE',
        'D4TY',
        'zKDl',
        'BCr7',
        'vkf4',
        'viEN',
        'kBe8',
        'eDfT',
        'fJWx',
        'GD7j',
        'Di1J',
        'dA0w',
        '83DI',
        'waza',
        'Jtt2',
        'hvoV',
        'ZgSt',
        '5HhV',
        'SJeR',
        'jPuO',
        'DWih',
        '5jmT',
        'HbRe',
        'GvGX',
        'ODkL',
        'LQTO',
        '2R4L',
        'Mq4M',
        'sSne',
        'HBbk',
        'Ges7',
        'UgLx',
        'ep8B',
        'ieBS',
        'CDVn',
        'eDIx',
        'iwhU',
        '7IYW',
        'QOBv',
        'PgMP',
        'tX1S',
        'kZ1I',
        '2oHt',
        'pPH8',
        'pS5B',
        'tbhG',
        'h98I',
        'byxG',
        'ijmR',
        '55Kv',
        'S6TV',
        '68aI',
        'sW8x',
        'UhER',
        '0KWd',
        'wZ7I',
        '7XCS',
        'LIvc',
        'gp3j',
        'Iu5z',
        'klTK',
        'h4oR',
        'Idld',
        'im17',
        'NRZI',
        'WCsA',
        'B0q8',
        'Kzzq',
        '1SJz',
        '4EIt',
        'OqRS',
        '8DLn',
        'k4RH',
        '7zYJ',
        'HuCS',
        'jGs1',
        'vBTJ',
        'VcD4',
        'UVy3',
        'KvhX',
        '6PmP',
        'qFEX',
        'X1En',
        'zk3M',
        'md9Z',
        'UW4f',
        'LUkk',
        'GNcG',
        'ioLd',
        'A89k',
        'pn8W',
        'JWTg',
        '1oRT',
        'AvTt',
        'isA1',
        'G0Bj',
        'l9nH',
        'ihgh',
        'qZQQ',
        'ka5w',
        'UrSm',
        'e28z',
        'Z4zW',
        'I3M7',
        'lcac',
        '89oO',
        'wkeb',
        'AONe',
        'kCHz',
        '6xTm',
        '5CL1',
        '9fYU',
        'YgRh',
        'VzJD',
        'k8Xt',
        'PMhh',
        'cH3N',
        'h4j7',
        'AayV',
        'hQ0E',
        'SsVT',
        'NuKa',
        'fqXR',
        'I4NN',
        'EATg',
        'JFLx',
        'qE0V',
        '8uPZ',
        'OL91',
        'ww58',
        'atBe',
        'Wn95',
        'g0vf',
        'MTLf',
        'KcWN',
        'cYw7',
        '0rLp',
        'dvyH',
        'Pgql',
        '8p0j',
        'KmDJ',
        'r5F2',
        'Iqw7',
        'hNKi',
        'bxmT',
        'IWjC',
        'Xzbu',
        '2tjq',
        'AFu2',
        'aoO9',
        'lcZk',
        '4Pqn',
        'GDPt',
        'zeIM',
        'LMzw',
        'QqEa',
        'W1qs',
        'A4Ae',
        'nwl9',
        'qyFc',
        'F5F6',
        'svSE',
        '2kfx',
        'B1xM',
        'Hv1d',
        '2LpO',
        'O9w4',
        'IF1G',
        '5Rhm',
        'KTln',
        'fUS4',
        'M6ln',
        'enb9',
        'PUc8',
        'HApV',
        'NFPw',
        'J8JI',
        'CsVo',
        'z4jL',
        'cQ55',
        'rVuY',
        '6iah',
        'jOn9',
        '7LdX',
        'ZmZ6',
        'UL74',
        'OdnL',
        'm4bF',
        'd6NR',
        'AOKH',
        'Oukg',
        'h0qG',
        'nMO0',
        'whvz',
        'iDhA',
        'db5I',
        'YD7C',
        'gFpm',
        'XNxS',
        'Nnc7',
        'c4qW',
        'KS42',
        'qd1V',
        'P9iE',
        'I5iJ',
        '18WP',
        'YXVQ',
        'QEhD',
        'qf5r',
        'neUQ',
        'wEsa',
        'o0Wx',
        'lCnH',
        'ImwE',
        '6pvD',
        'jYlO',
        'dldX',
        'Ovhq',
        'RTh4',
        'KQni',
        '5Ckv',
        '13fb',
        '95Lb',
        'a2Jr',
        's7v3',
        'o7jI',
        'cATc',
        'TIgo',
        'awCp',
        'zrei',
        'OLVc',
        '3Z3j',
        'AoZT',
        'ensw',
        'PdRq',
        'y48F',
        '4WCm',
        'eL5l',
        'Nq2n',
        'T0HZ',
        'iJbC',
        'Z6Bt',
        '8KiW',
        'myZJ',
        '1nY6',
        '4ysn',
        '9vNR',
        'NfrQ',
        'qMVC',
        'fFJK',
        'nEti',
        '6NBv',
        'pRam',
        'mwZa',
        'tL5o',
        'yQtB',
        'YMK2',
        'Tvwk',
        'W3hi',
        'gT6R',
        'k9KB',
        'Xrox',
        '6LcQ',
        'fuVE',
        'GTbY',
        '6vJu',
        'O4iC',
        'etBY',
        'SwLb',
        '2J3s',
        'UNC2',
        'bE0g',
        'Gltu',
        'zvXA',
        '86v5',
        '91yy'
	]




class Subsession(BaseSubsession):
	def before_session_starts(self):

		# how long is the real effort task time?
		# refer to settings.py settings.
		for p in self.get_players():
		    if 'ret_time' in self.session.config:
		        p.ret_timer = self.session.config['ret_time']
		    else:
		        p.ret_timer = Constants.task_timer


class Group(BaseGroup):
	pass

class Player(BasePlayer):


	ret_timer = models.PositiveIntegerField(
	    doc="""The length of the real effort task timer."""
	)
	user_text = models.CharField(
		doc="user's transcribed text")
	is_correct = models.BooleanField(
		doc="did the user get the task correct?")
	ret_final_score = models.IntegerField(
		doc="player's total score up to this round")
	round_payoff = models.FloatField(
		doc="total number of correct real effort tasks, completed before timer expired")




	def set_final_score(self):
		correct_cnt = 0
		for p in self.in_all_rounds():
			if p.round_payoff != None:
				correct_cnt = correct_cnt + p.round_payoff
			else:
				correct_cnt = correct_cnt + 0

		if correct_cnt == None:
			self.ret_final_score = 20
		elif (correct_cnt < 10):
			self.ret_final_score = 2 + (2 * correct_cnt)
		else:
			self.ret_final_score = 20
