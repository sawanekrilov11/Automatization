from smartphone import Smartphone
catalog = []
phone_1 = Smartphone("Apple", "Iphone 14 PRO max", "+79211234556")
phone_2 = Smartphone("Samsung", "Galaxy S24 Ultra", "+79217894556")
phone_3 = Smartphone("Xiaomi", "13 Lite", "+79851234556")
phone_4 = Smartphone("LG", "G flex", "+75216548512")
phone_5 = Smartphone("Honor", "50 Lite", "+79642314899")
catalog.append(phone_1)
catalog.append(phone_2)
catalog.append(phone_3)
catalog.append(phone_4)
catalog.append(phone_5)
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")