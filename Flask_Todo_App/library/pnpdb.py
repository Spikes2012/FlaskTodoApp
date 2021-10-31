##CONNECT TO DATABASE##
import pymongo
from pymongo import MongoClient
import time

# initialize database


def initialize(emp_id, password):
    global client
    global db
    start = time.time()
    try:
        client = pymongo.MongoClient("mongodb+srv://%s:%s@pnp.6lidp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" %
                                     (emp_id, password), serverSelectionTimeoutMS=2000)
        db = client.pnpdb
        client.server_info()
        print("Successfully connected to database in",
              time.time() - start, "Seconds")
    except pymongo.errors.OperationFailure as e:
        print(e.code)
        print(e.details)
        # print("Connection error, Time elapsed", time.time() - start, "seconds")


##RETRIEVE DATA IN THE DATABASE##
##DATA FROM EMPLOYEES COLLECTION##
def find_data():
    col = db["Employees"]
    x = col.find()
    print("Data in Employees")
    # for data in x:
    # print(data)
    results = []
    for data in x:
        temp = {}
        temp["ID"] = data["Emp-ID"]
        temp["name"] = data["Emp_name"]
        results.append(temp)
    print(results)

    ##DATA FROM PROJECTS COLLECTION##
    col = db["Projects"]
    x = col.find()
    print("Data in Projects")
    results = []
    for data in x:
        temp = {}
        temp["ID"] = data["Project_ID"]
        temp["name"] = data["Project_name"]
        results.append(temp)
    print(results)
    return results

##DATA FROM TASKS COLLECTION##


def all_tasks():
    col = db["Tasks"]
    x = col.find()
    results = []
    for data in x:
        temp = {}
        temp["ID"] = data["Task_ID"]
        temp["name"] = data["Task_name"]
        temp["status"] = data["Task_Status"]
        # takes object id fo the entry in employees coolection
        y = data["Emp_assigned"]
        # takes object id for entry in projects collection
        z = data["Project_details"]
        temp["staff"] = db.Employees.find_one({"_id": y})["Emp_name"]
        # searching for entry using object id and storing it
        temp["Project Name"] = db.Projects.find_one({"_id": z})["Project_name"]
        temp['start_time'] = data["Start_time"]
        temp["end_time"] = data["Deadline"]
        temp["detail"] = data["Details"]
        results.append(temp)
    return results

##ADD DATA TO DATABASE##
##ADD DATA TO EMPLOYESS##


def add_data_emp(name, designation, department, role, number, password):
    col = db.Employees
    x = col.find().limit(1).sort([('$natural', -1)])
    for data in x:
        ID = data["Emp-ID"]
    emp_rec1 = {
        "Emp-ID": int(ID) + 1,
        "Emp_name": name,
        "Designation": designation,
        "Department": department,
        "User_role": role,
        "Contact_no": number,
        "Password": password

    }
    rec_id1 = col.insert_one(emp_rec1)
    print("Data inserted with record ids", rec_id1)


##RETRIEVE DATA FOR TASK LIST##
def emp_tasks(emp_id):
    y = db.Employees.find_one({"Emp-ID": emp_id})["_id"]
    col = db["Tasks"]
    results = []
    x = col.find({"Emp_assigned": y})
    for data in x:
        temp = {}
        temp["ID"] = data["Task_ID"]
        temp["name"] = data["Task_name"]
        temp["status"] = data["Task_Status"]
        # takes object id fo the entry in employees coolection
        y = data["Emp_assigned"]
        temp["staff"] = db.Employees.find_one({"_id": y})["Emp_name"]
        # takes object id for entry in projects collection
        z = data["Project_details"]
        # searching for entry using object id and storing it
        temp["Project Name"] = db.Projects.find_one({"_id": z})["Project_name"]
        temp['start_time'] = data["Start_time"]
        temp["end_time"] = data["Deadline"]
        temp['detail'] = data['Details']
        results.append(temp)
    return results


