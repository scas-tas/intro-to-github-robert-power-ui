def combine_trucks(trucks, first_truck, second_truck):
    return(int(trucks[first_truck-1] + trucks[second_truck-1]))
    #returns the total packages in first_truck and second_truck
    pass


def main():
    #lists the number of trucks
    trucks = [4, 7, 2, 6, 9]
    #prints the combined number of packages within the two trucks chosen
    print(combine_trucks(trucks, 4, 3))  # Expected: 13
    print(combine_trucks(trucks, 3, 5))  # Expected: 6


main()