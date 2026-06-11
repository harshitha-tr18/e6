From app import add
def test_add_positive():
  assert add(2,3) == 5
def test_add_negitive():
  assert add(-1,-1) == -2
def test_add_zero():
  assert add(0,5) == 5
def test_add_mixed():
  assert add(-1,1) == 0
