import functools


class Parity:
    """Bitwise operation
    Find the parity
    from EPI Ch 1
    """

    def __init__(self, x):
        self._x = x

    def set_x(self, x):
        self._x = x

    def print_result(fun):
        @functools.wraps(fun)
        def wrap(self):
            result = fun(self)
            print(f"{'x':<8}:{self._x :>6}")
            print(f"{'result':<8}:{result :>5}")
            print(f"{'x':<8}:{bin(self._x) :>5}")
            print(f"{'result':<8}:{bin(result) :>5}")

        return wrap

    @print_result
    def parity_bruteforce(self):
        result = 0
        var = self._x
        while var:
            result ^= var & 1
            var >>= 1
        return result

    def parity_dropbits(self):
        result = 0
        var = self._x
        while var:
            result ^= 0
            var &= var - 1
        return result

    def drop_lowest(self):
        count = 0
        var = self._x
        while var:
            print(f"{'x' : <5} : {bin(var)}")
            print(f"{'x-1' :<5}: {bin(var - 1)}")
            var = var & (var - 1)
            count += 1
        print(f"drop lowest 1s for {count} times")

    def drop_lowest2(self):
        " Observe how x & (x-1) works"
        count = 0
        var = self._x
        while count < 5:
            print(bin(var))
            print(bin(~(var - 1)))
            var = var & ~(var - 1)
            print(f"result {bin(var)}")
            count += 1
        print(f"count: {count}")

    def variant1(self):
        """fill bits after the less significant bit 1 to be 1
        ex. 101000 -> 101111
        """
        var = self._x
        var |= var - 1
        return var

    def variant2(self):
        """x modulo apower of 2
        ex. input: 77, output: 13
        """
        val = self._x
        while val:
            pre_val = val
            val = val & (val - 1)
        return pre_val ^ self._x

    def variant3(self):
        """if x is power of 2

        Args:
            x (int): a positive integer
        """
        return self._x & (self._x - 1) is 0


def main():
    # x = 128
    # result = variant3(x)
    # print(f"x: {x} result: {result}")
    # x = 127
    # result = variant3(x)
    # print(f"x: {x} result: {result}")
    p = Parity(127)
    p.parity_bruteforce()


if __name__ == "__main__":
    main()