 #!/usr/bin/env python
 
import sys
 
word2count = {}
 
for line in sys.stdin:
 
   line = line.strip()
 
   word , count = line.split('\t',1)
 
   try:
       count = int(count)
   except ValueError:
       continue
 
   try:
       word2count[word] += count
   except:
       word2count[word] = count
 
for word in sorted(word2count.keys()):
   print('%s --> %s' % (word , word2count[word]))
