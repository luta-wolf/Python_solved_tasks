from module import code

def test_add():
	assert code.add(1, 2) == 3

def test_add__failing():
    assert code.add(10, 11) == 33

def test_add_int():
    assert type(code.add(10, 11)) == type(1)

def test_add__failing_float():
    assert type(code.add(10, 11)) == type(1.1)

# print(code.add(1, 2))
