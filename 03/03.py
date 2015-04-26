Python 3.5.0a3 (v3.5.0a3:82656e28b5e5, Mar 30 2015, 00:12:00) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def BinSearch(list,value):
    begin = 0
    if list[0] == value:
        return 0

    end = len(list)-1
    while(begin < end):
        mid = begin + (end - begin)//2
        if list[mid]>value:
            end = mid - 1
        elif list[mid] <value:
            begin = mid + 1
        else:
            return mid

    if(begin == end):
        if(value == list[begin]):
            return begin
        else:
            return -1

        
>>> list = ['a','b','c','d','e','f','g','h','i']
>>> value = 'f'
>>> aa = BinSearch(list,value)
>>> aa
5
>>> 
