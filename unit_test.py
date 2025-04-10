import unittest

def bear_drop(t):
    g = 9.8 
    h0 = 20
    h1 = h0 - 0.5 * g * t**2

    if h1<0:
        h1=0
    return h1

class Test_bear_drop(unittest.TestCase):
    def test_initial_height(self):
        self.assertEqual(bear_drop(0), 20)

    def test_negative_height(self):
        long_time = 100
        self.assertEqual(bear_drop(long_time), 0)

    def test_positive_height(self):
        short_time = 1
        self.assertEqual(bear_drop(short_time), 15.1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, bear_drop, "string")
if __name__ == '__main__':
    unittest.main()






'''h2=h0 - 0.5 * g * t2**2

t = np.linspace(0, 3, 100)
h = h0 - 0.5 * g * t**2


plt.figure(figsize=(5, 8))
plt.plot([0]*len(h), h, 'b-', label="motion curve")
plt.scatter(0, h0, color='g', label="initial location", zorder=3)
plt.scatter(0, h1, color='r', label="t=1s location", zorder=3)
plt.scatter(0, h2, color='b', label="t=2s location", zorder=3)

plt.xlabel("horizontal coordinate (m)")
plt.ylabel("height (m)")
plt.title("free drop movement of bear")
plt.ylim(0, h0 + 2)
plt.legend()
plt.grid(True)


plt.show()

print("the heigt of the bear at t=1s is: ", h1)'''