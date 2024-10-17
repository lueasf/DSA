def validExpression(values, constraints):
    def aux(values, constraints, solution, curr_sum):
        if values == []:
            return solution
        
        for i,j in enumerate(values):
            for signed_j in [-j,+j]:
                curr_sum += signed_j
                if (constraints[0] == 'P' and curr_sum >= 0) or (constraints[0] == 'N' and curr_sum < 0):
                    s = aux(values[:i]+values[i+1:], constraints[1:],solution + [signed_j],curr_sum)
                    if s != []:
                        return s
                curr_sum -= signed_j
        return []
    return aux(values, constraints,[],0)
    

# Test
values = [19, 4, 21]
constraints = ['P', 'N', 'P']
result = validExpression(values, constraints)
print(result)