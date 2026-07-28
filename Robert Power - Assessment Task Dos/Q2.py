#the function that defines the code for checking how many empty seats are currently in the classroom.
def count_empty(classroom: list) -> int:
    count = 0 #sets the default amount of empty seats (0)
    for row in classroom: #looping through every row in the classroom.
        for i in row: #looping through each seat in the specific row being tested.
            if i == 0:
                count = count + 1 #if the seat has no student present, then the total amount of empty seats in the classroom moves up by one, and it moves on to the rest of the seats.
    print(count) #displays the amount of empty seats to the screen.
    return count

#the function that defines the code for checking which row has the most empty seats in the classroom so far.
def most_empty_row(classroom: list) -> int:
    best_row = 0 #Sets a default for the row with the most empty seats, being 0.
    best_count = -1 #Sets a default for the amount of empty seats within a row, being -1, because now if all rows have 0 empty seats, the order of rows will ensure that the first row always becomes the default.
    count = 0 #the temporary default count of the amount of empty seats within a row.
    for row_index in range(len(classroom)): #finds the amount of rows in the classroom, and then the amount of seats in each row, then loops through them all.
        count = classroom[row_index].count(0) #finds the amount of empty seats in the row that is currently being looped.
        if count > best_count: #checks whether this amount of seats is higher than the default (which the first must be, as the default is -1)
            best_count = count #if this is the case, then the amount of empty seats in that row now becomes the new highest amount of seats in any row.
            best_row = row_index #if this is the case, this row is labeled as the new row with the most empty seats.
    print(best_row) #displays the row with the most empty seats to the screen.
    return best_row


classroom=[[1,2,0], #the array (list of lists) containing the specific seat layout.
           [0,3,4],
           [5,0,0]]
count_empty(classroom)
most_empty_row(classroom)