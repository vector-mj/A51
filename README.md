# A5/1 Encryption Cipher Algorithm 🔐

![alt](https://upload.wikimedia.org/wikipedia/commons/5/5e/A5-1_GSM_cipher.svg)

## About 🧐

`A5/1 is a stream cipher used to provide over-the-air communication privacy in the GSM cellular telephone standard. It is one of several implementations of the A5 security protocol. It was initially kept secret, but became public knowledge through leaks and reverse engineering. A number of serious weaknesses in the cipher have been identified.`


## Description 🧾

`A5/1 is based around a combination of three linear-feedback shift registers (LFSRs) with irregular clocking. The three shift registers are specified as follows:`


<table>
  <tr>
    <td>LFSR no.</td>
    <td>Length in bits</td>
    <td>Feedback polynomial</td>
    <td>Clocking bit</td>
    <td>Tapped bits</td>
  </tr>
  <tr>
    <td>1</td>
    <td>19</td>
    <td>x<sup>19</sup> + x<sup>18</sup> + x<sup>17</sup> + x<sup>14</sup> + 1</td>
    <td>8</td>
    <td>13, 16, 17, 18</td>
  </tr>
  <tr>
    <td>2</td>
    <td>22</td>
    <td>x<sup>22</sup> + <sup>21</sup> + 1</td>
    <td>10</td>
    <td>20, 21</td>
  </tr>
  <tr>
    <td>3</td>
    <td>23</td>
    <td>x<sup>23</sup> + x<sup>22</sup> + x<sup>21</sup> + x<sup>8</sup> + 1</td>
    <td>10</td>
    <td>10	7, 20, 21, 22</td>
  </tr>
</table>


## Example 🧪

```yml
$ python A51.py 
----------------------------------------------------------------------
LFRS1: 0010011100010111101
LFRS2: 0110101111100000111101
LFRS3: 00111000100010110011101
0 ^ 0 = 0
keysteam: 0
----------------------------------------------------------------------
LFRS1: 1001001110001011110
LFRS2: 0110101111100000111101
LFRS3: 00011100010001011001110
1 ^ 1 = 0
keysteam: 00
----------------------------------------------------------------------
LFRS1: 0100100111000101111
LFRS2: 1011010111110000011110
LFRS3: 00011100010001011001110
0 ^ 1 = 1
keysteam: 001
----------------------------------------------------------------------
LFRS1: 0010010011100010111
LFRS2: 1101101011111000001111
LFRS3: 00011100010001011001110
1 ^ 0 = 1
keysteam: 0011
----------------------------------------------------------------------
LFRS1: 1001001001110001011
LFRS2: 0110110101111100000111
LFRS3: 00011100010001011001110
1 ^ 1 = 0
keysteam: 00110
----------------------------------------------------------------------
LFRS1: 0100100100111000101
LFRS2: 0110110101111100000111
LFRS3: 00001110001000101100111
1 ^ 0 = 1
keysteam: 001101
----------------------------------------------------------------------
LFRS1: 0100100100111000101
LFRS2: 0011011010111110000011
LFRS3: 10000111000100010110011
1 ^ 1 = 0
keysteam: 0011010
```

`Also you can convert your text to binary like below:`

```py
text_to_binary = ''.join(format(ord(i),'b') for i in "Hello world")
print(text_to_binary[:19])
print(text_to_binary[19:41])
print(text_to_binary[41:64])

# OutPut >
#   1001000110010111011
#   0011011001101111100000 
#   11101111101111111001011
```

## References 📚
> [https://asecuritysite.com/encryption/a5]()

> [https://en.wikipedia.org/wiki/A5/1]()

> [https://www.researchgate.net/figure/The-A5-1-Stream-Cipher_fig1_228963335]()


