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

# <premium imports>
from scipy.stats import rankdata
import numpy as np
# </premium imports>

author = 'Curtis Kephart'

doc = """
CSR Experiment
This experiment ...
Designed by Chetan Dave and Alicja Reuben.
First implementation by Curtis Kephart (curtiskephart@gmail.com) 2016.11
"""

class Constants(BaseConstants):
    name_in_url = 'csr_vcm_wg'
    players_per_group = 4
    task_timer = 30
    num_rounds = 11 # otree variable
    vcm_rounds = 9  # number of vcm rounds. can pull from settings.py
    automatic_earnings = 120



class Subsession(BaseSubsession):
	def before_session_starts(self):
		# how long is the real effort task time?
		# refer to settings.py settings.
		cnt = 1
		for p in self.get_players():

			p.participant.vars['id_in_subsession'] = cnt
			cnt = cnt + 1

			if 'vcm_round_count' in self.session.config:
			    p.participant.vars['vcm_round_count'] = self.session.config['vcm_round_count']
			    vcm_round_count = self.session.config['vcm_round_count']
			    self.session.vars['vcm_round_count'] = vcm_round_count
			else:
				p.participant.vars['vcm_round_count'] = Constants.vcm_rounds
				self.session.vars['vcm_round_count'] = Constants.vcm_rounds


		paid_round = random.randint(1,vcm_round_count) #pick paid round
		for p in self.get_players():
			p.participant.vars['paid_round'] = paid_round
			p.mpcr = self.session.config['mpcr']


		self.group_randomly()




class Group(BaseGroup):
	pass


class Player(BasePlayer):

	vcm_round = models.PositiveIntegerField(
		doc='The vcm round number.'
		)

	individual_exchange = models.FloatField(
		initial=None,
		verbose_name='Individual exchange:',
		doc="Individual exchange contribution in this round")

	group_exchange = models.FloatField(
		initial=None,
		verbose_name='Group exchange:',
		doc="Group exchange contribution in this round")

	group_exchange_percent = models.FloatField(
		min = 1, max = 100,
		blank=True, #not required
		doc="in this round, this subject's percent contribution to group exchange relative to total amount availale to user",
		widget=widgets.SliderInput(
			attrs={'step': '1','value':'5'}))


	total_op_individual_exchange = models.FloatField(
		doc='total individual_exchange contributions of opposing players'
		)

	total_op_group_exchange = models.FloatField(
		doc='total group_exchange contributions of opposing players'
		)

	mpcr = models.FloatField(
		doc="marginal per-capita rate of return to vcm game")
	
	round_points = models.FloatField(
		doc='Points earned this round from the VCM'
		)

	player_role = models.CharField(
		doc="player type, A or F"
		)

	player_role_list = models.CharField(
		doc="list of all player roles after assignment. index 0 -> P1, index 1 -> P2"
		)

	paid_round = models.PositiveIntegerField(
		doc='vmc period that is paid on')

	final_score = models.FloatField(
		doc="this palyer's final score in this round")

	final_avg_ge = models.FloatField(
		doc="this player's final average group exchange contribution over all rounds")




	def set_payoffs(self):
		"""calc player payoffs"""
		self.total_op_individual_exchange = sum([p.individual_exchange for p in self.get_others_in_group()])
		self.total_op_group_exchange = sum([p.group_exchange for p in self.get_others_in_group()])

		self.round_points = self.individual_exchange + (0 * self.total_op_individual_exchange) + (self.mpcr * self.total_op_group_exchange) + (self.mpcr * self.group_exchange)





	def set_roles(self, overall_ge_percent_list):
		"""set player roles"""

		own_id_index = self.participant.vars['id_in_subsession'] - 1

		# rank players (globally) by group exchange contribution
		self.participant.vars['GE_Rank_list'] = ((rankdata(np.array(overall_ge_percent_list), method='ordinal'))).tolist()
		self.participant.vars['GE_Rank'] = ((rankdata(np.array(overall_ge_percent_list), method='ordinal'))).tolist()[own_id_index]

		# type cutoff rank
		cufoff_F = max(p.participant.vars['id_in_subsession'] for p in self.subsession.get_players() if p.group_exchange_percent != None) / 2

		# details...
		if (self.participant.vars['GE_Rank'] > cufoff_F):
		    self.player_role = self.participant.vars['Role'] = "A"
		else:
		    self.player_role = self.participant.vars['Role'] = "A" #SH was F

		# set player_role_list, a log of each player's role
		player_role_list = []
		for id_ in range(0,len(overall_ge_percent_list)):
			if (rankdata(np.array(overall_ge_percent_list), method='ordinal').tolist()[id_] > cufoff_F):
			    player_role_list.append("A")
			else:
			    player_role_list.append("A") #SH was F

		self.player_role_list = self.participant.vars['player_role_list'] = player_role_list #just for debugging, might delete  self.participant.vars['player_role_list'] later.

		#this is the key var passed to stage game.
		self.participant.vars['player_role_list'] = player_role_list #used to get roles in stage game.
		self.participant.vars['overall_ge_percent_list'] = overall_ge_percent_list
		self.final_avg_ge = self.participant.vars['overall_ge_percent'] = overall_ge_percent_list[own_id_index]
		self.participant.vars['overall_own_ge'] = overall_ge_percent_list[own_id_index] * self.participant.vars["ret_score"]
