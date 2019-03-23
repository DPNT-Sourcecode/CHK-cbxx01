from solutions.CHK.checkout_solution import checkout


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

    # Result is: FAILED
    # Some requests have failed (6/40). Here are some of them:
    #  - {"method":"checkout","params":["AAAAAAAA"],"id":"CHK_R2_020"}, expected: 330, got: 350
    assert checkout('AAAAAAAA') == 330
    #  - {"method":"checkout","params":["AAAAAAAAA"],"id":"CHK_R2_021"}, expected: 380, got: 400
    assert checkout('AAAAAAAAA') == 380


def test_checkout_ABCDEABCDE():
    #  - {"method":"checkout","params":["ABCDEABCDE"],"id":"CHK_R2_038"}, expected: 280, got: 265
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


def test_checkout_UUUUUU():
    assert checkout('UUUUUU') == 200
