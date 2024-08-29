# Challenge Name

Cecure Cerver

# Description

Many Cecure web Cervers are written in C

# Summary

Vulnerability occurs in `STRING_EQUALS`.
```c
#define STRING_EQUALS(s1, s2) (!strncmp(s1, s2, strlen(s1)))
```
If `strlen(s1)` contains only 1 character, only the first character of each string will be compared.

Since the password and username only contains hex digits, the credentials can be bruteforced easily.

# Author

jro

# Hints

N/A

# Flag

`grey{3xpl0171n6_l061c_bu65}`
