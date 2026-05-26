class Complex:
	# Write the code......
    def __init__(self):
        self.real = 0
        self.imaginary = 0

    def initComplex(self):
        # Read the space-separated input and map to real and imaginary
        data = list(map(int, input().split()))
        self.real = data[0]
        self.imaginary = data[1]

    def sum(self, c1, c2):
        # Add real parts and imaginary parts separately
        self.real = c1.real + c2.real
        self.imaginary = c1.imaginary + c2.imaginary

    def display(self):
        # Format the output to handle positive and negative imaginary parts
        if self.imaginary >= 0:
            print(f"{self.real} + {self.imaginary}i")
        else:
            # For negative, we use the absolute value of imaginary since the '-' is manually added
            print(f"{self.real} - {abs(self.imaginary)}i")

# Create three instances
c1 = Complex()
c2 = Complex()
c3 = Complex()

# Initialize two complex numbers
c1.initComplex()
c2.initComplex()

# Compute and display sum
c3.sum(c1, c2)
c3.display()
