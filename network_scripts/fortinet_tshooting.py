import netmiko

class FortinetTshooting():

    def __init__(self):
        self.command_list = { 'show_version':
                                    'get system status | grep Version',
                              'show_ha_status':
                                    'get system ha status'
                              }

    def connect_and_do_work(self, **kwargs):
        '''
        This is what connects to the fortigate and does all the work
        :param kwargs: values used to connect to the fortigate
        :return: output_list - this is the list of text output from commands ran against the fortigate
        '''
        # now connect to the firewall
        connection = netmiko.ConnectHandler(**kwargs)
        # send an 'a' to accept the prompt, basically we enter an a with a newline then change device type
        connection.write_channel('a\n')
        # redispatch will change the device type
        netmiko.redispatch(connection, device_type='fortinet')
        # now we run through each command and add to a list of output to display
        output_list = {}
        for key, value in self.command_list.items():
            output_list[key] = connection.send_command(value)
        # when all is said and done return the dictionary of command output
        return output_list
