# octopusLAB simple examp
from time import sleep
from components.analog import Analog
an2 = Analog(33)


while True:
    data =  an2.get_adc_aver(8)
    print(data)
    sleep(5)
