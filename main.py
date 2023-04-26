def listeler(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = listeler(list1, list2)
print(result)

def palindrome(strings):
    return [s for s in strings if s == s[::-1]]

strings = ['kaan', 'aydın', 'naber', 'iyi','görüşürüz']
result = palindrome(strings)
print(result)


def sieves(numbers):
    primes = []
    sieve = [True] * (max(numbers) + 1)
    for i in range(2, int(len(sieve)**0.5)+1):
        if sieve[i]:
            for j in range(i**2, len(sieve), i):
                sieve[j] = False
    for n in numbers:
        if n > 1 and sieve[n]:
            primes.append(n)
    return primes

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = sieves(numbers)
print(primes)


def anagrams(word, word_list):
    word_sorted = sorted(word.lower().replace(" ", ""))
    anagrams = []
    for w in word_list:
        w_sorted = sorted(w.lower().replace(" ", ""))
        if w_sorted == word_sorted:
            anagrams.append(w)
    return anagrams

word = "listen"
word_list = ["enlists", "google", "inlets", "banana"]
anagrams_list = anagrams(word, word_list)
print(anagrams_list)





