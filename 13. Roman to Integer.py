class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom_token = ['M','D','C','L','X','V','I']
        rom_match_num = [1000,500,100,50,10,5,1]
        rom_token_index = 0
        result = 0
        s_list = list(s)
        length = len(s_list)
        i = 0
        while i < length:
            if rom_token_index >= len(rom_token):
                break
            if s_list[i]==rom_token[rom_token_index]:
                result = result + rom_match_num[rom_token_index]
                i = i + 1
            else: 
                if rom_token_index + 1 < len(rom_token) and i + 1 < length:
                    if s_list[i] == rom_token[rom_token_index + 1] and s_list[i+1] == rom_token[rom_token_index]:
                        result = result + (rom_match_num[rom_token_index] - rom_match_num[rom_token_index + 1])
                        i = i + 2
                        continue
                
                if rom_token_index + 2 < len(rom_token) and i + 1 < length:
                    if s_list[i] == rom_token[rom_token_index + 2] and s_list[i+1] == rom_token[rom_token_index]:
                        result = result + (rom_match_num[rom_token_index] - rom_match_num[rom_token_index + 2])
                        i = i + 2
                        continue
                rom_token_index = rom_token_index + 1

        return result
        

print(Solution().romanToInt("MCMXCIV"))