no_test_cases=int(input())
for i in range(no_test_cases):
    cost=input()
    no_input_lines=int(input())
    cost_split=cost.split(" ")
    cost_purple=cost_split[0]
    cost_green=cost_split[1]
    cost_purple1=int(cost_purple)
    cost_green1=int(cost_green)
    total_purple1=0
    total_green1=0
    total_purple2=0
    total_green2=0
    for j in range(no_input_lines):
        who_won=input()
        who_won_split=who_won.split(" ")
        A=who_won_split[0]
        B=who_won_split[1]
        a=int(A)
        b=int(B)
        a_won1=(a*cost_purple1)
        total_purple1+=a_won1
        b_won1=(b*cost_green1)
        total_green1+=b_won1
        a_won2=(a*cost_green1)
        total_green2+=a_won2
        b_won2=(b*cost_purple1)
        total_purple2+=b_won2
    case1=total_purple1+total_green1
    case2=total_purple2+total_green2
    if(case1>case2):
        print(case2)
    else:
        print(case1)
