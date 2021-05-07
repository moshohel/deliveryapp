from core .models import Districts


class Parcel_price:
    def __init__(self, data, weight):
        self.data = data
        self.weight = weight

    def price(self):
        price = 0
        return_charge = 0

        districtObj = Districts.objects.get(pk=self.data)
        if districtObj.name == 'Dhaka' and districtObj.division.name == 'Dhaka':
            if self.weight < 2:
                price = 60
                return_charge = 0
                return price, return_charge

            else:
                price = (((self.weight-2)*10)+60)
                return_charge = 0
                return price, return_charge

        elif districtObj.division.name == 'Dhaka':
            if self.weight < 2:
                price = 110
                cod = price*0.01
                price += cod
                return_charge = price/2
                return price, return_charge

            else:
                price = ((self.weight-2)*20)+110
                cod = (((self.weight-2)*20)+110)*0.01
                price += cod
                return_charge = price/2
                return price, return_charge
        else:
            if self.weight < 2:
                price = 130
                cod = price*0.01
                price += cod
                return_charge = price/2
                return price, return_charge
            else:
                price = ((self.weight-2)*20)+130
                cod = (((self.weight-2)*20)+130)*0.01
                price += cod
                return_charge = price/2
                return price, return_charge
