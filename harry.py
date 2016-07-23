#!/usr/bin/env python3

from errbot import BotPlugin, botcmd


class Harry(BotPlugin):
    """call in the harry (german humor)
    """


    @botcmd()
    def harry(self, msg, args):
        """ harry is on its way!!!
        """
        url = 'https://cdn.meme.am/instances/61688577.jpg'
        return url