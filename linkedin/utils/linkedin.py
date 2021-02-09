import json
import linkedin.utils.config as config
import logging
from urllib import request, parse


logger = logging.getLogger(__name__)


class MemberNetworkVisibility():
    CONNECTIONS = "CONNECTIONS"
    PUBLIC = "PUBLIC"


class Linkedin():
    def post(self, visibility, content):
            data = {
                        'author': config.getConfig().CONFIG['urn'],
                        'lifecycleState': 'PUBLISHED',
                        'specificContent': {
                            'com.linkedin.ugc.ShareContent': {
                                'shareCommentary': {
                                    'text': content
                                },
                                'shareMediaCategory': 'NONE'
                            }
                        },
                        'visibility': {
                            'com.linkedin.ugc.MemberNetworkVisibility': visibility
                        }
                    }
            logger.debug(data)
            data=json.dumps(data).encode('utf-8')
            url = "https://api.linkedin.com/v2/ugcPosts"
            req = request.Request(url, data=data, headers={'Content-Type':'application/json', 'Authorization': 'Bearer ' + config.getConfig().CONFIG['access_token']})
            response = request.urlopen(req)
            logger.debug("Response code: " + str(response.getcode()))
            logger.info("Post sent!")
