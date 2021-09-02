import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]



# def get_jokes(num):
#     num = int(num)
#     noun_rnd = random.choice(nouns)
#     ad_rnd = random.choice(adverbs)
#     adj_rnd = random.choice(adjectives)
#     joke = [noun_rnd,ad_rnd,adj_rnd]
#     result = [] * num
#     result.append(joke)
#     return result
#

def get_jokes(num, flag = True):
    num = int(num)
    noun_rnd = random.choice(nouns)
    ad_rnd = random.choice(adverbs)
    adj_rnd = random.choice(adjectives)
    joke = f'{noun_rnd},{ad_rnd},{adj_rnd}'
    result = []
    print(joke)
    if flag == True:
        result = joke.split()
        for noun in nouns:
            for fun in result:
                if noun == fun:
                    nouns.remove(noun)

        for adverb in adverbs:
            for fun in result:
                if adverb == fun:
                    adverbs.remove(adverb)

        for adjective in adjectives:
            for fun in result:
                if adjective == fun:
                    adjectives.remove(adjective)


get_jokes(num=2,flag=True)

