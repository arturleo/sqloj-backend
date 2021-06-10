# SQLOJ-BACKEND Dev Documentation

## Database

### mongodb.document
#### users
    {
        "username": "admin",
        "password": # salted password,
        "role": # "teacher" or "student"
    }
#### assignments

    {
        "assignment_id": "a-066ab87a062b",
        "assignment_name": "第一次作业",
        "assignment_start_time": # datetime.datetime,
        "assignment_end_time": # datetime.datetime
    }
#### questions

    {
        "question_id": "q-21ru2933hui4",
        "question_name": "7-1 select查询",
        "assignment_id": "a-066ab87a062b",
        "question_description": "22222",
        "question_output": "3333333333",
        "question_answer": "select * from albums;",
        "question_standard_output": [],
        "question_type": # "sql" or "text",
        'db_id': "db-21ru2933hui4"
    }

#### records
    {
        "record_id": "r-21ru2923hui4",
        "question_id": "q-21ru2933hui4",
        "question_type": # "sql" or "text",
        "assignment_id": "a-066ab87a062b",
        "username": "admin",
        "submit_time": # datetime.datetime,
        "finished_time": # datetime.datetime,
        "record_code": "code1",
        "record_status": # "AC", "WA", "TLE", "RE"
        "running_time": 100,
        "record_lack": 0,
        "record_err": 0,
    }
    
#### record_outputs
    {
        "question_id": "q-21ru2933hui4",
        "username": "123",
        "output": "lalalala",
        "record_id": "r-21ru2943hui4",
        "submit_time": # datetime.datetime,
        "finished_time": # datetime.datetime,
    }

#### dbs
    {
        "db_id": "db-r9imvrvnq40s",
        "db_name": "q2",
        "db_description": "123",
        "db_filename": "r9imvrvnq40s", 
        # database path will be ./database/filename, which is db_id[3:]
        "upload_time": # datetime.datetime,
    }

## File structure

    sqloj_backend
    │  login.py         # namespace router
    │  model.py         # req/res model
    │  student.py       # namespace router
    │  task.py          # task functions to be completed in queue 
    │  teacher.py       # namespace router
    │  util.py          
    │  __init__.py      # flask app initialization   
    ├─database          # database file storage
    ├─extension
    │  └─__init__.py    # initialize extensions for routers to import  
    └─module                
       └─judge.py       # problem judger function

  