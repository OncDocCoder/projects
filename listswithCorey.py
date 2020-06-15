# courses = ['History', 'Math', 'Physics', 'Compsci']
# nums = [4, 3, 5, 2, 1]
# print(courses)
# sorted_courses = sorted(courses)
# print(sorted_courses)
# print(min(nums))
# print(max(nums))
# print(sum(nums))
# for index, course in enumerate(courses):
#     print(index, course)
# for index, course in enumerate(courses, start= 2):
#     print(index, course)
#
# course_str = ', '.join(courses)
# print (course_str)

# cs_courses = {'History', 'Math', 'Physics', 'Compsci' }
# print(cs_courses)
# art_courses = {'History', 'design', 'Physics', 'Art' }
# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))

#Sets can be combined using mathematical operators
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) #union first and second
print(first & second) #intersects first and second
print(first - second) #what is in first but not in second
print(second - first) #what is in second but not in first
print(first ^ second) #things unique to each set combined into one set

