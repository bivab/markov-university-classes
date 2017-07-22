import codecs
import sys

import markovify


BATCH_SIZE = 5
DATASETS = ['cs', 'phil', 'wiwi']


def get_all_models(state_size):
    return markovify.combine([get_model(state_size, ds) for ds in DATASETS])

def get_model(state_size, dataset):
    units = 'data/{0}/units.txt'.format(dataset)
    abstract_units = 'data/{0}/abstract_units.txt'.format(dataset)
    #
    with codecs.open(units, 'r', 'utf-8') as f:
        text = f.read()
    model1 = markovify.NewlineText(text, state_size=state_size)
    #
    with codecs.open(abstract_units, 'r', 'utf-8') as f:
        text =f.read()
    model2 = markovify.NewlineText(text, state_size=state_size)
    #
    model = markovify.combine([model1, model2], [ 1.5, 1 ])

    return model

def main(state_size=1, dataset='phil'):

    if dataset == 'ALL':
        model = get_all_models(state_size)
    else:
        model = get_model(state_size, dataset)
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
    kwargs = {}
    if len(sys.argv) > 1:
        kwargs['state_size'] = int(sys.argv[1])
    if len(sys.argv) > 2:
        kwargs['dataset'] = sys.argv[2]

    main(**kwargs)
