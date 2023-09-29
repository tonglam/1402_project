import random


def get_random_imei():
    # 定义一个长度为14字符类的数字
    take_two_num = 0
    num = str(random.randint(10000000000000, 99999999999999))
    # 计算最后一位校验值
    num_list = list(num)
    # 数字和
    math_sum = 0
    for i in range(1, len(num_list) + 1):
        # 如果是偶数
        if i % 2 == 0:
            take_two_num = int(num_list[i - 1]) * 2
            # 判断乘于2之后的数，是一位还是二位，二位的话就，将个位和十位上的数字相加，一位就保持不变
        if len(str(take_two_num)) == 2:
            for j in list(str(take_two_num)):
                math_sum = int(j) + math_sum
        else:
            math_sum = take_two_num + math_sum
    # 如果是奇数的话，直接相加
    else:
        math_sum = int(num_list[i - 1]) + math_sum

    # 根据math_sum得出校验位
    last_num = list(str(math_sum))[-1]
    if last_num == 0:
        check_num = 0
        imei = num + str(check_num)
        return imei

    else:
        check_num = 10 - int(last_num)
        imei = num + str(check_num)
        return imei
