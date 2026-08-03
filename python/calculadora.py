while True:
    opcao = input("===== ... =====\n1. calculos basicos")
    match opcao:
        case '1':
            cont = True 
            while cont:
                calc = input("===== Operações =====\nSoma : +\nSubtração : -\nMultiplicação : *\nDivisão : /\n=>")

                for i in calc: # busca caracteres invalidos 
                    if i.isnumeric == False or i not in ["-",'+','/','*','=']:
                        carac_invalido = ''
                        carac_invalido = carac_invalido + i

                if len(calc) < 2 or calc[1].isnumeric == True:
                    print("digite o calculo todo, ex: 1+1, ou adicione um operador para adicionar mais um calculo, ex -2, e para terminar o calculo digite = ")

                elif carac_invalido > 0:
                    print(f'Erro: Os caracteres {list(carac_invalido)} são invalidos para a operação')
                else:
                    for i in calc:
                        nums=[]
                        op=[]
                        num=''
                        result = ''
                        if i.isnumeric() == True:
                            num = num + i
                        elif i in ['+', '-', '*', '/']:
                            op.append(i) 
                            nums.append(num)
                            num = ''
                        elif i == '=':
                            for i in len(op):
                                if op[i] == '+':
                                    if i == "0":
                                        result = int(nums[0] + nums[1])
                                    else:
                                        result = result + int(nums[i+1])
                                elif op[i] == '-':
                                    pass
                                elif op[i] == '*':
                                    pass
                                elif op[i] == '/':
                                    pass
                    print(calc + '=' + result)









# calc = input('calc : ')

# nums=[]
# op=[]
# num=''
# result = 0

# for i in calc:
#     print('i ', i) 

#     if i.isnumeric() == True:
#         num = num + i
#         print('num1 ', num)


#     elif i in ['+', '-', '*', '/']:
#         op.append(i) 
#         nums.append(float(num))
#         print('nums1 ', nums)
#         print('num2 ', num)
#         num=''

#     else:
#         pass

# nums.append(float(num))
# print('nums2 ', nums)

# #! erro : não tem a ierarquia operação, que é * e / vir antes de + e -
# for i in range(0, len(op)):
#     print(type(i))
#     print(i)
#     if op[i] == '+':
#         print('op',op[i])
#         if i == 0:
#             result = nums[0] + nums[1]
#         else:
#             result = result + nums[i+1]

#     elif op[i] == '-':
#         if i == 0:
#             result = nums[0] - nums[1]
#         else:
#             result = result - nums[i+1]

#     elif op[i] == '*':
#         if i == 0:
#             result = nums[0] - nums[1]
#         else:
#             result = result - nums[i+1]

#     elif op[i] == '/':
#         if i == 0:
#             result = nums[0] - nums[1]
#         else:
#             result = result - nums[i+1]

# print(calc, '=' , result)


                    # nums = []
                    # num = ''
                    # for i in calc :
                    #     print("i"+i)
                    #     if i.isnumeric() == True:
                    #         num = num + i
                    #         print(num)
                    #     elif i in ['+', '-', '*', '/']:
                    #         op = i
                    #         nums.append(num)
                    #         num = ''
                            
                    #         print("nums",nums)

                    #     else:
                    #         pass
                        
                    # nums.append(num)
                    # print("nums",nums)
                    # if op == "+":
                    #     print(f'{nums[0]} + {nums[1]} = {int(nums[0]) + int(nums[1])}')
