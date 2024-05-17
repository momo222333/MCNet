import matplotlib.pyplot as plt

list = [0 for _ in range(60)]
right_list = [0 for _ in range(60)]
wrong_list = [0 for _ in range(60)]
accuracy_list = [0 for _ in range(60)]
actions_list = [x for x in range(1, 61)]

# print(right_list)
# print(wrong_list)

def function_read(file):
    lines = file.readlines()
    length = len(lines)
    print(length)
    numbers = []
    for line in lines:
        num_list = line.split(',')
        numbers = []
        for num in num_list:
            numbers.append(int(num))

        left_num = numbers[0]
        right_num = numbers[1]

        # print(left_num, right_num)

        if left_num == right_num:
            right_list[right_num] = right_list[right_num] + 1
            # list[right_num] = list[right_num] + 1

        else:
            wrong_list[right_num] = wrong_list[right_num] + 1
            # list[right_num] = list[right_num] + 1

        list[right_num] = list[right_num] + 1

        accuracy_list[right_num] = round(right_list[right_num] / list[right_num], 2)

    print(right_list)
    print(wrong_list)
    print(list)
    print(accuracy_list)
    # print(actions_list)

with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/joint_21/runs-65-20345_right.txt', 'r') as file:
    function_read(file)

# 绘制线形图
plt.plot(actions_list, accuracy_list, marker=".", color='blue')

with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/bone_21/runs-40-12520_right.txt', 'r') as file:
    function_read(file)

# 绘制线形图
plt.plot(actions_list, accuracy_list, marker=".", color='orange')

# 添加标题、x轴标签和y轴标签
# plt.title("Line Chart")
plt.xlabel("Actions")
plt.ylabel("Accuracy")
# 设置图例
plt.legend(['joint_21','joint_21+bone_21'], loc='lower right')
plt.ylim(0.5, 1)
# 显示图表
plt.show()