import linkedin.commands.command as command
import linkedin.utils.config as config
import logging
from getpass import getpass

logger = logging.getLogger(__name__)


class HelpCommand(command.BaseCommand):
    def execute(self, args):
        print("""usage: linkedin config [command]
        
        Available commands:
            set application
        """)


class SetApplicationConfigCommand(command.BaseCommand):
    def execute(self, args):
        client_id = input("Enter your linkedin application client id: ") 
        client_secret = getpass("Enter your linkedin application client secret: ") 
        config.getConfig().setApplication(client_id, client_secret)
