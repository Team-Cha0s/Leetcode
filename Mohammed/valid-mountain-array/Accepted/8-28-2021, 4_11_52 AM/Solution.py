// https://leetcode.com/problems/valid-mountain-array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #Retrieving the highest number within the list
        highest = arr.index(max(arr))
        #making sure the lest is more than 3 numbers
        if len(arr) < 3:
            return False
        #Filtering the neighbours out
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
        #Making sure the last and the first number is not the highest
        print(len(arr) - 1)
        print(0)
        if highest == len(arr)-1 or highest == 0:
            return False
        #splitting the two in
        inc = arr[:highest]
        dec = arr[highest:]
        #if there is an increasing side and a decreasing side i just have to make sure both sides of the list are not             equal to the sorted version but for the decreased version i have to make sure that it doesnt equal it reversed             sorted cause its decreasing not increasing
        if inc != sorted(inc):
            return False
        if dec != sorted(dec, reverse=True):
            return False

        return True