```python
from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2) - Counter(s1)) == 0
```

```python
def scramble(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))
```

```python
def scramble(s1,s2):
    return all( s1.count(x) >= s2.count(x) for x in set(s2))
```