import time
def sentence_maker(sen):
    interrogatives = ("what", "when", "where", "how", "why")
    capitalized = sen.capitalize()
    if sen.startswith(interrogatives):
        res = "{}?".format(capitalized)
    else:
        res = "{}.".format(capitalized)
    return res

result = []
n = 1

while True:
    insentence = str(input("Type your sentence here: "))
    breaker = "\end"

    if insentence == breaker:
        break
    else:
        result.append(sentence_maker(insentence))

for i in result:
    print(str(n) + ".", i, "\n")
    n += 1

time.sleep(3600)

