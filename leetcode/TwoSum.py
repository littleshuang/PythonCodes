# coding: utf-8
class Solution(object):

    def add_2_map(self, num_map, cur, k, i, time=0):
        if k+i not in cur:
            d_map = {}
        else:
            d_map = cur[k+i].copy()
        if num_map is None:
            if time in d_map:
                d_map[time] = d_map[time] + 1
            else:
                d_map[time] = 1
        else:
            k_map = num_map[k]
            for k, v in k_map.items():
                if k+1 in d_map:
                    d_map[k+1] = d_map[k+1] + v
                else:
                    d_map[k+1] = v
        return d_map

    def clear(self, cur, time):
        ret = {}
        for k, v in cur.items():
            ret[k] = {}
            for x, y in v.items():
                if x != time:
                    continue
                ret[k][x] = y
        return ret

    def twoSum(self, n):
        if n <= 0:
            return []
        # 数字： 加和个数： 有几次这样的加和
        num_map = {1: {1: 1}, 2: {1: 1}, 3: {1: 1}, 4: {1: 1}, 5: {1: 1}, 6: {1: 1}}
        base = [1, 2, 3, 4, 5, 6]
        total = 6
        ret = []
        for time in range(n-1):# 4： 0 1 2
            cur = num_map.copy()
            for i in base:
                for k, v in num_map.items():
                    if k in num_map:
                        ret_map = self.add_2_map(num_map, cur, k, i)
                        cur[k+i] = ret_map

                    else:
                        ret_map = self.add_2_map(None, cur, k, i, time+2)
                        cur[k+i] = ret_map

            num_map = self.clear(cur, time+2)
            print(num_map)
        print(num_map)
        total = 0
        num = []
        for k, v in num_map.items():
            if n in v:
                count = v[n]
                total = total + count
                num.append(count)
        ret = []
        for i in num:
            ret.append(float(format(i/float(total), '.5f')))
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(3))
