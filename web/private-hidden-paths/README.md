# Challenge Name

Private Hidden Paths

# Challenge Summary

Tokens created using PHP's `pack` function with user controlled format string. This allows the attacker to delete the previously written permissions integer using the `X` format operator. Once the attacker has gained `0x1337` (aka pro) permissions, adding a `c` to the end of `/pro` unlocks the `/proc` filesystem. They can then use `/proc/self/root/flag.txt` to access the flag.

# Details

Check out my Personal Home Page!

# Author

jro

# Hints

None

# Flag

`grey{1_l0v3_php_17_15_50_53cur3}`

# Learning Objectives

Use of proc filesystem for arbitrary file disclosure, looking at some relatively rarely used functions in PHP.
