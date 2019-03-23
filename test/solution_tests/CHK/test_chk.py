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
    #  - {"method":"checkout","params":["ABCDEABCDE"],"id":"CHK_R2_038"}, expected: 280, got: 265


