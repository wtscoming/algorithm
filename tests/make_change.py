'''
用动态规划解硬币找零问题
共1分、5分、10分三种硬币, 输入金额change元, new_coin记录最新的硬币
'''

def make_change(change):
    # 最简单一枚硬币只有一种找零方式(0元不需要找零)
    min_coins = [0, 1]
    use_coins = [0, 1]
    for i in range(2, change + 1):
        coin_count = i
        new_coin = 1
        # 迭代更新最小硬币值: coin_count
        for j in [k for k in [1, 5, 10] if k <= i]:
            if min_coins[i - j] + 1 < coin_count:
                coin_count = min_coins[i - j] + 1
                new_coin = j
        min_coins.append(coin_count)
        use_coins.append(new_coin)
    
    # 回溯打印所使用的硬币
    while use_coins[change] > 0:
        print(use_coins[change])
        change -= use_coins[change]
