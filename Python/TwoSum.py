class Solution:
    def twoSum(self, nums, target):

        ####### Define an hash table given the nums list
        ArrayDict = {}
        for i in range(len(nums)):
            if nums[i] in ArrayDict.keys():
                ArrayDict.update({nums[i]:[ArrayDict[nums[i]],i]})
            else:
                ArrayDict.update({nums[i]:i})
        #######

        Output = []
        # Iterate over the keys
        for element in ArrayDict.keys():

            # Find the complement value
            ElementToSearch = target - element

            # If the complement exists within the keys
            if (ElementToSearch in ArrayDict.keys()):
                
                if element == ElementToSearch:
                    if type(ArrayDict[ElementToSearch]) != int:
                        Output = [ArrayDict[ElementToSearch][0],ArrayDict[ElementToSearch][1]]
                        print('The element in nums whose index is: ' + str(Output) + ' sum up to ' + str(target))
                        return Output
                    else:
                        continue
                else:
                    Output = [ArrayDict[element],ArrayDict[ElementToSearch]]
                    print('The element in nums whose index is: ' + str(Output) + ' sum up to ' + str(target))
                    return Output
     
        print('No solution possible')



if __name__ == '__main__':
    
    # Define input
    nums = [3,3]
    target = 6
    
    # Execute code
    SolutionObject = Solution()
    SolutionObject.twoSum(nums,target)
    