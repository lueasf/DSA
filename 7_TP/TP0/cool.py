# Les nombres cools, sont des nombres qui sont ordonnés de façon croisante de gauche à droite
import sys

#q1
def estCool(list : list[int]) -> bool:
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

#q2
def pCool(list : list[int])->list[int]:

    num = int(''.join(map(str,list)))

    while(num > 0):
        num -=1

        num_list = [int(i) for i in str(num)]
        if estCool(num_list):
            return num_list
    return []

#q3
if __name__ == "__main__": 
    if len(sys.argv) != 2:
        print("Veuillez saisir un nombre.")
        sys.exit(1)
 
    number_str = sys.argv[1] # 
    number_list = [int(d) for d in number_str]
     
    cool_number = pCool(number_list)
     
    print("Le premier nombre cool qui précède", number_str, "est :", ''.join(map(str, cool_number)))