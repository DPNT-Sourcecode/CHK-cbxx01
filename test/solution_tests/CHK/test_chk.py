from solutions.CHK.checkout_solution import checkout


def test_checkout():
    assert checkout('AAA') == 130
    assert checkout('AAAA') == 180
    assert checkout('ABAB') == 145
    assert checkout('AB') == 80
    assert checkout(00) == -1
    assert checkout('xyz') == -1
    assert False


