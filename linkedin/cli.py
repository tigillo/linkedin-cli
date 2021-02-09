import re
import logging

logger = logging.getLogger(__name__)

class InvalidCommandException(Exception):
    pass


class CLI:
    def __init__(self):
        self.commands = [
            {"name": "help", "pattern": r'^help$', "module":"linkedin.commands.help", "klass": "HelpCommand"},
            {"name": "version", "pattern": r'^version$', "module":"linkedin.commands.version", "klass": "VersionCommand"},
            {"name": "login.help", "pattern": r'^login help$', "module":"linkedin.commands.login", "klass": "HelpCommand"},
            {"name": "login", "pattern": r'^login$', "module":"linkedin.commands.login", "klass": "LoginCommand"},
            {"name": "config.set.application", "pattern": r'^config set application$', "module":"linkedin.commands.config", "klass": "SetApplicationConfigCommand"},
            {"name": "me", "pattern": r'^me$', "module":"linkedin.commands.me", "klass": "MeCommand"},
            {"name": "post.help", "pattern": r'^post help$', "module":"linkedin.commands.post", "klass": "HelpCommand"},
            {"name": "post.public", "pattern": r'^post -v=public', "module":"linkedin.commands.post", "klass": "PostPublicCommand"},
            {"name": "post.public", "pattern": r'^post --visibility=public', "module":"linkedin.commands.post", "klass": "PostPublicCommand"},
            {"name": "post.connections", "pattern": r'^post -v=connections', "module":"linkedin.commands.post", "klass": "PostConnectionsCommand"},
            {"name": "post.connections", "pattern": r'^post --visibility=connections', "module":"linkedin.commands.post", "klass": "PostConnectionsCommand"},
            {"name": "post", "pattern": r'^post', "module":"linkedin.commands.post", "klass": "PostConnectionsCommand"},
        ]

    def execute(self, args):
        command_str = ' '.join(args)
        logger.debug("Command string: " + command_str)
        for command in self.commands:
            p = re.compile(command["pattern"])
            if p.match(command_str):
                klass = self.load(command["module"], command["klass"])
                kommand = klass()
                kommand.execute(args)
                return
        klass = self.load('linkedin.commands.help', 'HelpCommand')
        kommand = klass()
        kommand.execute("")
        raise InvalidCommandException()

    def load(self, module, klass):
        module = __import__(module, fromlist=[klass])
        klass = getattr(module, klass)
        return klass
