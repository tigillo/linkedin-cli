
import os
import json
import logging

logger = logging.getLogger(__name__)

class getConfig:
    def __init__(self):
        self.CONFIG_DIR = os.path.join(os.getenv("HOME"), ".linkedin")
        self.CONFIG_FILE = os.path.join(self.CONFIG_DIR, "config.json")
        self.CONFIG = {}
        self.CONFIG['application'] = {}
        self.CONFIG['application']['client_id'] = ""
        self.CONFIG['application']['client_secret'] = ""
        self.CONFIG['access_token'] = ""
        self.CONFIG['port'] = 4625
        self.CONFIG['urn'] = ""
        self.AUTH_URL = ""
        try:
            with open(self.CONFIG_FILE) as json_file:
                config = json.load(json_file)
                self.CONFIG.update(config)
                self.AUTH_URL=("https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id="
                    + self.CONFIG['application']['client_id']
                    + "&redirect_uri=http%3A%2F%2Flocalhost%3A"
                    + str(self.CONFIG['port'])
                    + "&scope=r_liteprofile%20r_emailaddress%20w_member_social")
                self.REDIRECT_URL="http://localhost:" + str(self.CONFIG['port'])
        except FileNotFoundError:
            logger.error("Config file not found: '" + self.CONFIG_FILE + "'")

    def setApplication(self, client_id, client_secret):
        self.CONFIG['application']['client_id'] = client_id
        self.CONFIG['application']['client_secret'] = client_secret
        self.saveConfig()
        logger.info("Application configured")

    def setAccessToken(self, access_token):
        self.CONFIG['access_token'] = access_token
        self.saveConfig()
        logger.info("Access token configured")

    def setUrn(self, id):
        self.CONFIG['urn'] = "urn:li:person:" + id
        self.saveConfig()
        logger.info("User URN configured")

    def saveConfig(self):
        try:
            os.mkdir(self.CONFIG_DIR)
        except FileExistsError:
            pass
        with open(self.CONFIG_FILE, 'w') as outfile:
            json.dump(self.CONFIG, outfile, sort_keys=True, indent=2)
