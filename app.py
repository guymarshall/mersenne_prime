# make list to check
    # square the previous number then subtract 2
        # 4, 14 etc

# do 2^n - 1
# if the (n-1)th element of the list is a multiple of the answer, then PRIME else NOT PRIME
# 2 -> 14, is it a multiple of 2^3 - 1 (7), if it is then PRIME else NOT PRIME
# to get element of list, remember to take one away, so 14 is the 2nd number, but the 1st element of the list

def generate_list(count):
    multiples = [4]

    for _ in range(count - 1):
        multiples.append((multiples[-1] ** 2) - 2)
    
    return multiples

def main():
    number = int(input("Enter number of elements in list: "))
    multiples = generate_list(number)
    print(multiples)

if __name__ == "__main__":
    main()
