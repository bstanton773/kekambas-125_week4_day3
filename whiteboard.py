# You are given a string s representing an attendance record for a student where each character
#  signifies whether the student was absent, late, or present on that day. The record only 
# contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.

# Example 1:
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

def solution(attendance):
    is_eligible = True
    day = 0
    num_absent = 0
    while day < len(attendance):
        if attendance[day] == 'A':
            num_absent += 1
            day += 1
        elif attendance[day] == 'L':
            days_late = 1
            day += 1
            while day < len(attendance) and attendance[day] == 'L':
                days_late += 1
                if days_late >= 3:
                    is_eligible = False
                day += 1
        else:
            day += 1
    if num_absent > 2:
        is_eligible = False
    return is_eligible

# def solution(attendance):
#     num_absent = 0
#     num_late = 0
#     for record in attendance:
#         if record == 'L':
#             num_late += 1
#             if num_late >= 3:
#                 return False
#         elif record == 'A':
#             num_absent += 1
#             num_late = 0
#         else:
#             num_late = 0
#     if num_absent > 2:
#         return False
#     return True