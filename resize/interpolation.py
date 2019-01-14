class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for linear interpolation here
        c1 = pt1[0]
        i1 = pt1[1]
        c2 = pt2[0]
        i2 = pt2[1]
        t = c2 -c1
        if t == 0:
            print("Divide by zero error")
        return (i1 * (c2 - unknown) / (t)) + (i2 * (unknown - c1) / (t))


    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        I1 = self.linear_interpolation([pt1[0], pt1[2]],[pt3[0], pt3[2]], unknown[0])
        I2 = self.linear_interpolation([pt2[0], pt2[2]],[pt4[0], pt4[2]], unknown[0])
        return self.linear_interpolation([pt1[1], I1],[pt2[1], I2], unknown[1])


