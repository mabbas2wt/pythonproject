# ----------------------------------------------------------------
# Author:
# Date:
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
import datetime


def display_bill(s_id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function displays the student's bill. It takes four
    # parameters: s_id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # The function has no return value.
    # ------------------------------------------------------------
   in_state = s_in_state.get(s_id, False)

    # Set the tuition cost based on the student's residency
    if in_state:
        tuition_per_hour = 225  # In-state tuition cost per credit hour
    else:
        tuition_per_hour = 850  # Out-of-state tuition cost per credit hour

    # Get the student's course roster
    student_courses = c_rosters.get(s_id, [])

    # Display the tuition bill header
    print("\nTuition Summary")
    print(f"Student: {s_id}, {'In-State' if in_state else 'Out-of-State'}")

    # Display the current date and time using the datetime library
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%b %d, %Y at %I:%M %p"))

    # Display the table header
    print("{:<10} {:<8} {:<13}".format("Course", "Hours", "Cost"))
    print("{:<10} {:<8} {:<13}".format("------", "-----", "---------"))

    total_hours = 0
    total_cost = 0

    # Display the details for each course the student is enrolled in
    for course in student_courses:
        hours = c_hours.get(course, 0)
        cost = hours * tuition_per_hour
        total_hours += hours
        total_cost += cost

        print("{:<10} {:<8} ${:,.2f}".format(course, hours, cost))

    # Display the total row
    print("{:<10} {:<8} ${:,.2f}".format("Total", total_hours, total_cost))


# Test the function
# Provide sample data for testing
sample_student_id = '1001'
sample_in_state = {'1001': True, '1002': False}
sample_course_rosters = {'1001': ['CSC101', 'CSC102'], '1002': ['CSC103', 'CSC105']}
sample_course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC105': 2}

# Call the function with the sample data
display_bill(sample_student_id, sample_in_state, sample_course_rosters, sample_course_hours)

