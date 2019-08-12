# This is test version
# 7 elements stnad for 7 items of different price, choose two of them from these 7 items with 10 dollars
# Brute force
import subprocess

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
        print("Call Windows batch!")
        return subprocess.call("test.bat")