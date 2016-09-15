from string import punctuation

with open("text.txt") as better_open_file:
    text = better_open_file.read()
    text = text.lower()
    exclude = """a, able, about, across, after, all, almost, also, am, among, an, and, any, are, as, at, be,
because, been, but, by, can, cannot, could, dear, did, do, does, either, else, ever, every,
for, from, get, got, had, has, have, he, her, hers, him, his, how, however, i, if, in, into, is,
it, its, just, least, let, like, likely, may, me, might, most, must, my, neither, no, nor,
not, of, off, often, on, only, or, other, our, own, rather, said, say, says, she, should,
since, so, some, than, that, the, their, them, then, there, these, they, this, tis, to, too,
twas, us, wants, was, we, were, what, when, where, which, while, who, whom, why, will, with,
would, yet, you, your"""
    exclude = exclude.replace("\n", "")
    exclude = exclude.replace(",", "")
    exclude = exclude.split(" ")
    for item in punctuation:
        text = text.replace(item, "")
    text = text.replace("\n", " ")
    for excluded_words in exclude:
        while excluded_words in text:
            text.replace(excluded_words, "")
    words_list = text.split(" ")

    word_count = {}
    for words in words_list:
        if words in word_count.keys():
            word_count[words] += 1
        else:
            word_count[words] = 1
    word_count = (sorted(word_count.items(), key=lambda x: x[1]))
    word_count = word_count[-21: -1]
    for item in reversed(word_count):
        print (*item)
