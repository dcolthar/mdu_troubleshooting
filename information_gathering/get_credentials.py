import getpass

class GetCredentials():

    def __init__(self):
        pass

    def ask_if_same_creds(self):
        '''
        Prompt to see if we should use the same credentials for all devices
        :return: same_creds - will be a y or n determining if we should use same info for all devices to login
        '''
        same_creds = input('use same credentials for each device? y or n?:\n')
        return same_creds

    def get_username(self,
                     device = 'all devices'):
        '''
        Prompt for a username for the connection
        :return: username - the username that was received
        '''
        username = input('enter a username to use for {device}:\n'.format(device=device))
        return username

    def get_password(self,
                     device = 'all devices'):
        '''
        Prompt for a password for the connection
        :return: password - the password that was received from getpass
        '''
        password = getpass.getpass('enter a password to use for {device}:\n'.format(device=device))
        return password
