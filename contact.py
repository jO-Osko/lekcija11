
class Contact(object):

    def __init__(self, first_name, last_name, phone_number, email, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.birth_year = int(birth_year)
        self.age = 2016 - self.birth_year

    def izpisi_kontakt(self):
        return self.last_name + ", " + self.first_name + ": " + str(self.phone_number)

    def starost_v_mesecih(self):
        return self.age * 12

moji_kontakti = [Contact("Filip", "Koprivec", "123456", "asd@gmail.com", 1900)]

while True:
    odgovor = raw_input("Ali zelis koncati?")
    if odgovor == "da":
        break
    ime = raw_input("ime")
    priimek = raw_input("priimek")
    phone = raw_input("phone")
    email = raw_input("email")
    year = raw_input("year")

    kontakt = Contact(ime, priimek, phone, birth_year=year, email=email)

    moji_kontakti.append(kontakt)
    

for posamezni_kontakt in moji_kontakti:
    #print(posamezni_kontakt.last_name + ", " +
    #      posamezni_kontakt.first_name + ": " +
    #      str(posamezni_kontakt.phone_number))
    print(posamezni_kontakt.izpisi_kontakt())


# Izpisimo samo dolocene
for kontakt in moji_kontakti:
    if kontakt.starost_v_mesecih() < 99999:
        print(kontakt.izpisi_kontakt())


# V datoteko lahko pisemo samo nize, tako da je potrebno vse stvari najprej spraviti v niz
# Predvsem pa si moramo izbrati nacin, kako v datoteko smiselno zapisati,
# da bomo kdaj kasneje znali iz nje prebrati
# Preprost nacin, ki deluje je kar da spoamezne stvari locimo z ";"


# Odpremo na poseben nacin, da nam ni potrebno zapirati
with open("kontakti.txt", "w") as output_file:
    for kontakt in moji_kontakti:
        # Zapisemo posamezen kontakt v datoteko
        output_file.write(str(kontakt.first_name) + ";")
        output_file.write(str(kontakt.last_name) + ";")
        output_file.write(str(kontakt.phone_number) + ";")
        output_file.write(str(kontakt.birth_year) + ";")
        output_file.write(str(kontakt.email) + "\n") # Na koncu pa zapisimo novo vrstico


# Bolj napredno (v bistvu zanimivost)

# Nekoliko boljsi nacin pa je da uporabimo ze pythonovo knjiznico pickle
import pickle

                        # b pomeni, da bo v datoteko zapisoval binarno in prihranil se nekaj prostora, poglej in bos videl, da je shranjeno na cloveku nerazumljiv nacin
with open("pickle_out", "wb") as pickle_datoteka:
    pickle.dump(moji_kontakti, pickle_datoteka)

# To shrani ucinkovito in hitro, poleg tega pa lahko iz te datoteke tudi brez tezav preberemo
# stare kontakte


"""
with open("pickle_out", "rb") as pickle_datoteka:
    moji_kontakti_v_datoteki = pickle.load(pickle_datoteka)

"""

# Super zanimivost
# Ce bos v pickle datoteko zapisoval vec stvari in jo preverjal "na roko"
# lahko ugotovis, da tudi ce zapises isto stvar, rezultat ne bo nujno enaka datoteka, a ko jo bos prebral bo rezultat enak
# Razlog za to je dejstvo, da je pickle uporablja razlicne metode za shranjevanje, ki niso nujno vedno enake
