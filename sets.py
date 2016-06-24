s = {1, 2, 3, 4}
assert 3 in s
assert len(s) == 4
t = s.union({1, 5})
assert len(t) == 5
assert s.intersection({4,5,6,7}) == {4}
assert t.intersection({4,5,6,7}) == {4, 5}
