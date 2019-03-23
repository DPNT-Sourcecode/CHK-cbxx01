from solutions.CHK.checkout_solution import checkout

def test_SSXX():
    assert checkout('SSXX') == 61


def test_checkout_Z():
    assert checkout('Z') == 21


def test_checkout_B():
    assert checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 965


def test_checkout_B():
    assert checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ') == 1880


def test_checkout():
    assert checkout('AAA') == 130
    assert checkout('AAAA') == 180
    assert checkout('AAAAA') == 200
    assert checkout('ABAB') == 145
    assert checkout('AB') == 80
    assert checkout(0) == -1
    assert checkout('xyz') == -1
    assert checkout('C') == 20
    assert checkout('D') == 15
    assert checkout('BEE') == 80
    assert checkout('EE') == 80
    assert checkout('AAAAAAAA') == 330
    assert checkout('AAAAAAAAA') == 380


def test_checkout_ABCDEABCDE():
    assert checkout('ABCDEABCDE') == 280


def test_checkout_B():
    assert checkout('B') == 30


def test_checkout_F():
    assert checkout('F') == 10


def test_checkout_FFF():
    assert checkout('FFF') == 20


def test_checkout_FFFF():
    assert checkout('FFFF') == 30


def test_checkout_FFFFFF():
    assert checkout('FFFFFF') == 40


def test_checkout_UUUU():
    assert checkout('UUUU') == 120


def test_checkout_FFFFF():
    assert checkout('FFFFF') == 40


def test_checkout_UUUUUU():
    assert checkout('UUUUUU') == 200

