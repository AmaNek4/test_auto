class Auto:
    def __init__(self, make, model, year, mileage, price, origin_ru):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
        self.orign_ru = origin_ru

    def makeModel(self):
        print(f'{self.make} {self.model} {self.mileage} ')

    def getAttrValue(self, attr):
        return getattr(self, attr)
    
    def __repr__(self):
        return f'{self.make} {self.model} - Цена {self.price}, Год производства: {self.year}, Пробег: {self.mileage}, Производство: {self.orign_ru}'

KiaSor = Auto('Kia', 'Sorrento', 2003, 223000, 415000, 'Россия')
HyunSol = Auto('Hyundai', 'Solaris', 2015, 41000, 869000, 'Корея')
VolkPas = Auto('Volkswagen', 'Passat', 2012, 127000, 900000, 'Германия')
LadaPri = Auto('Lada', 'Priora', 2011, 139000, 150000, 'Россия')
UazPat = Auto('UAZ', 'Patriot', 2011, 150000, 345400, 'Россия')

listOfCarNames=[]
listOfCarNames.append((KiaSor.make, KiaSor.model))
listOfCarNames.append((HyunSol.make, HyunSol.model))
listOfCarNames.append((VolkPas.make, VolkPas.model))
listOfCarNames.append((LadaPri.make, LadaPri.model))
listOfCarNames.append((UazPat.make, UazPat.model))

sortedByMileage=[]
def sorted_by_mileage(list_autos: list):
    return sorted(list_autos, key=lambda x: x.getAttrValue("mileage"))
temp = [KiaSor, HyunSol, VolkPas, LadaPri, UazPat]
sortedByMileage = sorted_by_mileage(temp)


