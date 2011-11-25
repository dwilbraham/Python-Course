import lxml.etree as ET

if __name__ == '__main__':
    tree = ET.parse('xml/cityindex.xml')
    tree.write('xml/cityindex.new.xml')
    tree.write('xml/cityindex.newc14n.xml', method='c14n')
    
    