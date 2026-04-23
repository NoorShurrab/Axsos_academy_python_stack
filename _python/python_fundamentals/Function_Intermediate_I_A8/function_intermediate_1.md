# randInt()
The randInt function calculates a random number by determining the "distance" between a minimum and maximum value, scaling the output of random.random(), and then shifting it to the correct starting point.

The core logic relies on the following linear transformation:
***$$num = random() \times (max - min) + min$$***
1. Multiplying random.random() (which is $0 \le x < 1$) by the difference $(max - min)$ stretches the range to the desired width.
2. Adding the min value moves that range to start at the correct number.
3. The round() function converts the resulting float into the nearest integer.