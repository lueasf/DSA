# A. Mix Mex Max on Atto Round 1 (Codeforces Round 1041, Div. 1 + Div. 2) Aug/07/2025

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    valeur_k = -100
   
    possible = True
   
    for nombre in a:
        if nombre == 0:
            possible = False
            break

        elif nombre != -1:
            if valeur_k == -100:
                valeur_k = nombre
            else:
                if nombre != valeur_k:
                    possible = False
                    break

    if possible:
        print("YES")
    else:
        print("NO")

"""
Summary of Problem-Solving for Codeforces A. Mix Mex Max

1. Understanding the Problem
Goal: Given an array 'a' with some missing elements (-1), determine if we can replace the -1s with non-negative integers to make the array "good".

Definition of a "Good" Array: An array is good if for every consecutive 3-element window [a_i, a_{i+1}, a_{i+2}], the following equation holds:
mex(...) = max(...) - min(...)

Key Definition mex(b): The Minimum Excluded non-negative integer from a collection 'b'. For example, mex([1, 5, 2]) = 0, and mex([0, 1, 3]) = 2.


2. Deconstructing the Core Condition
The key is to analyze what the condition "mex = max - min" implies for a 3-element window. We can do this by considering the possible values of mex.

Case 1: mex = 0
This means the number 0 is not present in the window. All three numbers are positive.
The equation becomes 0 = max - min, which means max = min.
If the maximum and minimum values are the same, all three numbers must be identical.
Conclusion: A valid window is of the form [k, k, k] where k is a positive integer (e.g., [2, 2, 2]). This is a valid configuration.

Case 2: mex = 1
This means 0 is present, but 1 is not present.
Since 0 is in the window, min = 0.
The equation becomes 1 = max - min  => 1 = max - 0 => max = 1.
This leads to a contradiction: The maximum element must be 1, but the number 1 is not allowed to be in the window for its mex to be 1.
Conclusion: This case is impossible.

Case 3: mex = 2
This means 0 and 1 are present, but 2 is not.
Again, min = 0.
The equation becomes 2 = max - min => 2 = max - 0 => max = 2.
Another contradiction: The maximum element must be 2, but the number 2 is not allowed to be in the window for its mex to be 2.
Conclusion: This case is also impossible.

General Case (mex > 0): Any case where mex > 0 will lead to a similar contradiction.


3. The Key Insight
The analysis reveals a massive simplification:
- The only way a 3-element window can satisfy the condition is if it is of the form [k, k, k] for some positive integer k > 0.
- Since this must be true for every sliding window in the array, it forces the entire array to be uniform. If [a_1, a_2, a_3] is [k, k, k], and [a_2, a_3, a_4] must also be a valid window, it must also be [k, k, k], forcing a_4 to be k. This propagates through the entire array.
- Final Conclusion: A "good" array must consist of a single, repeating positive integer k.


4. The Resulting Algorithm
The problem is no longer about mex or complex calculations. It simplifies to a consistency check: can the given array 'a' be made into an array of [k, k, k, ...] where k > 0?

This leads to two simple failure conditions:
1. The array contains a 0. This is impossible, as k must be positive.
2. The array contains two or more different positive numbers (e.g., a 3 and a 5). This is impossible, as k must be a single, unique value.

If neither of these failure conditions is met, the answer is "YES". Otherwise, it's "NO".

5. Step-by-Step Implementation Plan

1. Initialize a variable, 'target_k', to a sentinel value (e.g., -1 or None) to indicate that we haven't found a required number yet.
2. Iterate through each number in the input array 'a'.
3. If the number is -1, it's a wildcard. We can ignore it and move on.
4. If the number is 0, we have found an impossible value. The answer is immediately "NO". Stop processing.
5. If the number is positive:
   - If 'target_k' has not been set yet, set 'target_k' to this number. This is the value all other numbers must match.
   - If 'target_k' has already been set, check if the current number is equal to 'target_k'. If they are different, the array is inconsistent. The answer is "NO". Stop processing.
6. If the loop completes without ever returning "NO", it means the array is either empty of non-'-1' values or all existing numbers are consistent. The answer is "YES"."""