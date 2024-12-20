import inflect
def fun(n):
    letter_count = 0
    for i in range(1, n+1):
        p = inflect.engine()
        english_word = p.number_to_words(i)
        letter_count += sum([x.isalpha() for x in english_word])
    return letter_count

fun(1000)

        
