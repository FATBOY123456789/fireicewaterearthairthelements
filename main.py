class pair_elements:
    def twosum(self,num,target):
        Lookup={}
        for c,d in enumerate(num):
            if target-d in Lookup:
                return (Lookup[target-d],c)
            Lookup[d]=c
n=int(input('Enter a number: '))
print("index1=%d , index2=%d" %pair_elements().twosum((10,20,30,40,50,60,70),n))