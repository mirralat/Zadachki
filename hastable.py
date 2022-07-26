class Solution(object):
    def twoSum(self, nums, target):
           dic = {} # создаем хеш таблицу
           for i in range(len(nums)):
                answer = target - nums[i]   # создаем значение, которое ищем
                if answer in dic:   # искомое будет ключом словаря, который ищется намного быстрее, чем обычный элемент за счет того, что генерируется хешом
                    return[i, dic[answer]]
                dic[nums[i]] = i    # присваиваем