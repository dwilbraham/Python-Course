import lxml.etree as ET

if __name__ == '__main__':
    tree = ET.parse('xml/cityindex.xml')
    
    print([ el.text for el in tree.xpath('//city')])
    
    find_city = ET.XPath('/cityindex/entry/region')
    regionList = [el.text for el in find_city(tree)]
    regionList.sort()
    regionCount = {}
    for i in regionList:
        regionCount.setdefault(i, 0)
        regionCount[i] =+ 1
    print(regionCount)
    