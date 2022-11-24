class FlatIterator:

    def __init__(self, lst):
        self.lst = lst
        self.index1 = 0
        self.index2 = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index1 >= len(self.lst):
            raise StopIteration()
        el_list = self.lst[self.index1]
        steps_list = len(el_list) - 1
        for el in el_list:
            if isinstance(el, list):
                return el
            else:
                return el



list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

for item in FlatIterator(list_of_lists_2):
    print(item)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()