if __name__ == "__main__":
    # Write your solution here
    class StepperDevice:

        STEPPER_MODEL_LIST = ['FL42STH25-0404 A', 'FL42STH25-0404 B', 'FL42STH47-1684M A']
        __instance = None
        obj_counter = 0
        OBJ_MAX_NUM = 5

        def __new__(cls, *args, **kwargs):

            cls.obj_counter += 1
            if cls.obj_counter <= cls.OBJ_MAX_NUM:
                cls.__instance = super().__new__(cls)
            else:
                raise ValueError('too many class objects')
            return cls.__instance

        def __init__(self, name: str, stepper_model: str, axe_len: int, max_speed: int, __move_xy: int = 0):

            self.__move_xy = 0
            self.check_name(name)
            self.check_max_speed(max_speed)
            self.check_stepper_model(stepper_model)
            self.check_axe_len(axe_len)

            self.name = name
            self.stepper_model = stepper_model
            self.axe_len = axe_len
            self.max_speed = max_speed

        @classmethod
        def check_name(cls, value):

            if not isinstance(value, str):
                raise TypeError('attribute name must have type str')

        @classmethod
        def check_stepper_model(cls, value):

            if not isinstance(value, str):
                raise TypeError('attribute stepper_model must have type str')
            if not value in cls.STEPPER_MODEL_LIST:
                raise ValueError('stepper model is not registered in STEPPER_MODEL_LIST')

        @classmethod
        def check_axe_len(cls, value):

            if not isinstance(value, int):
                raise TypeError('attribute axe_len must have type int')

        @classmethod
        def check_max_speed(cls, value):

            if not isinstance(value, int):
                raise TypeError('attribute max_speed must have type int')
            if not 0 <= value < 30000:
                raise ValueError('attribute max_speed is out of range due to acceleration table')

        def __str__(self):

            return f'Устройство {self.name}, модель двигателя - {self.stepper_model}'

        def __repr__(self):

            return f'{self.__class__.__name__}(name={self.name!r}, stepper_model={self.stepper_model!r},' \
                   f' axe_len={self.axe_len!r}, max_speed={self.max_speed!r})'

        def check_move_xy(self, value):
            if type(value) != int:
                raise TypeError('attribute move_xy bust be int')
            if not (1 <= value <= self.axe_len):
                raise ValueError('attribute move_xy is out of range')

        @property
        def move_xy(self):

            return self.__move_xy

        @move_xy.setter
        def move_xy(self, value):

            self.check_move_xy(value)
            self.__move_xy = value


    class AxesStepper(StepperDevice):
        def __init__(self, name: str, stepper_model: str, axe_len: int = 500, max_speed: int = 5000,
                     detector_num: int = 2):

            super().__init__(name, stepper_model, axe_len, max_speed)
            self.detector_num = detector_num

        def __repr__(self):
            return f'{self.__class__.__name__}(name={self.name!r}, stepper_model={self.stepper_model!r},' \
                   f' axe_len={self.axe_len!r}, max_speed={self.max_speed!r}, detector_num={self.detector_num!r})'

        @classmethod
        def check_axe_len(cls, value):

            super().check_axe_len(value)
            if value > 500:
                raise ValueError('attribute axe_len must be less or equal 500 steps')


    class PumpStepper(StepperDevice):
        def __init__(self, name: str, stepper_model: str, axe_len: int = 500, max_speed: int = 5000,
                     detector_num: int = 2, volume_step: int = 1):

            super().__init__(name, stepper_model, axe_len, max_speed)
            self.detector_num = detector_num
            self.volume_step = volume_step

        def __repr__(self):
           
            return f'{self.__class__.__name__}(name={self.name!r}, stepper_model={self.stepper_model!r},' \
                   f' axe_len={self.axe_len!r}, max_speed={self.max_speed!r}, detector_num={self.detector_num!r},' \
                   f'volume_step={self.volume_step!r})'

a1 = StepperDevice(name='X', stepper_model='FL42STH25-0404 A', axe_len=60000, max_speed=5000)
print(a1.__dict__)
a2 = AxesStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
print(a2.__dict__)
a3 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
print(a3.__dict__)

a1._StepperDevice__move_xy = 100
print(a1.__dict__)

print(a2)

print(a3.__repr__())

n1 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
n2 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
n3 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
n4 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)
n5 = PumpStepper(name='X', stepper_model='FL42STH25-0404 A', axe_len=140, max_speed=5000)  # class object №6, but we need <= 5
