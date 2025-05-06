
def generateasequesnce(start, end1, increaseby = 1):
        list1 = []
        while(start<end1):
                list1.append(start)
                start += increaseby

        return list1

print(generateasequesnce(0, 6, 3))
