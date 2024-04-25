# AI_RedBlueNim
Red Blue Nim Problem

Programming Language used: Python 3.11.4

RedBlueNim.py

Instruction needed to execute the program:

Command : python RedBlueNim.py  red blue <version> <player> depth

Examples:

when all the parameters are given:

python RedBlueNim.py 14 15 misere human 1

when depth is not given:

python RedBlueNim.py 14 15 misere human 

when default player is computer:

python RedBlueNim.py 14 15 misere

when default version is standard:

python RedBlueNim.py 14 15

and few more combinations can be done


Methods: 

find_alpha_beta(): We implement min max algorithm with alpha beta pruning to make sure the optimal choice that needed to be picked inorder to win the game. We calculate alpha beta pruing using recursive algorithm and calculate the scores of each game when we hit the base case when one of the pile is empty.

eval is used to evaluate the score in RedBlueNim. we multiply the left red piles with 2 and blue piles with 3. And these values are assigned to a varible which checks alpha and beta values and update the scores accordingly.
