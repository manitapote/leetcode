class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        self.new = []
        for i in address:
            if i == '.':
                self.new.append('[')
                self.new.append('.')
                self.new.append(']')
            else:
                self.new.append(i)


        return ''.join(self.new)

#fastest of all
class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')

class Solution(object):
    def defangIPaddr(self, address):
        stri  = ''
        for i in address:
            if i == '.':
                stri+='[.]'
            else:
                stri+=i

        return stri


address = '1.1.1.1'
b = Solution()
print(b.defangIPaddr(address))