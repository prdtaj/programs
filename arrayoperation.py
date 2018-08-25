array = a=[]
n=int(input('Enter the number of element in array:-'))
for i in range(n):
    e=input('Element:-')
    a.append(e)
print('Array Before any operation:-',a)
def main():
        print('for add element:-1,for delete an element:-2,for read array:-3,for exit:-4')
        
        c=input('Enter your choice :-')
        if c==1:
            add_element()

        elif c==2:
            delete_element()
        elif c==3:
            read()
        elif c==4:
            a_exit()
        else:
            print('------------:Please eneter invalid choice:------------')
        
    
def add_element():
        s=input('Please enter element for add in array')
        a.append(s)
        print('Array after adding a element',a)

def delete_element():
    d=0
    
    
    while d==0:
        print(a)
        b=input('Please enter the element for delete:-')
        try:
            a.remove(b)
            print('Deleting................')
            print('After deleting the element array is:-',a)
            d+=1
        except Exception as e:
            print('Please enter a number that is available in array')

def read():
    print('Array is :-',a)

def a_exit():
    exit()
while True:
    main()

