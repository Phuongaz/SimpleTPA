# -*- encoding: utf-8 -*-
"""
Simple tpa plugin for nukkit (PyPlugins) test
"""

from cn.nukkit.plugin import PluginBase
from cn.nukkit import Player

tpa_list = {}

class SimpleTPA(PluginBase):

	def onEnable(self):
		self.getServer().getLogger().info("SimpleTPA enable \n\n\n\n");
	
	def onCommand(self, sender, cmd, label, args):
		if cmd.getName() == "tpa":
			self.send_request(player=sender, target_name=str(args[0]))
		if cmd.getName() == "tpaccept":
	 		self.tp_accept(player=sender)

	def send_request(self, player, target_name):
		target = self.getServer().getPlayer(target_name)
		if self.getServer().getPlayer(target_name) is not None:
			target = self.getServer().getPlayer(target_name)
			target.sendMessage("player " + player.getName() + " wants to teleport to you\n /tpaccept to agree")
			tpa_list[target_name] = player.getName()
		else:
			player.sendMessage("Player " + target_name + " not found")

	def tp_accept(self, player):
		if player.getName() in tpa_list:
			target_name = tpa_list.get(player.getName())
			target = self.getServer().getPlayer(target_name)
			if target is not None:
				target.teleport(player)
				target.sendMessage("Teleport to " + player.getName())
				tpa_list.pop(player.getName())
			else:
				player.sendMessage("Player " + target_name + " offline, cancel request")
				tpa_list.pop(player.getName())
		else:
			player.sendMessage("You don't have any tp request")