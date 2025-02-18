from trackeval.datasets.mot_challenge_2D_box import MOTChallenge2DBox

class MyCustomDataset(MOTChallenge2DBox):
    def __init__(self, config=None):
        super().__init__(config)
        # 关键配置
        self.gt_fol = 'MyDataset'               # 数据集根目录
        self.tracker_fol = 'track_results'      # 跟踪结果目录
        self.seq_list = ['seq_01', 'seq_02', 'seq_03']  # 你的所有序列名称
        self.class_list = ['aircraft']          # 唯一类别名称
        self.class_name_to_class_id = {'aircraft': 1}  # 类别ID映射
        self.use_3d = False                     # 使用2D框