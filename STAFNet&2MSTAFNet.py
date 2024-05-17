import matplotlib.pyplot as plt
import numpy as np

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


# 2MSTAFNet ntu60 xsub
# with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/joint_21/runs-65-20345_right.txt', 'r') as file:
#     function_read(file)
# with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/bone_21/runs-40-12520_right.txt', 'r') as file:
#     function_read(file)
# with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/joint_2/runs-38-11894_right.txt', 'r') as file:
#     function_read(file)
# with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/bone_2/runs-63-19719_right.txt', 'r') as file:
#     function_read(file)
# with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/joint_1/runs-63-19719_right.txt', 'r') as file:
#     function_read(file)
# with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/bone_1/runs-37-11581_right.txt', 'r') as file:
#     function_read(file)

# 2MSTAFNet ntu60 xview
with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xview/joint_21/runs-58-17052_right.txt', 'r') as file:
    function_read(file)
with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xview/bone_21/runs-63-18522_right.txt', 'r') as file:
    function_read(file)
with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xview/joint_2/runs-63-18522_right.txt', 'r') as file:
    function_read(file)
with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xview/bone_2/runs-57-16758_right.txt', 'r') as file:
    function_read(file)
with open('/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xview/joint_1/runs-60-17640_right.txt', 'r') as file:
    function_read(file)

# 绘制线形图
plt.plot(actions_list, accuracy_list, marker=".", color='red')


# STAFNet  ntu60 xsub
# with open('/public/home/zxh_8991/project/CTR-GCN-main/work_dir/ntu60/xsub/joint_21_aff(res, out)&kd/runs-59-18467_right.txt', 'r') as file:
#     function_read(file)
# with open('/public/home/zxh_8991/project/CTR-GCN-main/work_dir/ntu60/xsub/bone_21_aff(res, out)&kd/runs-41-12833_right.txt', 'r') as file:
#     function_read(file)
# with open('/public/home/zxh_8991/project/CTR-GCN-main/work_dir/ntu60/xsub/limb_aff(res, out)&kd/runs-65-20345_right.txt', 'r') as file:
#     function_read(file)

# STAFNet  ntu60 xview
with open('/public/home/zxh_8991/project/CTR-GCN-main/work_dir/ntu60/xview/joint_21_aff(res, out)&kd/runs-66-19404_right.txt', 'r') as file:
    function_read(file)
with open('/public/home/zxh_8991/project/CTR-GCN-main/work_dir/ntu60/xview/bone_21_aff(res, out)&kd/runs-62-18228_right.txt', 'r') as file:
    function_read(file)
with open('/public/home/zxh_8991/project/CTR-GCN-main/work_dir/ntu60/xview/limb_aff(res, out)&kd/runs-59-17346_right.txt', 'r') as file:
    function_read(file)

# 绘制线形图
plt.plot(actions_list, accuracy_list, marker=".", color='blue')



# 添加标题、x轴标签和y轴标签
# plt.title("Line Chart")
plt.xlabel("Actions")
plt.ylabel("Accuracy")
# 设置图例
plt.legend(['STAFNet','2MSTAFNet'], loc='lower right')
plt.ylim(0.65, 1.01)
# plt.ylim(0.69, 1.01)
plt.yticks(np.arange(0.65, 1.01, 0.05))
# 显示图表
plt.show()


