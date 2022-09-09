class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]):
        properties.sort(reverse=True)
        set_prop = {}
        for attack,defend in properties:
            if attack not in set_prop:
                set_prop[attack] = [defend]
            else:
                set_prop[attack].append(defend)
        max_def = -1
        result = 0
        for attack in set_prop:
            max_def_temp = max_def
            for defend in set_prop[attack]:
                if defend < max_def:
                    result += 1
                max_def_temp = max(max_def_temp,defend)
            max_def = max_def_temp
        return result