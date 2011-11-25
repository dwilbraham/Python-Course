import lxml.etree as ET
from lxml.builder import E as B

def buildPerson(personid ,firstname, lastname, title, address, street, zipcode, city, country, day, month, year):
    root = B.person(
                    B.firstname(firstname),
                    B.lastname(lastname),
                    B.title(title),
                    B.address(
                              B.street(street),
                              B.zip(zipcode),
                              B.city(city),
                              B.country(country)
                              ),
                    B.birthday(
                               B.day(day),
                               B.month(month),
                               B.year(year)
                               ),
                    id=personid
                    )
    return root

def buildPersonList(numberOfPersons):
    personList = B.personlist()
    for i in xrange(numberOfPersons):
        arglist = []
        arglist.append(str(i))
        for j in xrange(11):
            arglist.append(str(j))
        personList.append(buildPerson(*arglist))
    return personList

if __name__ == '__main__':
    root = buildPersonList(2)
    print(ET.tostring(root, pretty_print=True))