from util import *
import sys
sys.path.append("..")
sys.path.append(".")

import P3

print_test_start()

#
#   Test compute_unlock_patterns_count
#

with TestCase("compute_unlock_patterns_count - max_length = 0") as t:

    c = P3.compute_unlock_patterns_count(0)

    if c != 0:
        t.fail(f"Il n'y a pas de patterns avec 0 chiffres")

with TestCase("compute_unlock_patterns_count - max_length = 5") as t:

    c = P3.compute_unlock_patterns_count(5)

    if c != 9161:
        t.fail(f"Le nombre de schémas de longeur inférieure ou égale à 5 est 9161, la fonction a renvoyé {c}")

with TestCase("compute_unlock_patterns_count - max_length = 9") as t:

    c = P3.compute_unlock_patterns_count(9)

    if c != 389497:
        t.fail(f"Le nombre de schémas de longeur inférieure ou égale à 9 est 389497, la fonction a renvoyé {c}")


#
#   Test compute_unlock_patterns
#

with TestCase("compute_unlock_patterns - schémas 1") as t:

    patterns = P3.compute_unlock_patterns(1)

    true_patterns = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    if set(patterns) != true_patterns:
        t.fail(f"La fonction ne renvoie pas les bon schémas.\nShémas attendus : {true_patterns}\nSchémas manquants : {true_patterns - set(patterns)}\nSchémas manquants : {set(patterns) - true_patterns}")


with TestCase("compute_unlock_patterns - schémas 2") as t:

    patterns = P3.compute_unlock_patterns(2)

    true_patterns = set(['1', '1-2', '1-4', '1-6', '1-8', '1-5', '2', '2-1', '2-4', '2-7', '2-5', '2-3', '2-6', '2-9', '3', '3-2', '3-4', '3-6', '3-8', '3-5', '4', '4-1', '4-2', '4-3', '4-5', '4-7', '4-8', '4-9', '5', '5-1', '5-2', '5-3', '5-4', '5-6', '5-7', '5-8', '5-9', '6', '6-1', '6-2', '6-3', '6-5', '6-7', '6-8', '6-9', '7', '7-2', '7-4', '7-6', '7-8', '7-5', '8', '8-1', '8-4', '8-7', '8-5', '8-3', '8-6', '8-9', '9', '9-2', '9-4', '9-6', '9-8', '9-5'])

    if set(patterns) != true_patterns:
        t.fail(f"La fonction ne renvoie pas les bon schémas.\nShémas attendus : {true_patterns}\nSchémas manquants : {true_patterns - set(patterns)}\nSchémas manquants : {set(patterns) - true_patterns}")

with TestCase("compute_unlock_patterns - max_length = 0") as t:

    c = P3.compute_unlock_patterns(0)

    if len(c) != 0:
        t.fail(f"Il n'y a pas de patterns avec 0 chiffres")

with TestCase("compute_unlock_patterns - max_length = 5") as t:

    c = P3.compute_unlock_patterns(5)

    if len(c) != 9161:
        t.fail(f"Le nombre de schémas de longeur inférieure ou égale à 5 est 9161, la fonction en a renvoyé {len(c)}")

with TestCase("compute_unlock_patterns - max_length = 9") as t:

    c = P3.compute_unlock_patterns(9)

    if len(c) != 389497:
        t.fail(f"Le nombre de schémas de longeur inférieure ou égale à 9 est 389497, la fonction a renvoyé {len(c)}")



tests_summary()
