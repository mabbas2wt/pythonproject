# ----------------------------------------------------------------
# Author:
# Date:
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------
from student import list_courses, add_course, drop_course
from billing import display_bill


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, in_state_list, course
    # list, max class size list and roster list.  It uses a loop to
    # serve multiple students. Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444'),
                    ('1005', '555'), ('1006', '666')]
    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False,
                        '1005': False,
                        '1006': True}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5,
                    'CSC104': 3, 'CSC105': 2}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': [],
                     'CSC105': ['1005', '1002']}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1,
                       'CSC104': 3, 'CSC105': 4}

    student_id = input('enter student id: ')
    login(student_id, student_list)
    show_menu()
        while True:
        action = input('what do you want to do: ')
        if action == '1':
            add_course(student_id, course_roster, course_max_size)
        if action == '2':
            drop_course(student_id, course_roster)
        if action == '3':
            list_courses(student_id, course_roster)
        if action == '4':
            display_bill(student_id, student_in_state, course_roster, course_hours)
        if action == '0':
            break


def login(s_id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: s_id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------

    student_dict = dict(s_list)
    print(student_dict)
    pin = input('enter your pin: ')
    if s_id in student_dict:
        if pin == student_dict[s_id]:
            print('Verified')
            return True
        else:
            print('could not verify student')
            return False
    else:
        print("Student doesn't exist")
        return False


def show_menu():
    # ------------------------------------------------------------
    # This function displays the action menu to the logged in student.
    # It takes no parameters and returns no values.
    # -------------------------------------------------------------
    print('Action Menu')
    print('-------------')
    print('1:Add course')
    print('2:drop courses')
    print('3:list courses')
    print('4:show bill')
    print('0:logout')



main()