def to_do_list():
    col = db.Tasks
    results = []
    x = col.find({"Task_Status": "to-do"})
    for data in x:
        temp = {}
        temp['ID'] = data['Task_ID']
        temp["name"] = data["Task_name"]
        temp["status"] = data["Task_Status"]
        # takes object id fo the entry in employees coolection
        y = data["Emp_assigned"]
        temp["staff"] = db.Employees.find_one({"_id": y})["Emp_name"]
        # takes object id for entry in projects collection
        z = data["Project_details"]
        # searching for entry using object id and storing it
        temp["Project Name"] = db.Projects.find_one({"_id": z})["Project_name"]
        temp['start_time'] = data["Start_time"]
        temp["end_time"] = data["Deadline"]
        results.append(temp)
    return results


def home_page(emp_id):
    print("Home page details")
    col = db.Employees
    results = []
    x = col.find({"Emp-ID": emp_id})
    for data in x:
        temp = {}
        temp["Name"] = data["Emp_name"]
        temp["Designation"] = data["Designation"]
        temp["Role"] = data["User_role"]
        results.append(temp)
    print(results)

# EDIT DATA IN EMPLOYEES COLLECTION


def edit_employees(emp_id, emp_name=None, designation=None, role=None, number=None, department=None):
    col = db.Employees
    x = col.find({"Emp-ID": emp_id})
    for data in x:
        name = data["Emp_name"]
        position = data["Designation"]
        dept = data["Department"]
        roles = data["User_role"]
        Cno = data["Contact_no"]
    if emp_name == None:
        a = name
    else:
        a = emp_name
    if designation == None:
        b = position
    else:
        b = designation
    if role == None:
        c = roles
    else:
        c = role
    if number == None:
        d = Cno
    else:
        d = number
    if department == None:
        e = dept
    else:
        e = department

    result = col.update_many({"Emp-ID": emp_id},
                             {
        "$set": {"Emp_name": a,
                 "Designation": b,
                 "Department": e,
                 "User_role": c,
                 "Contact_no": d,
                 },
        "$currentDate": {"lastmodified": True}
    }
    )
    print("Data upadated with id", result)

# EDIT DATA IN projetsS COLLECTION


def edit_projects(project_id, project_name=None, client_name=None, deadline=None, project_status=None, supervisor=None):
    col = db.Projects
    x = col.find({"Project_ID": project_id})
    for data in x:
        name = data["Project_name"]
        client = data["Client_name"]
        dated = data["Deadline"]
        status = data["Project_status"]
        appointed = data["Supervisor"]
    if project_name == None:
        a = name
    else:
        a = project_name
    if client_name == None:
        b = client
    else:
        b = client_name
    if deadline == None:
        c = dated
    else:
        c = deadline
    if project_status == None:
        d = status
    else:
        d = project_status
    if supervisor == None:
        e = appointed
    else:
        e = db.Employees.find_one({"Emp_name": supervisor})["_id"]

    result = col.update_many({"Project_ID": project_id},
                             {
        "$set": {"Project_name": a,
                 "Client_name": b,
                 "Deadline": c,
                 "Project_status": d,
                 "Supervisor": e
                 },
        "$currentDate": {"lastmodified": True}
    }
    )
    print("Data upadated with id", result)

# edit data in tasks collection


def edit_tasks(task_id, project_details=None, task_name=None, emp_assigned=None, deadline=None, task_status=None, details=None, start_time=None):
    col = db.Tasks
    x = col.find({"Task_ID": task_id})
    for data in x:
        name = data["Task_name"]
        status = data["Task_Status"]
        dated = data["Deadline"]
        appointed = data["Emp_assigned"]
        project = data["Project_details"]
        dtls = data["Details"]
        start = data["Start_time"]
    if task_name == None:
        a = name
    else:
        a = task_name
    if task_status == None:
        b = status
    else:
        b = task_status
    if deadline == None:
        c = dated
    else:
        c = deadline
    if emp_assigned == None:
        d = appointed
    else:
        d = db.Employees.find_one({"Emp_name": emp_assigned})["_id"]
    if project_details == None:
        e = project
    else:
        e = db.Projects.find_one({"Project_name": project_details})["_id"]
    if details == None:
        f = dtls
    else:
        f = details
    if start_time == None:
        g = start
    else:
        g = start_time

    result = col.update_many({"Task_ID": task_id},
                             {
        "$set": {"Task_name": a,
                 "Emp_assigned": d,
                 "Deadline": c,
                 "Task_Status": b,
                 "Project_details": e,
                 "Start_time": g,
                 "Details": f
                 },
        "$currentDate": {"lastmodified": True}
    }
    )
    print("Data upadated with id", result)
