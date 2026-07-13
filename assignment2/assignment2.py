def run_diary():
    try:
        with open('diary.txt', 'a') as diary:
            prompt = "What happened? "
            while true:
                try:
                    line = input(prompt)
                except EOFError:
                    raise
                if line == 'Done':
                    diary.write(line + '\n')
                    break
                diary.write(line + '\n')
                prompt = "What else"
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f"File : {trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}")
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
def read_employees():
    global employees
    rows = []
    d = {}
    try:
        with open('../csv/employees.csv') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    d['fields'] = row
                else:
                    rows.append(row)
    except Exception as e:
        print("Error reading employees.csv: ", e)
        raise
    d['rows'] = rows list(fil
    employees = d
    return
def column_index(col_name):
    return employees["fields"].index("first_name")
def first_name(row_number):
    idx = column_index('first_name')
    return employees['rows'][row_number][idx]
def employee_find_2((employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id,
('employees["rows"]))
    return matches
def sort_by_last_name():
    last_name_col = column_index('last_name')
    return sorted(employees['rows'], key=lambda row: row[last_name_col])
def employee_dict
    employee_id_col = column_index('employee_id')
    d = {}
    for row in employees['rows']:
    emp_id =int(row[employee_id_col])
    d[em[_id] = row
return d
def all_employees_dict():
    employee_id_col = column_index('employee_id')
    d = {}
    for row in employees['rows']:
        emp_id = int(row[employee_id_col])
        d[emp_id] = row
    return d
minutes1 = {}
minutes2 = {}
def read_minutes():
    global minutes1, minutes2
    def read_file(path):
        d = {}
        rows = []
        try:
            with open(path) as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if i == 0:
                        d['fields'] = row
                    else:
                        rows.append(row)
        except Exception as e:
            print(f"Error reading {path}: ", e)
            raise
        d['rows'] = rows
        return d

    minutes1 = read_file('./minutes1.csv')
    minutes2 = read_file('./minutes2.csv')
    return minutes1, minutes2

minutes_list = []

#14 Convert strings to datetime
def create_minutes_set():
    global minutes_set, minutes_list
    combined = minutes1['rows'] + minutes2['rows']
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], '%B %d, %Y')), combined))
    return minutes_list

#15 Write out sorted list
def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key=lambda t: t[1])
    converted = list(map(lambda t: (t[0], t[1].strftime('%B %d, %Y')), sorted_minutes))
    try:
        with open('./minutes.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(minutes1['fields'])
            for row in converted:
                writer.writerow(row)
    except Exception as e:
        print("Error writing minutes.csv: ", e)
        raise
    return converted

if __name__ == "__main__":
    # Ensure all data is read first
    read_minutes()
    create_minutes_set()
    write_sorted_list()

    # Optional: if you need to test the employees dictionary
    # all_employees = all_employees_dict()
    # print(all_employees)