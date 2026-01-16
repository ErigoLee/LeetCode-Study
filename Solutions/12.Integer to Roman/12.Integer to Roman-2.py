class Solution(object):
    def AddRom(self,token_list, unit):
        make_rom = ""
        if unit >= 5:
            if unit == 9:
                make_rom = token_list[0]+token_list[2]
            else:
                make_rom = token_list[1]+token_list[0]*(unit-5)
        else:
            if unit == 4:
                make_rom = token_list[0]+token_list[1]
            else:
                make_rom = token_list[0]*(unit)
        return make_rom


    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        index = 0
        token_list = [['I','V','X'],['X','L','C'],['C','D','M']]
        while True:
            unit = num % 10
            num = num // 10
            if index == 0:
                result = self.AddRom(token_list[0],unit)+result
            elif index == 1:
                result = self.AddRom(token_list[1],unit)+result
            elif index == 2:
                result = self.AddRom(token_list[2],unit)+result
            elif index == 3:
                result = 'M'*unit+result
            index = index + 1
            if (num == 0):
                break
        return result        
print(Solution().intToRoman(1994))