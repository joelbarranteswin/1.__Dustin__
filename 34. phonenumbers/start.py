import phonenumbers

NUMBER = '+51926337006'

ch_number = phonenumbers.parse(NUMBER, 'CH')
print(phonenumbers.is_valid_number(ch_number))
print(phonenumbers.format_number(ch_number, phonenumbers.PhoneNumberFormat.E164))
print(phonenumbers.format_number(ch_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print(phonenumbers.format_number(ch_number, phonenumbers.PhoneNumberFormat.NATIONAL))
print(phonenumbers.format_number(ch_number, phonenumbers.PhoneNumberFormat.RFC3966))
print(phonenumbers.geocoder.description_for_number(ch_number, 'en'))

service_number = phonenumbers.parse(NUMBER, 'US')
print(phonenumbers.carrier.name_for_number(service_number, 'en'))
print(phonenumbers.carrier.name_for_number(service_number, 'de'))
print(phonenumbers.carrier.name_for_number(service_number, 'fr'))
print(phonenumbers.carrier.name_for_number(service_number, 'it'))
print(phonenumbers.carrier.name_for_number(service_number, 'es'))
print(phonenumbers.carrier.name_for_number(service_number, 'pt'))
print(phonenumbers.carrier.name_for_number(service_number, 'ru'))
