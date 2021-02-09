import linkedin.commands.command as command
import linkedin.resources.version as version


class VersionCommand(command.BaseCommand):
    @staticmethod
    def version():
        return "linkedin-cli version " + version.VERSION

    def execute(self, args):
        print(VersionCommand.version())
