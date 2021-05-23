# i-ok

## short desc
small math esolang for small numbers and equations

## how to use
| chars   | desc |
| --------| --------|
| i+ or i++| adds    |
| i- or i--| subtracts|
| i*      | multiples by 2|
| i/      | divides by 2|

```
i+ i+ i- i* this would equal 2
```
### letters
turning the digit over 15 converts numbers into letters
```
i+ i+ i* i* i* this would be 'a'
```
the range for letters is a-i
going over 24 turns result into null

the same applies for going negative, special characters range from ! to  )  going above 26 results in null

### setting up
download the iok.py, and import it
``` python
from iok import run
```

