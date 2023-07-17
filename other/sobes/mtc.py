# ["t1", "t2", "t3", ... "tN"]

# student_id | subject
# 1          | Math
# 1          | English
# 2
# 3
# 4


# select * from t1
# left join (select * from t2) as t2 ON t1.student_id = t2.student_id
# left join (select * from t3) as t3 ON t2.student_id = t3.student_id

tables = ["t1", "t2", "t3", "t5"]

def create_request(tables):
    line = 'select * from ' + str(tables[0])
    for i in range(1, len(tables)):
       line +=  f'\nleft join (select * from {tables[i]}) as {tables[i]} ON {tables[i-1]}.student_id = {tables[i]}.student_id '
    return line

print(create_request(tables))
