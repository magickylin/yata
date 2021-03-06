"""
Copyright 2019 kivou.2000607@gmail.com

This file is part of yata.

    yata is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    yata is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with yata. If not, see <https://www.gnu.org/licenses/>.
"""

from bot.models import DiscordApp

import json


def saveBotsConfigs():
    for bot in DiscordApp.objects.all():
        var = dict({})
        # loop on configuration helpers attached to the bot
        for guild in bot.guild_set.all():
            var[guild.guildId] = dict({})
            var[guild.guildId]["admin"] = {"name": guild.guildName,
                                           "owner": guild.guildOwnerName,
                                           "owner_id": guild.guildOwnerId,
                                           "contact": guild.guildContactName,
                                           "contact_id": guild.guildContactId}

            # allowed channels
            if guild.allowedChannels:
                var[guild.guildId]["admin"]["channels"] = json.loads(guild.allowedChannels)

            # allowed roles
            if guild.allowedRoles:
                var[guild.guildId]["admin"]["roles"] = json.loads(guild.allowedRoles)

            # manage channels
            if guild.manageChannels:
                var[guild.guildId]["channels"] = {"active": True}

            # loot module
            if guild.lootModule:
                var[guild.guildId]["loot"] = {"active": True}

            # stocks
            if guild.stockModule:
                var[guild.guildId]["stocks"] = {"active": True}
                if guild.stockWSSB:
                    var[guild.guildId]["stocks"]["wssb"] = True
                if guild.stockTCB:
                    var[guild.guildId]["stocks"]["tcb"] = True
                if guild.stockChannel:
                    var[guild.guildId]["stocks"]["channel"] = guild.stockChannel
                if guild.stockAlerts:
                    var[guild.guildId]["stocks"]["alerts"] = True

            # chain
            if guild.chainModule:
                var[guild.guildId]["chain"] = {"active": True}

            # repository
            if guild.repoModule:
                var[guild.guildId]["repository"] = {"active": True, "name": guild.repoName, "token": guild.repoToken}

            # verify
            if guild.verifyModule:
                var[guild.guildId]["verify"] = {"active": True}
                if guild.verifyForce:
                    var[guild.guildId]["verify"]["force"] = True
                if guild.verifyFacsRole:
                    var[guild.guildId]["verify"]["common"] = guild.verifyFacsRole
                var[guild.guildId]["factions"] = dict({f.tId: f.name for f in guild.verifyFactions.all()})

            # loop over yata users to get their keys
            if len(guild.masterKeys.all()):
                var[guild.guildId]["keys"] = dict({p.tId: p.key for p in guild.masterKeys.all() if p.botPerm})

        bot.variables = json.dumps(var)
        bot.save()
