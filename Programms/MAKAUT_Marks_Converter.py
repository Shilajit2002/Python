# Find Total Marks , Obtained Marks & Percentage

odd_sgpa = float(input("Enter Odd Semester SGPA = "))
odd_sub = int(input("Enter Odd Semester Total Subject = "))
odd_percentage = (odd_sgpa-0.75)*10
odd_total_marks = odd_sub*100
odd_obtained_marks = odd_percentage*odd_sub

even_sgpa = float(input("Enter Even Semester SGPA = "))
even_sub = int(input("Enter Even Semester Total Subject = "))
even_percentage = (even_sgpa-0.75)*10
even_total_marks = even_sub*100
even_obtained_marks = even_percentage*even_sub

Total_Sub = odd_sub+even_sub
Total_Marks = odd_total_marks+even_total_marks
Total_Obtained_Marks = odd_obtained_marks+even_obtained_marks

Total_Percentage = Total_Obtained_Marks/Total_Sub

print("Total Marks is = ", Total_Marks)
print("Obtained Marks is = ", Total_Obtained_Marks)
print("Total Percentage is = ", Total_Percentage)