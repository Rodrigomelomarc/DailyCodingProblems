import unittest


def solve(arr):
    new_arr = [reduce(lambda x, y: x * y, arr[:i] + arr[i+1:])
               for i in range(len(arr))]
    return new_arr


class Test(unittest.TestCase):
    def test(self):
        attempt = solve([1, 2, 3, 4, 5])
        expected = [120, 60, 40, 30, 24]
        self.assertEquals(attempt, expected)


if __name__ == '__main__':
    unittest.main()
