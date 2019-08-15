# This is test version
# 7 elements stnad for 7 items of different price, choose two of them from these 7 items with 10 dollars
# Brute force
import subprocess
#from subprocess import Popen

class Solution():
    def TwoSumBrute(self, price_list, target_price):
        print("price_list = ", price_list, ", target_price = ", target_price)
        for anchor_count in range(len(price_list)):
            for shift_count in range(anchor_count+1, len(price_list),1):
                if price_list[anchor_count] + price_list[shift_count] == 10:
                    return [anchor_count, shift_count]
    
    def TwoSumImprove(self, price_list, target_price):
        print("price_list = ", price_list, ", target_price = ", target_price)
        complement_list = {}
        for anchor_count in range(len(price_list)):
            if (target_price - price_list[anchor_count]) not in (complement_list):
                complement_list[price_list[anchor_count]] = anchor_count
            else:
                return [complement_list[target_price - price_list[anchor_count]], anchor_count]
            
    def CallWindowsBat(self):
        print("Call test.bat")
        #subprocess.call(["echo", "not my fault"], shell = True)
        #subprocess.run(["echo", "good luck!"], shell = True)
        #Popen(['dir', '/p'])
        return subprocess.call("test.bat")

    def CallWindowsBat1(self):
        print("Call LastBootUpTime.bat")
        return subprocess.call(["LastBootUpTime.bat","0"])

    ''' Given a 32-bit signed integer, reverse digits of an integer '''
    def reverse(self, x):
        #print("type of x = ", type(x))
        y = str(x)
        z = str("")
        for digit_count in range(len(y)):
            #print("y[", digit_count,"] = ", y[digit_count])
            z = y[digit_count] + z
            #print("z = ", z)
        if z[-1] == "-":
            z = '-' + z[:len(z)-1]
        #print("type of z = ", type(z))
        #print("z = ", z)
        x = int(z)
        #print("resulting x = ", x)
        #print(2**31-1)
        if (x > (2**31-1)) or (x < (-2**31)):
            return 0
        return x
