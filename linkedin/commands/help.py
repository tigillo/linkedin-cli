import linkedin.commands.command as command


class HelpCommand(command.BaseCommand):

    @staticmethod
    def message():
        return """usage: linkedin <command> [<args?]

These are common linkedin commands used in various situations:

    config       Get and set linkedin-cli options
    login        Login with a user for api access
    me           Display logged in user details
    post         Share a post

Other commands

    help         Print help (this message)
    version      Print the version information
"""

    def execute(self, args):
        print(HelpCommand.message())
