# Rail-Fence-Cipher-with-N-rails-amp-Row-Transposition-Cipher-Encryption

1.Rail Fence Cipher (with N rails):
To rearrange characters in a zigzag (rail-like) pattern to conceal the actual message.
Procedure:
1.Input:
oPlaintext message (string).
oKey = number of rails (integer ≥ 2).
2.Preprocessing:
oRemove all spaces from the message.
oConvert to lowercase (optional, for consistency).
3.Rail Setup:
oCreate a list of empty strings/lists equal to the number of rails.
4.Zigzag Logic:
oInitialize:
rail_index = 0 (starting from top rail).
direction = 1 (downward).
oFor each character in message:
Append character to the current rail.
Update rail index:
If at top (rail 0), set direction to down (1).
If at bottom (rail N-1), set direction to up (-1).
Move to next rail: rail_index += direction.
5.Encryption:
oConcatenate all rails from top to bottom.
oFinal encrypted text = rail_1 + rail_2 + ... + rail_N.
6.Output:
oShow each rail content.
oShow encrypted message.
oOptionally: for ch in rail1 + rail2 + ...: print(ch, end="").


WORKING VIDEO:
https://www.loom.com/share/255a9b8881674e3b8735bdd7311b77d9?sid=861ba7b6-bce4-4581-a145-a079f8f1aba3

2.Row Transposition Cipher
1. Input
Plaintext message: A string of letters only (no spaces, digits, or punctuation).
Example:
hellostreamlit
Key: A numeric string representing column positions.
Example:
"431256"

✅ 2. Preprocessing
The input is already:
oAlphabetic
oLowercase or is converted to lowercase
Example after preprocessing:
hellostreamlit

✅ 3. Matrix Setup
Let N = length of the key = number of columns
"431256" → N = 6
Let M = length of the plaintext message
"hellostreamlit" → M = 14
Calculate the number of rows needed:
rows = ceil(M / N) → rows = ceil(14 / 6) = 3

✅ 4. Create Matrix (Row-wise Filling)
Fill the matrix row by row with the letters from the message.
Matrix:
C1	C2	C3	C4	C5	C6
h	e	l	l	o	s
t	r	e	a	m	l
i	t				
(If characters run out, leave remaining cells blank)

✅ 5. Key Mapping
Key = "431256"
Key digits = [4, 3, 1, 2, 5, 6]
Sort the key digits and get their original positions to determine column read order:
Key Digit	Original Position (Index)
1	2
2	3
3	1
4	0
5	4
6	5
So column read order is:
[2, 3, 1, 0, 4, 5]
(Corresponding to columns: 3rd, 4th, 2nd, 1st, 5th, 6th)

✅ 6. Encryption Process
For each column in the sorted key order, read characters top to bottom, skipping blanks.
Column 3 (index 2): l, e
Column 4 (index 3): l, a
Column 2 (index 1): e, r, t
Column 1 (index 0): h, t, i
Column 5 (index 4): o, m
Column 6 (index 5): s, l
Concatenated Ciphertext:
lelaerthtiomsl

✅ 7. Output
Encrypted Message: lelaerthtiomsl


WORKING VIDEO:
https://www.loom.com/share/67d3eadbe76f429eb3d84112a8023214?sid=b566e716-b95f-44ca-b25c-5d1fe6ecb943
