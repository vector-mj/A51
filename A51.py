from functools import reduce
from textwrap import wrap

class A51():
    def __init__(self):
        self.LFSR1 = [0,1,0,0,1,1,1,0,0,0,1,0,1,1,1,1,0,1,0]         # len 19
        self.LFSR2 = [0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1]   # len 22
        self.LFSR3 = [0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,0,1,1,1,0,1,0] # len 23

    def majority(self)->int:
        """
        Calculate the majority of clock bits
        """
        return 1 if self.LFSR1[8] + self.LFSR2[10] + self.LFSR3[10] >= 2 else 0

    def clock(self,clk):

        x_o_r = []
        keystream = []

        for i in range(clk):

            maj = self.majority()

            if self.LFSR1[8] == maj:
                clkr = self.LFSR1[18] ^ self.LFSR1[17] ^ self.LFSR1[16] ^ self.LFSR1[13]
                x_o_r.append(self.LFSR1.pop())
                self.LFSR1.insert(0,clkr)

            if self.LFSR2[10] == maj:
                clkr = self.LFSR2[21] ^ self.LFSR2[20]
                x_o_r.append(self.LFSR2.pop())
                self.LFSR2.insert(0,clkr)

            if self.LFSR3[10] == maj:
                clkr = self.LFSR3[22] ^ self.LFSR3[21] ^ self.LFSR3[20] ^ self.LFSR3[7]
                x_o_r.append(self.LFSR3.pop())
                self.LFSR3.insert(0,clkr)
            
            keystream.append(str(reduce(lambda x,y: x ^ y , x_o_r)))

            print("-"*70)
            print(f"LFRS1: {''.join(str(i) for i in self.LFSR1)}")
            print(f"LFRS2: {''.join(str(i) for i in self.LFSR2)}")
            print(f"LFRS3: {''.join(str(i) for i in self.LFSR3)}")
            print(f"{' ^ '.join(str(i) for i in x_o_r)} = {str(reduce(lambda x,y: x ^ y , x_o_r))}")
            print(f"keysteam: {''.join(keystream)}")
            
            x_o_r.clear()


test = A51()
# test.clock(20)

text_to_binary = ''.join(format(ord(i),'b') for i in "Hello world")
print(text_to_binary[:19])
print(text_to_binary[19:41])
print(text_to_binary[41:64])