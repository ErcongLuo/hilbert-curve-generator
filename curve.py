import matplotlib.pyplot as plt

class HilbertCurveGenerator:
    def __init__(self):
        self.vertices = []

    def construct_curve(self, n):
        self.vertices = []
        self._construct_hilbert_curve(n, [0, 0], [0, 1], [1, 1], [1, 0])

    def _construct_hilbert_curve(self, n, p1, p2, p3, p4):
        if n <= 0:
            self.vertices.extend([p1, p2, p3, p4])
        else:
            # Calculate the midpoints of the line segments
            a = [(p1[0] + p4[0]) / 2, (p1[1] + p4[1]) / 2]
            b = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            c = [(p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2]
            d = [(p3[0] + p4[0]) / 2, (p3[1] + p4[1]) / 2]

            # Recursively construct the smaller Hilbert curves
            self._construct_hilbert_curve(n - 1, p1, b, a, d)
            self._construct_hilbert_curve(n - 1, b, p2, d, c)
            self._construct_hilbert_curve(n - 1, a, d, p3, c)
            self._construct_hilbert_curve(n - 1, d, c, b, p4)

    def plot_curve(self):
        x = [vertex[0] for vertex in self.vertices]
        y = [vertex[1] for vertex in self.vertices]
        plt.plot(x, y, '-o')
        plt.axis('equal')
        plt.title('Hilbert Curve')
        plt.show()


# Usage example
hilbert_curve = HilbertCurveGenerator()
hilbert_curve.construct_curve(3)  # Construct the Hilbert curve up to 3 iterations
hilbert_curve.plot_curve()  # Plot the Hilbert curve
