"""
Steamlink Launcher for Kodi
"""

import os
import xbmc
import xbmcgui
import xbmcaddon

from subprocess import check_call

class KodiAddon(object):
    def __init__(self):
        self._addon = xbmcaddon.Addon()
        # self.path = self._addon.getAddonInfo('path').decode('utf-8')
        self.path = self._addon.getAddonInfo('path')
        # self.path = os.path.dirname(os.path.realpath(__file__))
    
    def run(self):
        check_call(['bash', self.path + '/resources/lib/start.sh'])

def main():
    addon = KodiAddon()
    addon.run()

main()
