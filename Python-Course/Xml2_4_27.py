import lxml.etree as ET
from lxml.builder import E as B

def buildPerson(firstname, lastname, title, address, street, zip, city, country, day, month, year):
    root = B.person(
                    B.firstname(firstname),
                    B.lastname(lastname),
                    B.title(title),
                    B.address(
                              B.street(street),
                              B.zip(zip),
                              B.city(city),
                              B.country(country)
                              ),
                    B.birthday(
                               B.day(day),
                               B.month(month),
                               B.year(year)
                               )
                    )
    return root

def buildPersonList(numberOfPersons):
    personList = B.personlist()
    for _ in xrange(numberOfPersons):
        arglist = []
        for j in xrange(11):
            arglist.append(str(j))
        personList.append(buildPerson(*arglist))
    return personList

if __name__ == '__main__':
    root = buildPersonList(2)
    print(ET.tostring(root, pretty_print=True))