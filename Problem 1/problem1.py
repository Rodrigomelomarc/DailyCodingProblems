import unittest


def solve(k, arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return True
    return False


class Tests(unittest.TestCase):
    def test_should_return_true(self):
        attempt = solve(17, [10, 15, 7, 5])
        self.assertTrue(attempt)

    def test_should_return_false(self):
        attempt = solve(30, [10, 15, 7, 5])
        self.assertFalse(attempt)


if __name__ == '__main__':
    unittest.main()
