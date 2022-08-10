
# Constructor to accept
# real and imaginary part
class Complex:
    def __init__(self, tempReal, tempImaginary):
        self.real = tempReal
        self.imaginary = tempImaginary


# Defining addComp() method
# for adding two complex number
    def addComp(self, C1, C2):
     # creating temporary variable
        temp = Complex(0, 0)

    # adding real part of complex numbers
        temp.real = C1.real + C2.real

    # adding Imaginary part of complex numbers
        temp.imaginary = C1.imaginary + C2.imaginary

    # returning the sum
        print("Complex number 1 :", C1.real, "+ i" + str(C1.imaginary))

        print("Complex number 2 :", C2.real, "+ i" + str(C2.imaginary))

        print("Sum of complex number :", temp.real, "+ i" + str(temp.imaginary))
        return temp
    def subComp(self, C1, C2):

        temp = Complex(0, 0)


        temp.real = C1.real - C2.real


        temp.imaginary = C1.imaginary - C2.imaginary

        print("Complex number 1 :", C1.real, "+ i" + str(C1.imaginary))

        print("Complex number 2 :", C2.real, "+ i" + str(C2.imaginary))
        print("subtract of complex number :", temp.real, "+ i" + str(temp.imaginary))

        return temp

    def mulComp(self, C1, C2):
        temp = Complex(0, 0)

        temp.real = C1.real * C2.real

        temp.imaginary = C1.imaginary * C2.imaginary

        print("Complex number 1 :", C1.real, "+ i" + str(C1.imaginary))

        print("Complex number 2 :", C2.real, "+ i" + str(C2.imaginary))
        print("multiplication  of complex number :", temp.real, "+ i" + str(temp.imaginary))

        return temp


# Driver code
if __name__ == '__main__':

    C1 = Complex(3, 7)


    C2 = Complex(9, 5)

    C3 = Complex(0, 0)

    # calling addComp() method
    C3 = C3.addComp(C1, C2)
    C3=C3.subComp(C1,C2)
    C3=C3.mulComp(C1,C2)



