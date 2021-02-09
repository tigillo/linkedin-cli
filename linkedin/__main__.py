import sys
import linkedin.cli
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
root = logging.getLogger()
handler = root.handlers[0]
fmt = logging.Formatter('%(levelname)s: %(message)s')
handler.setFormatter(fmt)

def main():
    try:
        argv_start = 1
        debug = False
        if "--debug" in sys.argv:
            root.setLevel(logging.DEBUG)
            debug = True
            i = sys.argv.index("--debug")
            del sys.argv[i]
            logger.debug("Running in debug mode")

        cli = linkedin.cli.CLI()
        cli.execute(sys.argv[argv_start:])
        sys.exit(0)
    except linkedin.cli.InvalidCommandException as e:
        sys.exit(1)
    except Exception as e:
        logger.error(e, exc_info=debug)
        sys.exit(1)

main()
