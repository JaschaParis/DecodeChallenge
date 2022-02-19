# Description
This repository contains the contribution to a challenge writing a linear cellular automaton.

# Usage
The programm takes input from stdin as described in: [Challenge](https://mailing.demcon.com/lp/decode-demcon-linear-cellular-automata)

You can test the programm with the bash script supplied:
```
./test_automaton
```

You can run your own cases with:
```
input="A 11 10\n
init_start 6 init_end"

echo $input | python3 automaton.py
```

# Featues
Notable features of this solution:
  * Implementation of the automaton itself with only few characters of code (`gen[1:-1] = ac[4*np.roll(gen,1)+2*gen+np.roll(gen,-1)][1:-1]`)
  * Few lines of code in summary
  * Using only one for-loop as loops are normally inefficient in python

