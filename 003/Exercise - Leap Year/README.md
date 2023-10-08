## Instructions

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366,
with an extra day in February. The reason why we have leap years is really
fascinating, [this video](https://www.youtube.com/watch?v=xX96xng7sAE) does it more justice.

This is how you work out whether if a particular year is a leap year.

- On every year that is divisible by 4 with no remainder.
- Except every year that is evenly divisible by 100 with no remainder.
- Unless the year is also divisible by 400 with no remainder.

If English is not your first language or if the above logic is confusing, try
using [this flow chart](https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Leap%20Algorithm#R7VpNc9owEP01HNuxJdmYY4CkzTTNdEpmmhyFrdhqhcXIIkB+fSUsY4wcQhqwC+0p0urDu29Xu08KHTiYLD4JPE2+8oiwDnCiRQcOOwC4CPjqj5Ysc0k3gLkgFjQyk0rBiD4TI3SMdEYjklUmSs6ZpNOqMORpSkJZkWEh+Lw67ZGz6lenOCaWYBRiZkt/0EgmuTQA3VL+mdA4Kb7s+r18ZIKLycaSLMERn2+I4GUHDgTnMm9NFgPCNHgFLvm6qxdG14oJksp9FoDbYTJlQFxPomj0Jbzr4tT9YJTN5LIwmETKftPlQiY85ilml6W0L/gsjYje1VG9cs4N51MldJXwJ5FyaZyJZ5IrUSInzIwqhcXyXq//6BXdB7PdqjNcVHpL08t11Qq+CIERZXwmQrLD7iKUsIiJ3DEPrB2lIpzwCVH6qHWCMCzpU1UPbEItXs8rvaEaxiFvcI7Z9wmzmfnS6O7i+53lstIhGt15QiUZTfHK/rk6lVXwzZ5ESLLYDaNttlkAYE85brVoWZxWE+Tz8oy4xRFONs4Hco6ElfePBjLYM5DhOwN5tfRCCLzcmDDlNJXZxs7ftKAMFLcLtgKlyOulq/M9S8evlfvzWPD/x8LOWHCdQwSD5W3kdre97W8d91w1s64Mg7fGFQLWl5qIK2Dl4+tMr9GahYzglGkjOsBnCv3+WKhWrFsRfaIZHas4A85YT0EdeGVn8YRPxrOsmQxe8Jcif3dr8jf07PwdHCt/QwvbW65xvSHK/HcVvEfK2IAzLlZr4WMQkjBU8kwK/otsjIwDD3nOYQB23SrA65PQWoHs1gBsAasMllX0MKNxqtqhMpwooPoaFqr48YUZmNAoyjMoyegzHq+20iiaQ6z29fodb6j3Ukkzy/PngeLYDSwm0rOBhjU4g2PhHFg4P5Ds5IGG/j5AoyaBdmErZX5B5X1RyFX7oaz4qlfWeN0pSvxfQA2KVPM6N2j3xhO06VP3XH2KWvWpcyjapG+ZLRMn6IPX63pdvTkacXJtVnpwzhR5JIhQHWcKwBj6/oFIqVfFFtaR0kY5E2jnVeFESwzaMx2BVtMRaOd14ERLzL4+dXutlhh0qBKD2i8xyNum2rWJsI5rH6/I9M6lyHi9bXRRzUWm4TJjM6RzuDOi3hZXClq+MRYmnNcbCHS3I7oO6EbfQIDNSc8AaGQBDdt+bAL2s+k5ZA47Sdch3WzusCnGST9QQ9RkHVTd8ocO+b9jyp+LwMvf).

e.g. The year 2000:

- 2000 ÷ 4 = 500 (Leap)
- 2000 ÷ 100 = 20 (Not Leap)
- 2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

- 2100 ÷ 4 = 525 (Leap)
- 2100 ÷ 100 = 21 (Not Leap)
- 2100 ÷ 400 = 5.25 (Not Leap)

**Warning:** your output should match the Example Output format exactly, including spelling and punctuation.

### Example Input 1

```
2400
```

### Example Output 1

```
Leap year
```

### Example Input 2

```
1989
```

### Example Output 2

```
Not leap year
```