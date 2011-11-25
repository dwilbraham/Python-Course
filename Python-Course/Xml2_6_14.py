import lxml.etree as ET

def findRegion(lookupList, city, country):
    return lookupList.setdefault((city, country), "UNKNOWN")

def buildRegionLooupDict():
    lookupDict = {}
    for _, entry in ET.iterparse('xml/cityindex.xml', tag='entry'):
        city = entry.find('./city').text
        country = entry.find('./country').text
        region = entry.find('./region').text
        lookupDict[(city, country)] = region
        entry.clear()
    return lookupDict

if __name__ == '__main__':
    lookupDict = buildRegionLooupDict()
    for _, person in ET.iterparse('xml/personlist.xml', tag='person'):
        city = person.find('./address/city').text
        country = person.find('./address/country').text
        region = findRegion(lookupDict, city, country)
        if region is not "UNKNOWN":
            print(region)
        person.clear()
        