from typing import List, Optional
class DailyTemperatures:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        # stack = []
        # res = []
        # for temp in temperatures: 
        #     count = 0 
        #     if stack and stack[-1] > temp:
        #         count +=1 
        #         stack.pop()
        #     else:
        #         stack.append(temp)
        #     if count>=1:
        #         res.append(count)
        # return res 
        res = [0]* len(temperatures)
        #Stack has 2 values 
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t , stack_i = stack.pop()
                res[stack_i] = (i - stack_i)
            stack.append([t,i])
        
        return res 

if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    obj = DailyTemperatures()
    print(obj.daily_temperatures(temperatures))