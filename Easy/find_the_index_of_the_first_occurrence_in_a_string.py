def find_the_index_of_the_first_occurrence_in_a_string(haystack="leetcode", needle="leeto"):
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

output = find_the_index_of_the_first_occurrence_in_a_string()
print(output)

