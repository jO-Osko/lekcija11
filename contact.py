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

def dodaj_kontakt():
    ime = raw_input("ime")
    priimek = raw_input("priimek")
    phone = raw_input("phone")
    email = raw_input("email")
    year = raw_input("year")

    kontakt = Contact(ime, priimek, phone, birth_year=year, email=email)

    moji_kontakti.append(kontakt)

# Pomozna funkcija, s pomocjo katere uporabnik izbere kontakt, ki ga bo urejal/brisal
def izberi_kontakt():
    # Tabulator uporabimo zato, da se lepse poravnajo
    izpisi_kontakte()
    num = int(raw_input("vpisi zaporedno stevilko kontakta"))
    # Preverimo, ali je vpisal smiselno stevilko
    if not ( 0 <= num < len(moji_kontakti)):
        print("Takega kontakta ni")
        return -1
    return num

def izbrisi_kontakt():
    num = izberi_kontakt()
    if num == -1:
        # Ni tega kontakta (To se sicer lepse resi z izjemami, a do sedaj jih se nismo vzeli)
        return
    # izbrisemo izbrani kontakt (s tem se kontakto za njim zmanjsajo zaporedne stevilke)
    print("Brisem ....")
    # Bliznjica, ce uporabimo ze napisano funkcijo, ki naredi tocno to, kar zelimo, izbrise element in nam ga vrne, da ga lahko se uporabimo
    bliznjica = False
    if bliznjica:
        # python zna narediti vec stvari hkrati
        izbrisani = moji_kontakti.pop(num)
    else:
        # Lahko pa to naredimo sami
        # Vzamemo izbrisanega
        izbrisani = moji_kontakti[num]
        # Izbrisemo iz seznama (Opozorilo, ta operacija je lahko pri velikih seznamih pocasna, saj mora vse za njim premakniti za eno mesto nazaj - s tem se ni potrebno ubadati, samo za zanimivost)
        del moji_kontakti[num]


    print("Izbrisal: " + izbrisani.izpisi_kontakt())

def uredi_kontakt():
    num = izberi_kontakt()
    if num == -1:
        # Ni tega kontakta (To se sicer lepse resi z izjemami, a do sedaj jih se nismo vzeli)
        return
    # Podobno kot pri dodajanju, naredimo nov kontakt, le da ga tokrat vrnimemo na mesto (namesto) starega
    print("Urejanje: " + moji_kontakti[num].izpisi_kontakt())
    ime = raw_input("ime")
    priimek = raw_input("priimek")
    phone = raw_input("phone")
    email = raw_input("email")
    year = raw_input("year")

    # Naredimo nov kontakt
    kontakt = Contact(ime, priimek, phone, birth_year=year, email=email)

    # Prepisemo star kontakt
    moji_kontakti[num] = kontakt

    # Lahko bi urejal kontakt tudi po kosih
    # moji_kontkti[num].ime = raw_input("Novo ime")
    # In tako naprej
    # Ampak v kodo bi se ti na ta nacin hitro prikradla napaka, poskusi najti kje in zakaj

def izpisi_kontakte():
    print("St \t| Kontakt")
    print("-"*50)
    for j in range(len(moji_kontakti)):
        print(str(j) + "\t| " + moji_kontakti[j].izpisi_kontakt())

while True:
    odgovor = raw_input("Povej kaj zelis narediti (dodaj, izbrisi, uredi, izpisi, koncaj)?").lower()
    # Ideja je, da ima sedaj uporabnik ze na zacetku vec moznosti za izbor, kaj bi rad pocel
    # (prej je imel na voljo zgolj eno - dodaj), zato ga najprej prasamo po zelji
    if odgovor == "dodaj":
        dodaj_kontakt()
    elif odgovor == "uredi":
        uredi_kontakt()
    elif odgovor == "izbrisi":
        izbrisi_kontakt()
    elif odgovor == "izpisi":
        izpisi_kontakte()
    elif odgovor == "koncaj":
        break
    else:
        print("Nisem razumel odgvora :(")


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
