#Problem79.py

import re

keylog = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716"""


numbers_test = keylog.split("\n")

found = False
password = 100

while not found:
	gauntlet = True
	for num in numbers_test:
		regex = r".*"+re.escape(num[0])+r".*"+re.escape(num[1])+r".*"+re.escape(num[2])+r".*"
		if not re.search(regex, str(password)):
			gauntlet = False
			break
	if gauntlet:
		print password
		found = True
	password += 1
