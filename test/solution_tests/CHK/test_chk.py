from solutions.CHK.checkout_solution import checkout


def test_checkout():
    assert checkout('AAA') == 130
    assert checkout('AAAA') == 180
