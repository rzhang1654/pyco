#!/usr/bin/env python
#
import re

#the pattern can not use  break line
print bool(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)','(800) 555-1212 800-555-1212 18005551212'))

#the pattern can not use  break line even you use ''' it will not match
print bool(re.match(r'''\((?P<areacode>\d{3})\) 
(?P<prefix>\d{3})-(?P<number>\d{4}) 
(?P=areacode)-(?P=prefix)-(?P=number) 
1(?P=areacode)(?P=prefix)(?P=number)''','(800) 555-1212 800-555-1212 18005551212'))

# named group using ?P=
print re.match(r'''(?x)
# match (800) 555-1212, save areacode, prefix, no.
\((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})
# space
[ ]
# match 800-555-1212
(?P=areacode)-(?P=prefix)-(?P=number)
# space
[ ]
# match 18005551212
1(?P=areacode)(?P=prefix)(?P=number)
''','(800) 555-1212 800-555-1212 18005551212').groups()

#match using \n
print re.match(r'''(?x)
# match (800) 555-1212, save areacode, prefix, no.
\((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})
# space
[ ]
# match 800-555-1212
(?P=areacode)-(?P=prefix)-(?P=number)
# space
[ ]
# match 18005551212
1(?P=areacode)(?P=prefix)(?P=number)
''','(800) 555-1212 800-555-1212 18005551212').group()

#match using \g<xxx> somehow dow not work
print re.match(r'''(?x)
# match (800) 555-1212, save areacode, prefix, no.
\((\d{3})\)[ ](\d{3})-(\d{4})
# space
[ ]
# match 800-555-1212
\1-\2-\3
# space
[ ]
# match 18005551212
1\1\2\3
''','(800) 555-1212 800-555-1212 18005551212').group()

print re.match(r'''(?x)
# match (800) 555-1212, save areacode, prefix, no.
\((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})
# space
[ ]
# match 800-555-1212
\g<areacode>-\g<prefix>-\g<number>
# space
[ ]
# match 18005551212
1\g<areacode>\g<prefix>\g<number>
''','(800) 555-1212 800-555-1212 18005551212').group()

