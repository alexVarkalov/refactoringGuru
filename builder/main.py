from director import Director
from iphone_builder import IPhoneBuilder
from sony_phone_builder import SonyPhoneBuilder

if __name__ == '__main__':
    builder = SonyPhoneBuilder()
    # builder = IPhoneBuilder()
    director = Director(builder)
    # director.build_cheep_phone()
    director.build_expensive_phone()
    phone = builder.phone
    print(phone.cpu.model)
