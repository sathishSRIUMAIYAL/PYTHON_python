input_sub1,input_sub2,input_sub3,input_sub4,input_sub5=(input('Enter your Mark in 10 out of 500 ')).split(',')

Total=int(input_sub1)+int(input_sub2)+int(input_sub3)+int(input_sub4)+int(input_sub5)

if Total==175:
    print(" Pass")
    print('Your jest pass')
    if int(input_sub1)>=35:
        print_1='your Tamil mark is {}'.format(input_sub1)
        print(print_1)

elif Total >=200 and Total<=300:
    print("you pass and c+")

elif Total>=300 and Total<=400:
    print("you pass and B+")

elif Total >=400 and Total<=500:
    print("you pass and A+")

else:
    print('Fail')





