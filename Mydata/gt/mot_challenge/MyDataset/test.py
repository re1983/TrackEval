import os
import pandas as pd

def validate_dataset():
    # for seq in ['seq_01', 'seq_02', 'seq_03']:  # 替换为你的序列名
    for seq in os.listdir('MyDataset-all'):
        seq_path = os.path.join('MyDataset-all', seq)
        print(f"检查 {seq_path}")
        if not os.path.exists(seq_path):
            print(f"错误：序列目录 {seq} 不存在")
            continue

        # 检查 img1 图像
        img_dir = os.path.join(seq_path, 'img1')
        if not os.path.exists(img_dir):
            print(f"错误：{seq} 缺少 img1 目录")
        else:
            images = sorted([f for f in os.listdir(img_dir) if f.endswith('.jpg')])
            if len(images) == 0:
                print(f"错误：{seq}/img1 无图像文件")
            else:
                expected_frames = set(range(1, len(images)+1))
                actual_frames = set(int(f.split('.')[0]) for f in images)
                if expected_frames != actual_frames:
                    print(f"错误：{seq} 图像命名不连续")

        # 检查 gt.txt
        gt_file = os.path.join(seq_path, 'gt', 'gt.txt')
        if not os.path.exists(gt_file):
            print(f"错误：{seq} 缺少 gt/gt.txt")
        else:
            gt = pd.read_csv(gt_file, header=None)
            if gt.shape[1] != 10:
                print(f"错误：{seq}/gt.txt 列数不等于10")
            if not (gt[7] == 1).all():
                print(f"错误：{seq}/gt.txt 类别列不全为1")

        # 检查 track_results
        track_file = os.path.join('track_results', f'{seq}.txt')
        if not os.path.exists(track_file):
            print(f"警告：{seq}.txt 未找到于 track_results 目录")
        else:
            track = pd.read_csv(track_file, header=None)
            if track.shape[1] != 10:
                print(f"错误：{seq}.txt 列数不等于10")
            if not (track[7] == 1).all():
                print(f"错误：{seq}.txt 类别列不全为1")

validate_dataset()