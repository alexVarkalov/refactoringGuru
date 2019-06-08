from builders import (
    IPhoneBuilder,
    IPhoneManualBuilder,
)
from builders.director import Director

if __name__ == '__main__':
    phone_builder = IPhoneBuilder()
    director = Director(phone_builder)
    director.build_expensive_phone()
    phone = phone_builder.phone
    manual_builder = IPhoneManualBuilder()
    director = Director(manual_builder)
    director.build_expensive_phone()
    manual = manual_builder.manual
    print(phone.cpu.model)
    print(manual)
