import http.server
import os
import json
import linkedin.commands.command as command
import linkedin.utils.config as config
import logging
import webbrowser
from urllib import request, parse


logger = logging.getLogger(__name__)

class LoginRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        parsed_query = parse.parse_qsl(parsed_path.query)
        query_key = parsed_query[0][0]
        query_value = parsed_query[0][1]
        if query_key == "error":
            description = parsed_query[1][1]
            logger.error(description)
            self.send_response(307)
            self.send_header('Location','https://tigillo.com/error?error=' + query_value + '&description='+description)   
        elif query_key == "code":
            logger.debug("Authorization allowed")
            logger.debug("Authorization code:" + query_value)
            url = "https://www.linkedin.com/oauth/v2/accessToken"
            data = {'grant_type': 'authorization_code', 'code': query_value, 'redirect_uri': config.getConfig().REDIRECT_URL, 'client_id': config.getConfig().CONFIG['application']['client_id'], 'client_secret': config.getConfig().CONFIG['application']['client_secret']}
            data = parse.urlencode(data).encode()
            req = request.Request(url, data=data)
            response = request.urlopen(req)
            access_token = json.loads(response.read())['access_token']
            config.getConfig().setAccessToken(access_token)
                
            url = "https://api.linkedin.com/v2/me"
            req = request.Request(url, headers={'Authorization': 'Bearer ' + config.getConfig().CONFIG['access_token']})
            response = request.urlopen(req)
            user = json.loads(response.read())
            config.getConfig().setUrn(user["id"])
            self.send_response(307)
            self.send_header('Location','https://linkedin-cli.tigillo.com/success')
        else:
            description = "Unsupported response from linkedin"
            logger.error(description)
            self.send_response(307)
            self.send_header('Location','https://linkedin-cli.tigillo.com/error?error=' + query_value + '&description='+description)   
        self.end_headers()
        self.connection.close()

    def log_message(self, format, *args):
        return


class HelpCommand(command.BaseCommand):
    def execute(self, args):
        print("usage: linkedin login")


class LoginCommand(command.BaseCommand):
    def execute(self, args):
        webbrowser.open(config.getConfig().AUTH_URL)
        httpd = http.server.HTTPServer(('', 4625), LoginRequestHandler)
        httpd.socket.settimeout(120)
        httpd.handle_request()

