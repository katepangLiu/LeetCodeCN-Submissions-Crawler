def GetProblemId (string):
    mapping = {'两数之和': 1, '两数相加': 2, '无重复字符的最长子串': 3, '寻找两个有序数组的中位数': 4, '最长回文子串': 5, 'Z字形变换': 6, '整数反转': 7, '字符串转换整数(atoi)': 8, '回文数': 9, '正则表达式匹配': 10, '盛最多水的容器': 11, '整数转罗马数字': 12, '罗马数字转整数': 13, '最长公共前缀': 14, '三数之和': 15, '最接近的三数之和': 16, '电话号码的字母组合': 17, '四数之和': 18, '删除链表的倒数第N个节点': 19, '有效的括号': 20, '合并两个有序链表': 21, '括号生成': 22, '合并K个排序链表': 23, '两两交换链表中的节点': 24, 'k个一组翻转链表': 25, '删除排序数组中的重复项': 26, '移除元素': 27, '实现strStr()': 28, '两数相除': 29, '串联所有单词的子串': 30, '下一个排列': 31, '最长有效括号': 32,'搜索旋转排序数组': 33, '在排序数组中查找元素的第一个和最后一个位置': 34, '搜索插入位置': 35, '有效的数独': 36, '解数独': 37, '报数': 38, '组合总和': 39, '组合总和II': 40, '缺失的第一个正数': 41, '接雨水': 42, '字符串相乘': 43, '通配符匹配': 44, '跳跃游戏II': 45, '全排列': 46, '全排列II': 47, '旋转图像': 48, '字母异位词分组': 49, 'Pow(x,n)': 50, 'N皇后': 51, 'N皇后II': 52, '最大子序和': 53, '螺旋矩阵': 54, '跳跃游戏': 55, '合并区间': 56, '插入区间': 57, '最后一个单词的长度': 58, '螺旋矩阵II': 59, '第k个排列': 60, '旋转链表': 61, '不同路径': 62, '不同路径II': 63, '最小路径和': 64, '有效数字': 65, '加一': 66, '二进制求和': 67, '文本左右对齐': 68, 'x的平方根': 69, '爬楼梯':70, '简化路径': 71, '编辑距离': 72, '矩阵置零': 73, '搜索二维矩阵': 74, '颜色分类': 75, '最小覆盖子串': 76, '组合': 77, '子集': 78, '单词搜索': 79, '删除排序数组中的重复项II': 80, '搜索旋转排序数组II': 81, '删除排序链表中的重复元素II': 82, '删除排序链表中的重复元素': 83, '柱状图中最大的矩形': 84, '最大矩形': 85, '分隔链表': 86, '扰乱字符串': 87, '合并两个有序数组': 88, '格雷编码': 89, '子集II': 90, '解码方法': 91, '反转链表II': 92, '复原IP地址': 93, '二叉树的中序遍历': 94, '不同的二叉搜索树II': 95, '不同的二叉搜索树': 96, '交错字符串': 97, '验证二叉搜索树': 98, '恢复二叉搜索树': 99, '相同的树': 100, '对称二叉树': 101, '二叉树的层次遍历': 102, '二叉树的锯齿形层次遍历': 103, '二叉树的最大深度': 104, '从前序与中序遍历序列构造二叉树': 105, '从中序与后序遍历序列构造二叉树': 106, '二叉树的层次遍历II': 107, '将有序数组转换为二叉搜索树': 108, '有序链表转换二叉搜索树': 109, '平衡二叉树': 110, '二叉树的最小深度': 111, '路径总和': 112, '路径总和II': 113, '二叉树展开为链表': 114, '不同的子序列': 115, '填充每个节点的下一个右侧节点指针': 116, '填充每个节点的下一个右侧节点指针II': 117, '杨辉三角': 118, '杨辉三角II': 119, '三角形最小路径和': 120, '买卖股票的最佳时机': 121, '买卖股票的最佳时机II': 122, '买卖股票的最佳时机III': 123, '二叉树中的最大路径和': 124, '验证回文串': 125, '单词接龙II': 126, '单词接龙': 127, '最长连续序列': 128, '求根到叶子节点数字之和': 129, '被围绕的区域': 130, '分割回文串': 131, '分割回文串II': 132, '克隆图': 133, '加油站': 134, '分发糖果': 135, '只出现一次的数字': 136, '只出现一次的数字II': 137, '复制带随机指针的链表': 138, '单词拆分': 139, '单词拆分II': 140, '环形链表': 141, '环形链表II': 142, '重排链表': 143, '二叉树的前序遍历': 144, '二叉树的后序遍历': 145, 'LRU缓存机制': 146, '对链表进行插入排序': 147, '排序链表': 148, '直线上最多的点数': 149, '逆波兰表达式求值': 150, '翻转字符串里的单词': 151, '乘积最大子序列': 152, '寻找旋转排序数组中的最小值': 153, '寻找旋转排序数组中的最小值II': 154, '最小栈': 155, '上下翻转二叉树': 156, '用Read4读取N个字符': 157, '用Read4读取N个字符II': 158, '至多包含两个不同字符的最长子串': 159, '相交链表': 160, '相隔为1的编辑距离': 161, '寻找峰值': 162, '缺失的区间': 163, '最大间距': 164, '比较版本号': 165, '分数到小数': 166, '两数之和II-输入有序数组': 167, 'Excel表列名称': 168, '求众数': 169, '两数之和III-数据结构设计': 170, 'Excel表列序号': 171, '阶乘后的零': 172, '二叉搜索树迭代器': 173, '地下城游戏': 174, '组合两个表': 175, '第二高的薪水': 176, '第N高的薪水': 177, '分数排名': 178, '最大数': 179, '连续出现的数字': 180, '超过经理收入的员工': 181, '查找重复的电子邮箱': 182, '从不订购的客户': 183, '部门工资最高的员工': 184, '部门工资前三高的员工': 185, '翻转字符串里的单词II': 186, '重复的DNA序列': 187, '买卖股票的最佳时机IV': 188, '旋转数组': 189, '颠倒二进制位': 190, '位1的个数': 191, '统计词频': 192, '有效电话号码': 193, '转置文件': 194, '第十行': 195, '删除重复的电子邮箱': 196, '上升的温度':197, '打家劫舍': 198, '二叉树的右视图': 199, '岛屿数量': 200, '数字范围按位与': 201, '快乐数': 202, '移除链表元素': 203, '计数质数': 204, '同构字符串': 205, '反转链表': 206, '课程表': 207, '实现Trie(前缀树)': 208, '长度最小的子数组': 209, '课程表II': 210, '添加与搜索单词-数据结构设计': 211, '单词搜索II': 212, '打家劫舍II': 213, '最短回文串': 214, '数组中的第K个最大元素': 215, '组合总和III': 216, '存在重复元素': 217, '天际线问题': 218, '存在重复元素II': 219, '存在重复元素III': 220, '最大正方形': 221, '完全二叉树的节点个数': 222, '矩形面积': 223, '基本计算器': 224, '用队列实现栈': 225, '翻转二叉树': 226, '基本计算器II': 227, '汇总区间': 228, '求众数II': 229, '二叉搜索树中第K小的元素': 230, '2的幂': 231, '用栈实现队列': 232, '数字1的个数': 233, '回文链表': 234, '二叉搜索树的最近公共祖先': 235, '二叉树的最近公共祖先': 236, '删除链表中的节点': 237, '除自身以外数组的乘积': 238, '滑动窗口最大值': 239, '搜索二维矩阵II': 240, '为运算表达式设计优先级': 241, '有效的字母异位词': 242, '最短单词距离': 243, '最短单词距离II': 244, '最短单词距离III': 245, '中心对称数': 246, '中心对称数II': 247, '中心对称数III': 248, '移位字符串分组': 249, '统计同值子树': 250, '展开二维向量': 251, '会议室': 252, '会议室II': 253, '因子的组合': 254, '验证前序遍历序列二叉搜索树': 255, '粉刷房子': 256, '二叉树的所有路径': 257, '各位相加': 258, '较小的三数之和': 259, '只出现一次的数字III': 260, '以图判树': 261, '行程和用户': 262, '丑数': 263, '丑数II': 264, '粉刷房子II': 265, '回文排列': 266, '回文排列II': 267, '缺失数字': 268, '火星词典': 269, '最接近的二叉搜索树值': 270, '字符串的编码与解码': 271, '最接近的二叉搜索树值II': 272, '整数转换英文表示': 273, 'H指数': 274, 'H指数II': 275, '栅栏涂色': 276, '搜寻名人': 277, '第一个错误的版本': 278, '完全平方数': 279, '摆动排序': 280, '锯齿迭代器': 281, '给表达式添加运算符': 282, '移动零': 283, '顶端迭代器': 284, '二叉搜索树中的顺序后继': 285, '墙与门': 286, '寻找重复数': 287, '单词的唯一缩写': 288, '生命游戏': 289, '单词规律': 290, '单词规律II': 291, 'Nim游戏': 292, '翻转游戏': 293, '翻转游戏II': 294, '数据流的中位数': 295, '最佳的碰头地点': 296, '二叉树的序列化与反序列化': 297, '二叉树最长连续序列': 298, '猜数字游戏': 299, '最长上升子序列': 300, '删除无效的括号':301, '包含全部黑色像素的最小矩形': 302, '区域和检索-数组不可变': 303, '二维区域和检索-矩阵不可变': 304, '岛屿数量II': 305, '累加数': 306, '区域和检索-数组可修改': 307, '二维区域和检索-可变': 308, '最佳买卖股票时机含冷冻期': 309, '最小高度树': 310, '稀疏矩阵的乘法': 311, '戳气球': 312, '超级丑数': 313, '二叉树的垂直遍历': 314, '计算右侧小于当前元素的个数': 315, '去除重复字母': 316, '离建筑物最近的距离': 317, '最大单词长度乘积': 318, '灯泡开关': 319, '列举单词的全部缩写': 320, '拼接最大数': 321, '零钱兑换': 322, '无向图中连通分量的数目': 323, '摆动排序II': 324, '和等于k的最长子数组长度': 325, '3的幂': 326, '区间和的个数': 327, '奇偶链表': 328, '矩阵中的最长递增路径': 329,'按要求补齐数组': 330, '验证二叉树的前序序列化': 331, '重新安排行程': 332, '最大BST子树': 333, '递增的三元子序列': 334, '路径交叉': 335, '回文对': 336, '打家劫舍III': 337, '比特位计数': 338, '嵌套列表权重和': 339, '至多包含K个不同字符的最长子串': 340, '扁平化嵌套列表迭代器': 341, '4的幂': 342, '整数拆分': 343, '反转字符串': 344, '反转字符串中的元音字母': 345, '数据流中的移动平均值': 346, '前K个高频元素': 347, '判定井字棋胜负': 348, '两个数组的交集': 349, '两个数组的交集II': 350, '安卓系统手势解锁': 351, '将数据流变为多个不相交区间': 352, '贪吃蛇': 353, '俄罗斯套娃信封问题': 354, '设计推特': 355, '直线镜像': 356, '计算各个位数不同的数字个数': 357, 'K距离间隔重排字符串': 358, '日志速率限制器': 359, '有序转化数组': 360, '轰炸敌人': 361, '敲击计数器': 362, '矩形区域不超过K的最大数值和': 363, '加权嵌套序列和II': 364, '水壶问题': 365, '寻找完全二叉树的叶子节点': 366, '有效的完全平方数': 367, '最大整除子集': 368, '给单链表加一': 369, '区间加法': 370, '两整数之和': 371, '超级次方': 372, '查找和最小的K对数字': 373, '猜数字大小': 374, '猜数字大小II': 375, '摆动序列': 376, '组合总和Ⅳ': 377, '有序矩阵中第K小的元素': 378, '电话目录管理系统': 379, '常数时间插入、删除和获取随机元素': 380, 'O(1)时间插入、删除和获取随机元素-允许重复': 381, '链表随机节点': 382, '赎金信': 383, '打乱数组': 384, '迷你语法分析器': 385, '字典序排数': 386, '字符串中的第一个唯一字符': 387, '文件的最长绝对路径': 388, '找不同': 389, '消除游戏': 390, '完美矩形': 391, '判断子序列': 392, 'UTF-8编码验证': 393, '字符串解码': 394, '至少有K个重复字符的最长子串': 395, '旋转函数': 396, '整数替换': 397, '随机数索引': 398, '除法求值': 399, '第N个数字': 400, '二进制手表': 401, '移掉K位数字': 402, '青蛙过河': 403, '左叶子之和': 404, '数字转换为十六进制数': 405, '根据身高重建队列': 406, '接雨水II': 407, '有效单词缩写': 408, '最长回文串': 409, '分割数组的最大值': 410, '最短特异单词缩写': 411, 'FizzBuzz': 412, '等差数列划分': 413, '第三大的数': 414, '字符串相加': 415, '分割等和子集': 416, '太平洋大西洋水流问题': 417, '句子屏幕显示': 418, '甲板上的战舰': 419, '强密码检验器': 420, '数组中两个数的最大异或值': 421, '有效的单词方块': 422, '从英文中重建数字': 423, '替换后的最长重复字符': 424, '单词方块': 425, '将二叉搜索树转化为排序的双向链表': 426, '建立四叉树': 427, '序列化和反序列化N叉树': 428, 'N叉树的层序遍历': 429, '扁平化多级双向链表': 430, '将N叉树编码为二叉树': 431, '全O(1)的数据结构': 432, '最小基因变化': 433, '字符串中的单词数': 434, '无重叠区间': 435, '寻找右区间': 436, '路径总和III': 437, '找到字符串中所有字母异位词': 438, '三元表达式解析器': 439, '字典序的第K小数字': 440, '排列硬币': 441, '数组中重复的数据': 442, '压缩字符串': 443, '序列重建': 444, '两数相加II': 445,'等差数列划分II-子序列': 446, '回旋镖的数量': 447, '找到所有数组中消失的数字': 448, '序列化和反序列化二叉搜索树': 449, '删除二叉搜索树中的节点': 450, '根据字符出现频率排序': 451, '用最少数量的箭引爆气球': 452, '最小移动次数使数组元素相等': 453, '四数相加II': 454, '分发饼干': 455, '132模式': 456, '环形数组循环': 457, '可怜的小猪': 458, '重复的子字符串': 459, 'LFU缓存': 460, '汉明距离': 461, '最少移动次数使数组元素相等II': 462, '岛屿的周长': 463, '我能赢吗': 464, '最优账单平衡': 465, '统计重复个数': 466, '环绕字符串中唯一的子字符串': 467, '验证IP地址': 468, '凸多边形': 469, '用Rand7()实现Rand10()': 470, '编码最短长度的字符串': 471, '连接词': 472, '火柴拼正方形': 473, '一和零': 474, '供暖器': 475, '数字的补数': 476, '汉明距离总和': 477, '在圆内随机生成点': 478, '最大回文数乘积': 479, '滑动窗口中位数': 480, '神奇字符串': 481, '密钥格式化': 482, '最小好进制': 483, '寻找排列': 484, '最大连续1的个数': 485, '预测赢家': 486, '最大连续1的个数II': 487, '祖玛游戏': 488, '扫地机器人': 489, '迷宫': 490, '递增子序列': 491, '构造矩形': 492, '翻转对': 493, '目标和': 494, '提莫攻击': 495, '下一个更大元素I': 496, '非重叠矩形中的随机点': 497, '对角线遍历': 498, '迷宫III': 499, '键盘行': 500, '二叉搜索树中的众数': 501, 'IPO': 502, '下一个更大元素II': 503, '七进制数': 504, '迷宫II': 505, '相对名次': 506, '完美数': 507, '出现次数最多的子树元素和': 508, '斐波那契数': 509, '二叉搜索树中的中序后继II': 510, '找树左下角的值': 513, '自由之路': 514, '在每个树行中找最大值': 515, '最长回文子序列': 516, '超级洗衣机': 517, '零钱兑换II': 518, '随机翻转矩阵': 519, '检测大写字母': 520, '最长特殊序列Ⅰ': 521, '最长特殊序列II': 522, '连续的子数组和': 523, '通过删除字母匹配到字典里最长单词': 524, '连续数组': 525, '优美的排列': 526, '单词缩写': 527, '按权重随机选择': 528, '扫雷游戏': 529, '二叉搜索树的最小绝对差': 530, '孤独像素I': 531, '数组中的K-diff数对': 532, '孤独像素II': 533, 'TinyURL的加密与解密': 535, '从字符串生成二叉树':536,'复数乘法':537,'把二叉搜索树转换为累加树': 538, '最小时间差': 539, '有序数组中的单一元素': 540, '反转字符串II': 541, '01矩阵': 542, '二叉树的直径': 543, '输出比赛匹配对': 544, '二叉树的边界': 545, '移除盒子': 546, '朋友圈': 547, '将数组分割成和相等的子数组': 548, '二叉树中最长的连续序列': 549, '学生出勤记录I': 551, '学生出勤记录II': 552, '最优除法': 553, '砖墙': 554, '分割连接字符串': 555, '下一个更大元素III': 556, '反转字符串中的单词III': 557, '四叉树交集': 558, 'N叉树的最大深度': 559, '和为K的子数组': 560, '数组拆分I': 561, '矩阵中最长的连续1线段': 562, '二叉树的坡度': 563, '寻找最近的回文数': 564, '数组嵌套': 565, '重塑矩阵': 566, '字符串的排列': 567, '最大休假天数': 568, '员工薪水中位数': 569, '至少有5名直接下属的经理': 570, '给定数字的频率查询中位数': 571, '另一个树的子树': 572, '松鼠模拟': 573, '当选者': 574, '分糖果': 575, '出界的路径数': 576, '员工奖金': 577, '查询回答率最高的问题': 578, '查询员工的累计薪水': 579, '统计各专业学生人数': 580, '最短无序连续子数组': 581, '杀死进程': 582, '两个字符串的删除操作': 583, '寻找用户推荐人': 584, '2016年的投资': 585, '订单最多的客户': 586, '安装栅栏': 587, '设计内存文件系统': 588, 'N叉树的前序遍历': 589, 'N叉树的后序遍历': 590, '标签验证器': 591, '分数加减运算': 592, '有效的正方形': 593, '最长和谐子序列': 594, '大的国家': 595, '超过5名学生的课': 596, '好友申请I：总体通过率': 597, '范围求和II': 598, '两个列表的最小索引总和': 599, '不含连续1的非负整数': 600, '体育馆的人流量': 601, '好友申请II：谁有最多的好友': 602, '连续空余座位': 603, '迭代压缩字符串': 604, '种花问题': 605, '根据二叉树创建字符串': 606, '销售员': 607, '树节点': 608, '在系统中查找重复文件': 609, '判断三角形': 610, '有效三角形的个数': 611, '平面上的最近距离': 612, '直线上的最近距离': 613, '二级关注者': 614, '平均工资：部门与公司比较': 615, '给字符串添加加粗标签': 616, '合并二叉树': 617, '学生地理信息报告': 618, '只出现一次的最大数字': 619, '有趣的电影': 620, '任务调度器': 621, '设计循环队列': 622, '在二叉树中增加一行': 623, '数组列表中的最大距离': 624, '最小因式分解': 625, '换座位': 626, '交换工资': 627, '三个数的最大乘积': 628, 'K个逆序对数组': 629, '课程表III': 630, '设计Excel求和公式': 631, '最小区间': 632, '平方数之和': 633, '寻找数组的错位排列': 634, '设计日志存储系统': 635, '函数的独占时间': 636, '二叉树的层平均值': 637, '大礼包': 638, '解码方法2': 639, '求解方程': 640, '设计循环双端队列': 641, '设计搜索自动补全系统': 642, '子数组最大平均数I': 643, '最大平均子段和II': 644, '错误的集合': 645, '最长数对链': 646, '回文子串': 647, '单词替换': 648, 'Dota2参议院': 649, '只有两个键的键盘': 650, '4键键盘': 651, '寻找重复的子树': 652, '两数之和IV-输入BST': 653, '最大二叉树': 654, '输出二叉树': 655, '金币路径': 656, '机器人能否返回原点': 657, '找到K个最接近的元素': 658, '分割数组为连续子序列': 659, '移除9': 660, '图片平滑器': 661, '二叉树最大宽度': 662, '均匀树划分': 663, '奇怪的打印机': 664, '非递减数列': 665, '路径和IV': 666, '优美的排列II': 667, '乘法表中第k小的数': 668, '修剪二叉搜索树': 669, '最大交换': 670, '二叉树中第二小的节点': 671, '灯泡开关Ⅱ': 672, '最长递增子序列的个数': 673, '最长连续递增序列': 674, '为高尔夫比赛砍树': 675, '实现一个魔法字典': 676, '键值映射': 677, '有效的括号字符串': 678, '24点游戏': 679, '验证回文字符串Ⅱ': 680, '最近时刻': 681, '棒球比赛': 682, 'K个空花盆': 683, '冗余连接': 684, '冗余连接II': 685, '重复叠加字符串匹配': 686, '最长同值路径': 687, '“马”在棋盘上的概率': 688, '三个无重叠子数组的最大和': 689, '员工的重要性': 690, '贴纸拼词': 691, '前K个高频单词': 692, '交替位二进制数': 693, '不同岛屿的数量': 694, '岛屿的最大面积': 695, '计数二进制子串': 696, '数组的度': 697, '划分为k个相等的子集': 698, '掉落的方块': 699, '二叉搜索树中的搜索': 700, '二叉搜索树中的插入操作': 701, '搜索长度未知的有序数组': 702, '数据流中的第K大元素': 703, '二分查找': 704, '设计哈希集合': 705, '设计哈希映射': 706, '设计链表': 707, '循环有序列表的插入': 708, '转换成小写字母': 709, '黑名单中的随机数': 710, '不同岛屿的数量II': 711, '两个字符串的最小ASCII删除和': 712, '乘积小于K的子数组': 713, '买卖股票的最佳时机含手续费': 714, 'Range模块': 715, '最大栈':716, '1比特与2比特字符': 717, '最长重复子数组': 718, '找出第k小的距离对': 719, '词典中最长的单词': 720, '账户合并': 721, '删除注释': 722, '粉碎糖果': 723, '寻找数组的中心索引': 724, '分隔链表': 725, '原子的数量': 726, '最小窗口子序列': 727, '自除数': 728, '我的日程安排表I': 729, '统计不同回文子字符串': 730, '我的日程安排表II': 731, '我的日程安排表III': 732, '图像渲染': 733, '句子相似性': 734, '行星碰撞': 735, 'Lisp语法解析': 736, '句子相似性II': 737, '单调递增的数字': 738, '每日温度': 739, '删除与获得点数': 740, '摘樱桃': 741, '二叉树最近的叶节点': 742, '网络延迟时间': 743, '寻找比目标字母大的最小字母': 744, '前缀和后缀搜索': 745, '使用最小花费爬楼梯': 746, '至少是其他数字两倍的最大数': 747, '最短完整词': 748, '隔离病毒': 749, '角矩形的数量': 750, 'IP到CIDR': 751, '打开转盘锁': 752, '破解保险箱': 753, '到达终点数字': 754, '倒水': 755,'金字塔转换矩阵': 756, '设置交集大小至少为2': 757, '字符串中的加粗单词': 758, '员工空闲时间': 759, '找出变位映射': 760, '特殊的二进制序列': 761, '二进制表示中质数个计算置位': 762, '划分字母区间': 763, '最大加号标志': 764, '情侣牵手': 765, '托普利茨矩阵': 766, '重构字符串': 767, '最多能完成排序的块II': 768, '最多能完成排序的块': 769, '基本计算器IV': 770, '宝石与石头': 771, '基本计算器III': 772, '滑动谜题': 773, '最小化加油站的最大距离': 774, '全局倒置与局部倒置': 775, '拆分二叉搜索树': 776, '在LR字符串中交换相邻字符': 777, '水位上升的泳池中游泳': 778, '第K个语法符号': 779, '到达终点': 780, '森林中的兔子': 781, '变为棋盘': 782, '二叉搜索树结点最小距离': 783, '字母大小写全排列': 784, '判断二分图': 785, '第K个最小的素数分数': 786, 'K站中转内最便宜的航班': 787, '旋转数字': 788, '逃脱阻碍者': 789, '多米诺和托米诺平铺': 790, '自定义字符串排序':791, '匹配子序列的单词数': 792, '阶乘函数后K个零': 793, '有效的井字游戏': 794, '区间子数组个数': 795, '旋转字符串': 796, '所有可能的路径': 797, '得分最高的最小轮调': 798, '香槟塔': 799, '相似RGB颜色': 800, '使序列递增的最小交换次数': 801, '找到最终的安全状态': 802, '打砖块': 803, '唯一摩尔斯密码词': 804, '数组的均值分割': 805, '写字符串需要的行数': 806, '保持城市天际线': 807, '分汤': 808, '情感丰富的文字': 809, '黑板异或游戏': 810, '子域名访问计数': 811, '最大三角形面积': 812, '最大平均值和的分组': 813, '二叉树剪枝': 814, '公交路线': 815, '模糊坐标': 816, '链表组件': 817, '赛车': 818, '最常见的单词': 819, '单词的压缩编码': 820, '字符的最短距离': 821, '翻转卡片游戏': 822,'带因子的二叉树': 823, '山羊拉丁文': 824, '适龄的朋友': 825, '安排工作以达到最大收益': 826, '最大人工岛': 827, '独特字符串': 828, '连续整数求和': 829, '较大分组的位置': 830, '隐藏个人信息': 831, '翻转图像': 832, '字符串中的查找与替换': 833, '树中距离之和': 834, '图像重叠': 835, '矩形重叠': 836, '新21点': 837, '推多米诺': 838, '相似字符串组': 839, '矩阵中的幻方': 840, '钥匙和房间': 841, '将数组拆分成斐波那契序列': 842, '猜猜这个单词': 843, '比较含退格的字符串': 844, '数组中的最长山脉': 845, '一手顺子': 846, '访问所有节点的最短路径': 847, '字母移位': 848, '到最近的人的最大距离': 849, '矩形面积II': 850, '喧闹和富有': 851, '山脉数组的峰顶索引': 852, '车队': 853, '相似度为K的字符串': 854, '考场就座': 855, '括号的分数': 856, '雇佣K名工人的最低成本': 857, '镜面反射': 858, '亲密字符串': 859, '柠檬水找零': 860, '翻转矩阵后的得分': 861, '和至少为K的最短子数组': 862, '二叉树中所有距离为K的结点': 863, '获取所有钥匙的最短路径': 864, '具有所有最深结点的最小子树': 865, '回文素数': 866, '转置矩阵': 867, '二进制间距': 868, '重新排序得到2的幂': 869, '优势洗牌': 870, '最低加油次数': 871, '叶子相似的树': 872, '最长的斐波那契子序列的长度': 873, '模拟行走机器人': 874, '爱吃香蕉的珂珂': 875, '链表的中间结点': 876, '石子游戏': 877, '第N个神奇数字': 878, '盈利计划': 879, '索引处的解码字符串': 880, '救生艇': 881, '细分图中的可到达结点': 882, '三维形体投影面积': 883, '两句话中的不常见单词': 884, '螺旋矩阵III': 885, '可能的二分法': 886, '鸡蛋掉落': 887, '公平的糖果交换': 888, '根据前序和后序遍历构造二叉树': 889, '查找和替换模式': 890, '子序列宽度之和': 891, '三维形体的表面积': 892, '特殊等价字符串组': 893, '所有可能的满二叉树': 894, '最大频率栈': 895, '单调数列': 896, '递增顺序查找树': 897, '子数组按位或操作': 898, '有序队列': 899, 'RLE迭代器': 900, '股票价格跨度': 901, '最大为N的数字组合': 902, 'DI序列的有效排列': 903, '水果成篮': 904, '按奇偶排序数组': 905, '超级回文数': 906, '子数组的最小值之和': 907, '最小差值I': 908, '蛇梯棋': 909, '最小差值II': 910, '在线选举': 911, '排序数组': 912, '猫和老鼠': 913, '卡牌分组': 914, '分割数组': 915, '单词子集': 916, '仅仅反转字母': 917, '环形子数组的最大和': 918, '完全二叉树插入器': 919, '播放列表的数量': 920, '使括号有效的最少添加': 921, '按奇偶排序数组II':922, '三数之和的多种可能': 923, '尽量减少恶意软件的传播': 924, '长按键入': 925, '将字符串翻转到单调递增': 926, '三等分': 927, '尽量减少恶意软件的传播II': 928, '独特的电子邮件地址': 929, '和相同的二元子数组': 930, '下降路径最小和': 931, '漂亮数组': 932, '最近的请求次数': 933, '最短的桥': 934, '骑士拨号器': 935, '戳印序列': 936, '重新排列日志文件': 937, '二叉搜索树的范围和': 938, '最小面积矩形': 939, '不同的子序列II': 940, '有效的山脉数组': 941, '增减字符串匹配': 942, '最短超级串': 943, '删列造序': 944, '使数组唯一的最小增量': 945, '验证栈序列': 946, '移除最多的同行或同列石头': 947, '令牌放置': 948, '给定数字能组成的最大时间': 949, '按递增顺序显示卡牌': 950, '翻转等价二叉树': 951, '按公因数计算最大组件大小': 952, '验证外星语词典': 953, '二倍数对数组': 954, '删列造序II': 955, '最高的广告牌': 956, 'N天后的牢房': 957, '二叉树的完全性检验': 958, '由斜杠划分区域': 959, '删列造序III': 960, '重复N次的元素': 961, '最大宽度坡': 962, '最小面积矩形II': 963, '表示数字的最少运算符': 964, '单值二叉树': 965, '元音拼写检查器': 966, '连续差相同的数字': 967, '监控二叉树': 968, '煎饼排序': 969, '强整数': 970, '翻转二叉树以匹配先序遍历': 971, '相等的有理数': 972, '最接近原点的K个点': 973, '和可被K整除的子数组': 974, '奇偶跳': 975, '三角形的最大周长': 976, '有序数组的平方': 977, '最长湍流子数组': 978, '在二叉树中分配硬币': 979, '不同路径III': 980, '基于时间的键值存储': 981, '按位与为零的三元组': 982, '最低票价': 983, '不含AAA或BBB的字符串': 984, '查询后的偶数和': 985, '区间列表的交集': 986, '二叉树的垂序遍历': 987, '从叶结点开始的最小字符串': 988, '数组形式的整数加法': 989, '等式方程的可满足性': 990, '坏了的计算器': 991, 'K个不同整数的子数组': 992, '二叉树的堂兄弟节点': 993, '腐烂的橘子': 994, 'K连续位的最小翻转次数': 995, '正方形数组的数目': 996, '找到小镇的法官': 997, '最大二叉树II': 998, '车的可用捕获量': 999, '合并石头的最低成本': 1000, '网格照明': 1001, '查找常用字符': 1002, '检查替换后的词是否有效': 1003, '最大连续1的个数III': 1004, 'K次取反后最大化的数组和': 1005, '笨阶乘': 1006, '行相等的最少多米诺旋转': 1007, '先序遍历构造二叉树': 1008, '十进制整数的反码': 1009, '总持续时间可被60整除的歌曲': 1010, '在D天内送达包裹的能力': 1011, '至少有1位重复的数字': 1012, '将数组分成和相等的三个部分': 1013, '最佳观光组合': 1014, '可被K整除的最小整数': 1015, '子串能表示从1到N数字的二进制串': 1016, '负二进制转换': 1017, '可被5整除的二进制前缀': 1018, '链表中的下一个更大节点': 1019, '飞地的数量': 1020, '删除最外层的括号': 1021, '从根到叶的二进制数之和': 1022, '驼峰式匹配': 1023, '视频拼接': 1024, '除数博弈': 1025, '节点与其祖先之间的最大差值': 1026, '最长等差数列': 1027, '从先序遍历还原二叉树': 1028, '两地调度': 1029, '距离顺序排列矩阵单元格': 1030, '两个非重叠子数组的最大和': 1031, '字符流': 1032, '移动石子直到连续': 1033, '边框着色': 1034, '不相交的线': 1035, '逃离大迷宫': 1036, '有效的回旋镖': 1037, '从二叉搜索树到更大和树': 1038, '多边形三角剖分的最低得分': 1039, '移动石子直到连续II': 1040, '困于环中的机器人': 1041, '不邻接植花': 1042, '分隔数组以得到最大和': 1043, '最长重复子串': 1044, '买下所有产品的客户': 1045, '最后一块石头的重量': 1046, '删除字符串中的所有相邻重复项': 1047, '最长字符串链': 1048, '最后一块石头的重量II': 1049, '合作过至少三次的演员和导演':1050, '高度检查器': 1051, '爱生气的书店老板': 1052, '交换一次的先前排列': 1053, '距离相等的条形码': 1054, '形成字符串的最短路径': 1055, '易混淆数': 1056, '校园自行车分配': 1057, '最小化舍入误差以满足目标': 1058, '从始点到终点的所有路径': 1059, '有序数组中的缺失元素': 1060, '按字典序排列最小的等效字符串': 1061, '最长重复子串': 1062, '有效子数组的数目':1063, '不动点': 1064, '字符串的索引对': 1065, '校园自行车分配II': 1066, '范围内的数字计数': 1067, 'ProductSalesAnalysisI': 1068, 'ProductSalesAnalysisII': 1069, 'ProductSalesAnalysisIII': 1070, '字符串的最大公因子': 1071, '按列翻转得到最大值等行数': 1072, '负二进制数相加': 1073, '元素和为目标值的子矩阵数量': 1074, 'ProjectEmployeesI': 1075, 'ProjectEmployeesII': 1076, 'ProjectEmployeesIII': 1077, 'Bigram分词': 1078, '活字印刷': 1079, '根到叶路径上的不足节点': 1080, '不同字符的最小子序列': 1081, 'SalesAnalysisI': 1082, 'SalesAnalysisII': 1083, 'SalesAnalysisIII': 1084, '最小元素各数位之和': 1085, '前五科的均分': 1086, '字母切换': 1087, '易混淆数II': 1088, '复写零': 1089, '受标签影响的最大值': 1090, '二进制矩阵中的最短路径': 1091, '最短公共超序列': 1092, '大样本统计': 1093, '拼车': 1094, '山脉数组中查找目标值': 1095, '花括号展开II': 1096, 'GamePlayAnalysisV': 1097, 'UnpopularBooks': 1098, '小于K的两数之和': 1099, '长度为K的无重复字符子串': 1100, '彼此熟识的最早时间': 1101, '得分最高的路径': 1102, '分糖果II': 1103, '二叉树寻路': 1104, '填充书架': 1105, '解析布尔表达式': 1106, 'IP地址无效化': 1108, '航班预订统计': 1109, '删点成林': 1110, '有效括号的嵌套深度': 1111, '按序打印': 1114, '交替打印FooBar': 1115, '打印零与奇偶数': 1116, 'H2O生成': 1117, '一月有多少天': 1118, '删去字符串中的元音': 1119, '子树的最大平均值': 1120, '将数组分成几个递增序列': 1121, '数组的相对排序': 1122, '最深叶节点的最近公共祖先': 1123, '表现良好的最长时间段': 1124, '最小的必要团队': 1125, '等价多米诺骨牌对的数量': 1128, '颜色交替的最短路径': 1129, '叶值的最小代价生成树': 1130, '绝对值表达式的最大值': 1131, '最大唯一数': 1133, '阿姆斯特朗数': 1134, '最低成本联通所有城市': 1135, '平行课程': 1136, '第N个泰波那契数': 1137, '字母板上的路径': 1138, '最大的以1为边界的正方形':1139, '石子游戏II': 1140, '递减元素使数组呈锯齿状': 1144, '二叉树着色游戏': 1145, '快照数组': 1146, '段式回文': 1147}

    return mapping.get(string, 0) #返回0代表失败
# title = "会议室"
# # mapping = {"会议室":3, '不邻接植花': 1042}
# print (mapping['复数乘法']):
# print (mapping1["从字符串生成二叉树"])

# print ("你好")
# print ("你好" == "你好")
# for key, val in mapping.items():
#     print (key, mapping[key])
# # print len(mapping.items())
