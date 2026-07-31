class Solution(object):
    def finalValueAfterOperations(self, operations):
        ans = 0
        for operation in operations:
          if operation == "--X" or operation == "X--":
            ans -= 1
          if operation == "X++" or operation == "++X":
            ans += 1
          
        return ans