#!/usr/bin/python
impoer re
with open('y1.txt', 'r') as myfile:
  data = myfile.read()
#print data
record_re = re.compile(r'''Item ID:\s*
                           (?P<Item_ID>\d+)  
                           \n                #line break
                           Barcode:\s*
                           (?P<Barcode>\d+)  
                            \n               #line break
                           Title:\s*
                           (?P<Title>.*?)  
                            \n               #line break
                           Enum/Chron:\s*
                           (?P<Enum>.*?)  
                            \n               #line break
                           Call Number:\s
                           (?P<Enum>.*?)  
                            \n               #line break
Call Number Prefix:                
Holding Location:                  Circulating collection
Permanent Location:                Circulating collection
Temporary Location:                 / Cataloging Dept.
Permanent Type:                    book
Temporary Type:                    
Media Type:                        
Item Status:                       Not Charged, Withdrawn
Statistical Categories:            
Magnetic Media:                    No
Sensitize:                         Yes
Free Text:                         wdn:l & p : 10/12/07
Copy Number:                       1
Pieces Number:                     1
Price:                             0.00
MFHD ID 116223:                    Suppressed
Bib ID 113269:                     Suppressed
Update Bib Status:                 N/A
Update Holding Status:             N/A
Update Item Status:                Processed.
