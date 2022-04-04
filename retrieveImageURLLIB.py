# retrieving web image with urllib and compute frequency of each word
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode().rstrip())