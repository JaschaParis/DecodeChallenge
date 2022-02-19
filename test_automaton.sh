#!/bin/sh

TEST_1="U 80 3000\n
init start -1 0 1 10 20 30 80 81 init_end\n
0 1 0 1 1 0 0 5"

TEST_2="A 11 10\n
init_start 6 init_end"

TEST_3="B 61 20\n
init start 20 40 init_end"

echo "Input 1:"
echo $TEST_1
echo "Result 1:"
start_time=$(date +%s.%3N)
echo $TEST_1 | python3 automaton.py
end_time=$(date +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo "Test 1 took:" $elapsed "s"

echo "Input 2:"
echo $TEST_2
echo "Result 2:"
start_time=$(date +%s.%3N)
echo $TEST_2 | python3 automaton.py
end_time=$(date +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo "Test 2 took:" $elapsed "s"

echo "Input 3:"
echo $TEST_3
echo "Result 3:"
start_time=$(date +%s.%3N)
echo $TEST_3 | python3 automaton.py
end_time=$(date +%s.%3N)
elapsed=$(echo "scale=3; $end_time - $start_time" | bc)
echo "Test 3 took:" $elapsed "s"