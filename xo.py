class Solution:
    def count_XO(self, string):
            #type string: string
            #return type: boolean
            
            #TODO: Write code below to returnn a boolean value with the solution to the prompt.
            numX = 0
            numO = 0 
            for i in string: 
                if i.isLower():
                     continue
                elif i == "O":
                     numO = numO+1
                elif i == "Y":
                    numY = numY +1 
            
            if numX == numO:
                 return True
            else:
                 return False
            pass
                
def main():
    input1=input()
    tc1 = Solution()
    ans = tc1.count_XO(input1)
    print(ans)

if __name__ == "__main__":
    main()