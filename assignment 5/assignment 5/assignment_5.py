import sys

## reverse string
text = raw_input("type something useless and press enter!\n")

#https://docs.python.org/2/whatsnew/2.3.html
#extended-slices <url over hoe je een reversed string KAN maken en andere opties
# [begin:end:step]
sys.stdout.write(text[13::-1]+'\n')
## end reverse string

