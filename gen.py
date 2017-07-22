import codecs
import sys

import markovify


STATE_SIZE = 1
BATCH_SIZE = 5
DATASET = "phil"


def main():
    units = 'data/{0}/units.txt'.format(DATASET)
    abstract_units = 'data/{0}/abstract_units.txt'.format(DATASET)
    with codecs.open(units, 'r', 'utf-8') as f:
        text = f.read()
    model1 = markovify.NewlineText(text, state_size=STATE_SIZE)
    with codecs.open(abstract_units, 'r', 'utf-8') as f:
        text =f.read()
    model2 = markovify.NewlineText(text, state_size=STATE_SIZE)

    model = markovify.combine([model1, model2], [ 1.5, 1 ])
    for i in range(BATCH_SIZE):
        print(model.make_sentence())

    print("\n----------------\n")

    for i in range(BATCH_SIZE):
        print(model.make_short_sentence(140))

    print("\n----------------\n")

    try:
        for i in range(BATCH_SIZE):
            print(model.make_sentence_with_start("Die"))
    except KeyError:
        pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        STATE_SIZE = int(sys.argv[1])
    if len(sys.argv) > 2:
        DATASET = sys.argv[2]

    main()
