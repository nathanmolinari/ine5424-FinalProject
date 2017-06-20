from TSTP_Admission_Control import TSTP_Admission_Control

admission_control = TSTP_Admission_Control()

serial = admission_control.serial

serial.new_sensor_request(0,0)
serial.new_sensor_request(5,0)
serial.new_sensor_request(10,0)
serial.new_sensor_request(15,0)
serial.new_sensor_request(0,0)

x = 10
y = 0
radius = 5
period = 200
expiracy = 2000000

serial.new_interest_request(x, y, radius, period, expiracy)
