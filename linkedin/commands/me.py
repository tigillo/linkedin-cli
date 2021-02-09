import json
import linkedin.commands.command as command
import linkedin.utils.config as config
import logging
from urllib import request


logger = logging.getLogger(__name__)


class HelpCommand(command.BaseCommand):
    def execute(self, args):
        print("usage: linkedin me")


class MeCommand(command.BaseCommand):
    def execute(self, args):
        url = "https://api.linkedin.com/v2/me"
        req = request.Request(url, headers={'Authorization': 'Bearer ' + config.getConfig().CONFIG['access_token']})
        response = request.urlopen(req)
        user = json.loads(response.read())
        print("ID: " + user["id"],)
        print("First Name: " + user['localizedFirstName'])
        print("Last Name: " + user['localizedLastName'])


