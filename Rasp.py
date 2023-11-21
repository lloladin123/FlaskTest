from sense_hat import SenseHat
import time

class SenseMeasure:
    def init(self):
        self.s = SenseHat()
        self.s.low_light = True
        self.green = (0, 255, 0)
        self.yellow = (255, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.nothing = (0, 0, 0)
        self.pink = (255, 105, 180)

    def Get_Measure(self, mode):
        if mode == "temp":
            temp = self.s.temp
            print("Temp: "+str(temp))
            temp_value = temp / 2.5 + 16
            print("Temp value: "+str(temp_value))
            return temp_value
        elif mode == "pressure":
            pressure = self.s.pressure
            pressure_value = pressure / 20
            return pressure_value
        elif mode == "humidity":
            humidity = self.s.humidity
            humidity_value = 64* humidity / 100
            return humidity_value

if __name__ == "__main__":
    s = SenseMeasure()
    while True:
        print(s.Get_Measure("temp"))
        time.sleep(1)
        print(s.Get_Measure("pressure"))
        time.sleep(1)
        print(s.Get_Measure("humidity"))
        time.sleep(1)