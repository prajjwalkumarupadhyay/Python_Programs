def main():
    def convert(List):
        String=', '.join(List)
        return String
    list1=[]
    print('Enter items in list or type (d)one to exit')
    while True:
        items=input()
        if items.lower()=='d':
            break
        list1.append(items)
    print(convert(list1)+'& '+list1[len(list1)])
main()