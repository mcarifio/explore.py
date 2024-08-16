#! /usr/bin/env -S python -m pytest
import bt



def test_always():
    return None

def test_None():
    bt0 = bt.BT()
    assert bt.BT() == bt0.invert()

def test_example():
    bt0:bt.BT = bt.BT(contents=1, left=bt.BT(contents=2), right=bt.BT(contents=3, left=bt.BT(contents=4)))
    assert bt0.invert() == bt.BT(contents=1, left=bt.BT(contents=3, left=None, right=bt.BT(contents=4, left=None, right=None)), right=bt.BT(contents=2, left=None, right=None))
