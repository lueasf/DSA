def validExpression(values, constraints):
    def check_valid(perm):
        curr = perm[0]
        if (constraints[0] == 'P' and curr <= 0) or (constraints[0] == 'N' and curr >= 0):
            return False
        for i in range(1, len(perm)):
            curr += perm[i]
            if (constraints[i] == 'P' and curr <= 0) or (constraints[i] == 'N' and curr >= 0):
                return False
        return True

    def generate_permutations(current_perm, remaining):
        if not remaining:
            if check_valid(current_perm):
                return current_perm
            return None

        for i in range(len(remaining)):
            for sign in [1, -1]:
                new_perm = current_perm + [sign * remaining[i]]
                new_remaining = remaining[:i] + remaining[i+1:]
                result = generate_permutations(new_perm, new_remaining)
                if result:
                    return result

        return None

    result = generate_permutations([], values)
    return result if result else []

# Test
values = [19, 4, 21]
constraints = ['P', 'N', 'P']
result = validExpression(values, constraints)
print(result)