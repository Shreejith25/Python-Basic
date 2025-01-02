#Python program to print all Prime numbers in an Interval

start = int(input('Enter start number: '))
end = int(input('Enter end number: '))

is_prime = True
for i in range(start,end+1):
    if i < 2:
        continue
    else:
        for j in range(2,int(i**0.5)+1):
            
            if(i%j== 0):
                is_prime =False
                break


        if is_prime :
            
            print(f'{i} prime')
            




