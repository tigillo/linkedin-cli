import json
import linkedin.commands.command as command
import linkedin.utils.linkedin as linkedin
import logging


logger = logging.getLogger(__name__)


class HelpCommand(command.BaseCommand):
    def execute(self, args):
        print("usage: linkedin post [-options] \"content ...\"")
        print("""
        Options:
            -v, --visibility=connections: When sharing, set visibility as connections or public (default share with connections).
        """)


class PostConnectionsCommand(command.BaseCommand):
    def execute(self, args):
        content = args[-1]
        linkedin.Linkedin().post(linkedin.MemberNetworkVisibility.CONNECTIONS, content)

class PostPublicCommand(command.BaseCommand):
    def execute(self, args):
        content = args[-1]
        linkedin.Linkedin().post(linkedin.MemberNetworkVisibility.PUBLIC, content)

