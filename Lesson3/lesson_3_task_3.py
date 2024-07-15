from mailing import Mailing
from address import Address
from_address = Address("123456", "London", "Oxford St.", "12A", "1")
to_address = Address("780000", "Petrozavodsk", "Gogolya", "98B", "12")
mailing = Mailing(to_address, from_address, 1235, "qggfdg1")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartament}"
      f" в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartament}. Стоимость {mailing.cost} рублей.")