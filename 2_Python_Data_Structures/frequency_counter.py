separator = "-"
number_separtors = 50

print(number_separtors*separator)

fh = open("romeo.txt", "r")
count = 0
for line in fh:
    print(line.strip())
    count += 1
fh.close()

print(count, "Lines")
print(number_separtors*separator)

wordsFreq = {}
fh = open("romeo.txt", "r")
for line in fh:
    words = line.strip().split()
    print(words)
    for word in words:
        wordsFreq[word] = wordsFreq.get(word, 0)+1
fh.close()

print(number_separtors*separator)
print(wordsFreq)
print(number_separtors*separator)

wordsFreq_sorted = list(wordsFreq.items())
wordsFreq_sorted.sort(reverse=True, key=lambda x: x[1])

print(wordsFreq_sorted)
print(number_separtors*separator)
print(
    f'The most frequent word is "{wordsFreq_sorted[0][0]}", which appears {wordsFreq_sorted[0][1]} times')
print(number_separtors*separator)
