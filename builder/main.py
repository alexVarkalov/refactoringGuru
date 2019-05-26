from builder.director import Director
from builder.iphone_builder import IPhoneBuilder
from builder.sony_phone_builder import SonyPhoneBuilder

if __name__ == '__main__':
    builder = SonyPhoneBuilder()
    # builder = IPhoneBuilder()
    director = Director(builder)
    # director.build_cheep_phone()
    director.build_expensive_phone()
    phone = builder.phone
    print(phone.cpu.model)
