# main.py

import network_scripts
import information_gathering
import json

class Main():

    def __init__(self):
        pass

    def do_work(self):
        # get login information to use, create instance of GetCredentials class
        get_credentials = information_gathering.GetCredentials()
        # see if we're using the same creds for all devices
        same_creds = str(get_credentials.ask_if_same_creds()).lower()
        # if 'y' then lets just get the username/password now
        if same_creds == 'y':
            username = get_credentials.get_username()
            password = get_credentials.get_password()
            credentials_dictionary = { 'fortinet_username': username,
                                'fortinet_password': password,
                                'ruckus_username': username,
                                'ruckus_password': password
                                }
        else:
            # if the credentials are NOT the same for all devices we need to get them
            credentials_dictionary = { 'fortinet_username':
                                        get_credentials.get_username(device='fortinet'),
                                    'fortinet_password':
                                        get_credentials.get_password(device='fortinet'),
                                    'ruckus_username':
                                        get_credentials.get_username(device='ruckus switches'),
                                    'ruckus_password':
                                        get_credentials.get_password(device='ruckus switches')
                                }
        # now that we have credentials lets connect in to get info
        # temp to have this data right here
        # open as type terminal_server so we can send an 'a' to accept the banner
        fortinet_info = {
            'device_type': 'terminal_server',
            'host': '172.31.1.1',
            'username': credentials_dictionary['fortinet_username'],
            'password': credentials_dictionary['fortinet_password']
        }
        fortinet_connection = network_scripts.FortinetTshooting()
        # get output from the commands
        fortinet_output = fortinet_connection.connect_and_do_work(**fortinet_info)
        #print(json.dumps(fortinet_output, indent=1, sort_keys=True))
        for key, value in fortinet_output.items():
            print(key)
            print(value)


if __name__ == '__main__':
    main = Main()
    main.do_work()