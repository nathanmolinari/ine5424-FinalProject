class Burden_Estimator:

    def __init__(self, wsn):
        self.wsn = wsn;

    def is_sensor_aceptable(self, sensor):
        return True

    def is_interest_aceptable(self, interest):
        sensors_in_region = self.wsn.get_sensors_in_range(interest)
        print("Sensors in region of interest:")
        for s in sensors_in_region:
            print(s)

        nearest_sensor = self.wsn.get_nearest_sensor(sensors_in_region)
        print("The nearest sensor of gateway in region is: ", nearest_sensor)

        shortest_path = self.wsn.shortest_path(nearest_sensor)
        print("The shortest_path to nearest sensor is:")

        for s in shortest_path:
            print(s)

        print("The number of hops to nearest sensor is:", len(shortest_path))


        print("Lets estimate the fucking Burden!")
        return True
