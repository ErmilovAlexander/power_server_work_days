from client import DRACClient
import datetime
import time
import config_parse as CP
login = CP.DEFAULT['login']
password = CP.DEFAULT['password']
#works_days = {0: u"Пн", 1: u"Вт", 2: u"Ср", 3: u"Чт", 4: u"Пт"}
works_days = [i for i in range(0,5)]
# time_night = [i for i in range(18,25)]
# time_morning = [i for i in range(0,9)]
# works_time = time_night + time_morning
work_time = [i for i in range(9,19)]
#holiday_days = {5: u"Сб", 6: u"Вс"}
holiday_days = [i for i in range(5,7)]
POWER_STATE = {'POWER_ON':True, 'POWER_OFF':False,'REBOOT':None}
seconds = int(CP.DEFAULT['wait_time'])*60
state_now = {}
def get_drac(ip):
    return DRACClient(ip, login, password)

def getStatusServer(ip)
    client = get_drac(ip=ip) #object
    return [client.get_power_state(),client]

def power_on(client):
    client.set_power_state(target_state='POWER_ON')

def power_off(clinet):
    client.set_power_state(target_state='POWER_OFF')

def main():
    # servers = ['192.168.0.1','192.168.0.2','192.168.0.3','192.168.0.4','192.168.0.5','192.168.0.6']
    servers = CP.DEFAULT['servers'].split(',')
    while True:
        a = datetime.datetime.now()
        hour = a.hour
        # minute = a.minute
        num_day = datetime.date.today().weekday()
        if num_day in works_days and hour not in work_time:
            # day = works_days[num_day]
            for ip in servers:
                power_state = getStatusServer(ip=ip)
                if not POWER_STATE[power_state[0]]:
                    print("Server is down")
                    print("Wait server Up")
                    power_on(client=power_state[1])
                    #state_now.update() #TODO
        elif num_day in works_days and hour in work_time:
            for ip in servers:
                client = get_drac(ip=ip)
                power_state = client.get_power_state()
                if POWER_STATE[power_state[0]]:
                    print("Server is Up")
                    print("Wait server Down")
                    power_on(client=power_state[1])
        time.sleep(seconds)

if __name__ == '__main__':
    main()
