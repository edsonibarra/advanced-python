from collections import Counter


word = "superflous"

print(Counter(word))

counter = Counter("superflous")

print(counter["s"])
print(counter.elements())
print(counter.most_common(1))


