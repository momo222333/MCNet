import argparse
import pickle
import os

import numpy as np
from tqdm import tqdm

'''
Dataset split wise alpha values

NTU60 Xsub : [2, 1.8, 0.7]
NTU60 XView : [2.1, 1.6, 0.7]

NTU120 XSub : [2.2, 1.5, 0.7]
NTU120 XSet : [2.1, 2, 0.8]

NTU60x : [3.4, 2, 1]
NTU120x : [2.4, 2.2, 1]

'''


if __name__ == "__main__":
    


    j_21 = "/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/joint_21/epoch1_test_score.pkl"

    b_21 = "/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/bone_21/epoch1_test_score.pkl"

    j_2 = "/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/joint_2/epoch1_test_score.pkl"

    b_2 = "/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/bone_2/epoch1_test_score.pkl"

    j_1 = "/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/joint_1/epoch1_test_score.pkl"

    b_1 = "/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/bone_1/epoch1_test_score.pkl"

    # vel = "/public/home/zxh_8991/project/CTR-GCN-main-MC/work_dir/ntu60/xsub/body(vel)/epoch1_test_score.pkl"

    with open(j_21, 'rb') as r1:
        r1 = list(pickle.load(r1).items())

    with open(b_21, 'rb') as r2:
        r2 = list(pickle.load(r2).items())

    with open(j_2, 'rb') as r3:
        r3 = list(pickle.load(r3).items())

    with open(b_2, 'rb') as r4:
        r4 = list(pickle.load(r4).items())

    with open(j_1, 'rb') as r5:
        r5 = list(pickle.load(r5).items())

    with open(b_1, 'rb') as r6:
        r6 = list(pickle.load(r6).items())

    # with open(vel, 'rb') as r7:
    #     r7 = list(pickle.load(r7).items())



    right_num = total_num = right_num_5 = 0

    parser = argparse.ArgumentParser()

    arg = parser.parse_args()


    label = []
    npz_data = np.load('/public/home/zxh_8991/data/NTU60_CS.npz')
    label = np.where(npz_data['y_test'] > 0)[1]


    # arg.alpha = [0.6, 1.0, 0.6]    #  93.1219%   joint+bone+limb(4)   sub_60
    # arg.alpha = [0.6, 0.8, 0.6]    #  93.0733%  joint+bone+limb(vel)   sub_60

    # arg.alpha = [1.0, 0.8, 0.6]    #  96.8255%   joint+bone+limb(4)   view_60
    # arg.alpha = [0.6, 0.6, 0.5]    #  96.8149%   joint+bone+limb(vel)  view_60

    # arg.alpha = [0.6, 0.8, 0.8]      #  91.3866%   joint+bone+limb(4)   CSet
    # arg.alpha = [0.6, 1.0, 0.8]      #  90.8889%   joint+bone+limb(2)   CSet



    # arg.alpha = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6]    #  93.0 %   joint_21+bone_21+joint_2+bone_2+joint_1+bone_1    sub_60


    # arg.alpha = [0.6, 0.6, 0.4, 0.6, 0.2, 0.6]  #  93.0 %   joint_21+bone_21+joint_2+bone_2+joint_1+bone_1    60  sub
    # arg.alpha = [0.6, 0.4, 0.6, 0.6, 0.6, 0.6]  # 97.0 %   joint_21+bone_21+joint_2+bone_2+joint_1+bone_1    60  view

    # arg.alpha = [0.5, 0.6, 0.4, 0.6, 0.4, 0.6]  # 89.6856%   joint_21+bone_21+joint_2+bone_2+joint_1+bone_1    120 sub

    # arg.alpha = [0.5, 0.6, 0.4, 0.6, 0.4, 0.6]  # 91.3630%   joint_21+bone_21+joint_2+bone_2+joint_1+bone_1    120 set


# all

    arg.alpha = [0.6, 0.6, 0.4, 0.8, 0.4, 0.6]  #    joint_21+bone_21+joint_2+bone_2+joint_1+bone_1    60  sub




    for i in tqdm(range(len(label))):
        l = label[i]
        _, r11 = r1[i]
        _, r22 = r2[i]
        _, r33 = r3[i]
        _, r44 = r4[i]
        _, r55 = r5[i]
        _, r66 = r6[i]
        # _, r77 = r7[i]

        r = r11 * arg.alpha[0] + r22 * arg.alpha[1] + r33 * arg.alpha[2] + r44 * arg.alpha[3] + r55 * arg.alpha[4] + r66 * arg.alpha[5]

        # r = r11 * arg.alpha[0] + r22 * arg.alpha[1] + r33 * arg.alpha[2] + r44 * arg.alpha[3] + r55 * arg.alpha[4] + r66 * arg.alpha[5]

        # r = r11 * arg.alpha[0] + r22 * arg.alpha[1] + r33 * arg.alpha[2] + r55 * arg.alpha[3] + r66 * arg.alpha[4] + r77 * arg.alpha[5]

        rank_5 = r.argsort()[-5:]
        right_num_5 += int(int(l) in rank_5)
        r = np.argmax(r)
        right_num += int(r == int(l))
        total_num += 1
    acc = right_num / total_num
    acc5 = right_num_5 / total_num

    print('Top1 Acc: {:.4f}%'.format(acc * 100))
    print('Top5 Acc: {:.4f}%'.format(acc5 * 100))
