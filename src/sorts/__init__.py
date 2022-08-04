import random

class Sorts:
    # array to manipulate and print
    arr = [1, 2, 3, 4, 5]
    
    @classmethod
    def quickSort(cls, a):
        cls.arr = a
        l, r = 0, len(cls.arr)-1
    
        def quick(l, r):
            # find index of next partition while rearranging array
            def partition(l, r):
                # random pivot
                rand = random.randint(l, r)
                # swap random pivot
                cls.arr[r], cls.arr[rand] = cls.arr[rand], cls.arr[r]
                
                lo = l
                for i in range(l, r):
                    if cls.arr[i] <= cls.arr[r]:
                        cls.arr[i], cls.arr[lo] = cls.arr[lo], cls.arr[i]
                        lo += 1
                        
                cls.arr[lo], cls.arr[r] = cls.arr[r], cls.arr[lo]
                
                return lo
            
            if l < r:
                pi = partition(l, r)
                quick(l, pi-1)
                quick(pi+1, r)
        
        quick(l, r)
        
def main():
    arr = random.sample(range(0, 50), 25)
    Sorts.quickSort(arr)

if __name__ == '__main__':
    main()