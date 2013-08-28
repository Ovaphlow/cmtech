# -*- coding:utf-8 -*-

import mysql.connector
import xml.dom.minidom

xmlFile = 'HuanPingLeiBie.xml'
rootName = 'root'

cnx_cfg = {
  'user': 'root',
  'password': 'dsdfjk',
  'host': '127.0.0.1',
  'database': 'ems-hrb',
}

def get_tagname():
  from xml.dom.minidom import parse, parseString
  doc = parse(xmlFile)
  root = doc.documentElement
  str = root.getElementsByTagName(catName)
  for sub in str:
    name = sub.getElementsByTagName(subName)[0]
    tmp_name = name.childNodes[0].nodeValue
    tmp_name = tmp_name.encode('utf-8')
    print tmp_name

def gen_xml():
  t1_name = 'Tier1'
  t1_attribute = '环评类别'
  t2_name = 'Tier2'
  t2_value = ''
  sqlText = 'SELECT * FROM tbs001_basicdatasub WHERE MainID=7 ORDER BY ID'

  cnx = mysql.connector.connect(**config_database)
  cursor = cnx.cursor()
  cursor.execute(sqlText)
  data = cursor.fetchall()

  impl = xml.dom.minidom.getDOMImplementation()
  dom = impl.createDocument(None, rootName, None)
  root = dom.documentElement
  t1 = dom.createElement(t1_name)
  root.appendChild(t1)
  t1.setAttribute("name", t1_attribute)

  print cursor.rowcount
  for i in range(0, cursor.rowcount):
    t2 = dom.createElement(t2_name)
    value2 = dom.createTextNode(data[i][2].encode('utf-8'))
    t2.appendChild(value2)
    t1.appendChild(t2)

  xml_file = open(xmlFile, 'a')
  dom.writexml(xml_file, addindent='  ', newl='\n')
  xml_file.close()
  print 'done!', t2_value

def gen_xml_diqu():
  t1_name = 'Tier1'
  t2_name = 'Tier2'
  t3_name = 'Tier3'
  sql_text1 = 'SELECT * FROM tbs001_basicdatasub WHERE MainID=14ORDER BY ID'
  cnx1 = mysql.connector.connect(**config_database)
  cursor1 = cnx1.cursor()
  cursor1.execute('SELECT * FROM tbs001_basicdatasub WHERE MainID=14 ORDER BY ID')
  data1 = cursor1.fetchall()
  cnx2 = mysql.connector.connect(**config_database)
  cursor2 = cnx1.cursor()
  cnx3 = mysql.connector.connect(**config_database)
  cursor3 = cnx1.cursor()

  impl = xml.dom.minidom.getDOMImplementation()
  dom = impl.createDocument(None, rootName, None)
  root = dom.documentElement
  t1 = dom.createElement(t1_name)

  for var1 in range(0, cursor1.rowcount):
    tag1 = data1[var1][2][0:2]
    #print tag1
    t1 = dom.createElement(t1_name)
    root.appendChild(t1)
    t1.setAttribute("name", data1[var1][2])

    cursor2.execute('SELECT * FROM tbs001_basicdatasub WHERE MainID=24 AND DataValueMemo LIKE "' + tag1 + '%" ORDER BY ID')
    data2 = cursor2.fetchall()
    for var2 in range(0, cursor2.rowcount):
      tag2 = data2[var2][2][0:3]
      #print tag2
      t2 = dom.createElement(t2_name)
      t1.appendChild(t2)
      t2.setAttribute("name", data2[var2][2])

      cursor3.execute('SELECT * FROM tbs001_basicdatasub WHERE MainID=25 AND DataValueMemo LIKE "' + tag2 + '%"ORDER BY ID')
      data3 = cursor3.fetchall()
      for var3 in range(0, cursor3.rowcount):
        tag3 = data3[var3][2]
        #print tag3
        t3 = dom.createElement(t3_name)
        value3 = dom.createTextNode(data3[var3][2].encode('utf-8'))
        t3.appendChild(value3)
        t2.appendChild(t3)

  xml_file = open(xmlFile, 'a')
  dom.writexml(xml_file, addindent='  ', newl='\n')
  xml_file.close()
  print 'done!'

gen_xml()
