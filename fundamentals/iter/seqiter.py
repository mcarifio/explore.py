# https://realpython.com/python-iterators-iterables/
import pytest
import box

class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

class PassThrough:
    def __init__(self, o):
        self.o = o

    def __iter__(self):
        return self.o.__iter__()

    def __next__(self):
        yield from self.o


@pytest.fixture(scope="module")
def cases() -> box.Box:
    """
    Create a box of test cases for the Tests class.
    :return: a box (dict) of keys:values, each key is a test case name and each value is the value.
    """
    result = box.Box(key="value")
    return result


class Tests:

    def test_succeeds(self, cases):
        assert True

    def test_key(self, cases):
        assert cases.key == "value"

    def test_iter(self, cases):
        seq = [1, 2, 3]
        seq_iter = SequenceIterator(seq)
        assert [item for item in seq_iter] == seq

    def test_passthrough(self, cases):
        _set = {1, 2, 3}
        ptset = PassThrough(_set)
        _set_iter = PassThrough(_set)
        assert {s for s in ptset} == _set