class Solution(object):
   def validIPAddress(self, IP):
      """
      :type IP: str
      :rtype: str
      """
      def isIPv4(s):
         try: return str(int(s)) == s and 0 <= int(s) <= 255
         except: return False
      if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
         return "IPv4"
ob = Solution()
print(ob.validIPAddress("172.16.254.1"))
#edit this so that it can take 10 inputs
