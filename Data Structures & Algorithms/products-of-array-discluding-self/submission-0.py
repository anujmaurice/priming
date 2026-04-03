class Solution:
    def generate_infix(self, nums: List[int]) -> List[int]:
        print(nums)
        out = [0]* len(nums)
        multipliyer = 1

        for i,v in enumerate(nums):
           #print(i,v,multipliyer)
           out[i] = multipliyer * v
           multipliyer = out[i]
        return out

    def generate_prefix(self, nums: List[int]) -> List[int]:
        #print(nums)
        out = [0]* len(nums)
        multipliyer = 1
        for i in range(len(nums)-1,-1,-1):
            # print(out,i)
            out[i] = nums[i]*multipliyer
            multipliyer = out[i]
        return out

        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        infx = self.generate_infix(nums)
        postfx = self.generate_prefix(nums)
        out = []
        # print(infx)
        # print(postfx)
        for i,v in enumerate(nums):
            if i==0:
                infx_left = 1
            else:
                infx_left = infx[i-1]
            if i == (len(nums)-1):
                postfx_right = 1
            else:
                postfx_right = postfx[i+1]
            print(i,infx_left,postfx_right)
            out.append(infx_left*postfx_right)
        
        # print(out)
        return out


