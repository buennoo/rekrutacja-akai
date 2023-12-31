# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.

def most_repeated(sentences):
    words_repeated = []
    count = {}

    for sentence in sentences:
        words = sentence.replace('?', '').replace('!', '').replace('.', '').replace(',', '').lower().split()
        
        for word in words:
            if not word in count:
                count[word] = 1
            else:
                count[word] += 1

    sort = sorted(count.items(), key=lambda item: item[1])
    words_repeated = sort[-3:]

    num = 0
    for num, (word, count) in enumerate(reversed(words_repeated)):
        print(num+1, ". ", word, " - ", count)


most_repeated(sentences)

        


