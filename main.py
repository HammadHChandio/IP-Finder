from pubip import PubIp
from localIp import LocalIp


# Finding UserInput condition {0} for Public IP address and {1} for Local IP address
def ipfinder():
    while True:
        user_input = input('Please select 0 for Public IP and 1 for Local IP: ')
        if user_input == '0':
            # Create an object of the PublicIP class
            public_ip = PubIp()
            # Get the public IP address
            public_ip.get_ip()
            print(f'Your public IP is:  {public_ip.ip}')
            break
        if user_input == '1':
            # Create an object of the PublicIP class
            local_ip = LocalIp()
            # Get the public IP address
            local_ip.get_local_ip()
            print(f'Your local IP is:  {local_ip.ip}')
            break
        else:
            if user_input != "0" or "1":
                print(f"Wrong selection please try again!")


if __name__ == '__main__':
    ipfinder()
