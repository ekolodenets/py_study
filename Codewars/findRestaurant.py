'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants
represented by strings.
You need to help them find out their common interest with the least list index sum. If there is a choice tie between
answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Constraints:
1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30
list1[i] and list2[i] consist of spaces ' ' and English letters.
All the stings of list1 are unique.
All the stings of list2 are unique

class Solution:
    def findRestaurant(self, list1: 'List[str]', list2: 'List[str]') -> 'List[str]':
        pass
'''


class Solution:
    def findRestaurant(self, list1: 'List[str]', list2: 'List[str]') -> 'List[str]':
        x = []
        small, big = list1, list2 if len(list1) < len(list2) else list2
        for small_i, small_item in enumerate(small):
            for big_i, big_item in enumerate(big):
                if small_item == big_item:
                    x.append(small_item)
        if len(x) == 1:
            return x
        else:
            temp = {}
            for i in x:
                if not temp:
                    temp[i] = small.index(i)+big.index(i)
                else:
                    temp[i] = small.index(i)+big.index(i)
            minval = min(temp.values())
            res = [k for k, v in temp.items() if v == minval]
            return res[::-1]


assert Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]) == ["Shogun"]
assert Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]) == ["Shogun"]
assert Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Burger King", "Tapioca Express", "Shogun"]) == ["KFC", "Burger King", "Tapioca Express", "Shogun"]
