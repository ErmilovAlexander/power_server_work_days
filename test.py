from client import DRACClient
login = "root"
password="MSURaCkpa$$"
ip="172.30.254.14"
client = DRACClient(ip, login, password)
print (client.get_power_state())
# client.set_power_state(target_state='POWER_ON')