import pytest
def inc(x):
	return x + 1

def test_answer():
	assert inc(3) == 5

def test_answer_2():
	assert inc(4) == 5

def test_answer_3():
	assert inc(3) == 4

def test_sum():
	assert sum([1, 2, 3]) == 6, "Expected: 6"

if __name__ =="__main__":
	pytest.main()

