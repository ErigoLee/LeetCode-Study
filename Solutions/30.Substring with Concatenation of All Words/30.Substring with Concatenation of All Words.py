class Solution(object):
    
    def count_word(self, word, s):
        word_length = len(word)
        s_length =  len(s)
        result =[]
        for i in range(0, s_length-word_length):
            if s[i:i+word_length] == word:
                result.append(i)
        return result
    
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_index = {}
        for word in words:
            word_index = []
            word_index = self.count_word(word, s)
            words_index[word] = word_index
            print(word_index)
        
        result = []
        words_length = len(words)
        for value in words_index[words[0]]:
            flag = False
            temp = value
            for i in range(1, words_length):
                if temp + len(words[i-1]) not in words_index[words[i]]:
                    break
                if i == words_length -1:
                    flag = True
                temp = temp + len(words[i-1])
                
            if flag == True:
                print(value)
                result.append(value)
        
        for value in words_index[words[words_length-1]]:
            flag = False
            temp = value
            print(value)
            for i in range(words_length-2,0,-1):
                if temp + len(words[i+1]) not in words_index[words[i]]:
                    flag = False
                    break
                if i == 0:
                    print("temp")
                    flag = True
                temp = temp + len(words[i+1])            
            if flag == False:
                result.append(value)
        
        result.sort()
        return result

print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))