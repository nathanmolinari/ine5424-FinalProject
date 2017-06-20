# from TSTP_Admission_Control import TSTP_Admission_Control as Admission_Control
from Interest import Interest
from enum import Enum
from Sensor import Sensor

class Request_Type(Enum):
    SENSOR = 0
    INTEREST = 1

class Serial_Manager:

    def __init__(self, Admission_Control):
        self.Admission_Control = Admission_Control;

    def read(self):
        data = self.readLine()
        request_type, param = self.extract_data(data)

        if(request_type == Request_Type.INTEREST):
            Admission_Control.handle_new_interest_request(param)
        else:
            Admission_Control.handle_new_sensor_request(param)

    def write(self, data):
        if data:
            print("Writing on serial succes")
        else:
            print("Writing on serial fail")

    def readLine(self):
        print("Dados lidos do serial foram LALALALA")

    def extract_data(self, data):
        x = 10
        y = 10
        radius = 5
        period = 200
        expiracy = 2000000

        param = Interest(x, y, radius, period, expiracy)
        request_type = Request_Type.INTEREST

        return request_type, param

    def new_sensor_request(self, x, y):
        print("Serial recevied new sensor request with coordinates", x, y)
        sensor = Sensor(x, y)
        self.Admission_Control.handle_new_sensor_request(sensor)

    def new_interest_request(self, x, y, radius, period, expiracy):
        print("Serial recevied new interest request with coordinates", x, y)
        interest = Interest(x, y, radius, period, expiracy)
        self.Admission_Control.handle_new_interest_request(interest)
