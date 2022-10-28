from collections import defaultdict
word_dict = defaultdict(int)
path_name = r"/Users/fuuswik/Python Files/Rank Words/text.txt"
make_red = lambda s: f"\033[1;31;49m{s}\033[0;37;49m"
make_blue = lambda s: f"\033[1;34;49m{s}\033[0;37;49m"

with open(file = path_name, mode = 'r') as f:
    for word in f.read().replace('\n','').split(' '):
        word_dict[word.lower()] += 1
for word, count in sorted(word_dict.items(), key= lambda pair: pair[1], reverse=True):
    print(f'"{make_red(word)}" used {make_blue(count)} times')