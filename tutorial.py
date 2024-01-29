import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

#Enter the valid number
number = "+91-9080835402"
check_number = phonenumbers.parse(str(number), "CH")

#print the country of the number
print(geocoder.description_for_number(check_number, "en"))

#print the service provider of the number
print(carrier.name_for_number(check_number, 'en'))