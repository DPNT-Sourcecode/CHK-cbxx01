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


