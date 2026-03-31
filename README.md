
This is a simple command-line application built using Python to manage tasks and expenses. The project is intended for beginners to understand how to structure code using modules, work with files, and implement logging.

Features
Task Management
Add new tasks
Delete tasks
View all tasks

Expense Management
Add expenses under categories (food, travel, groceries)
Store amount and date
Data is saved locally using JSON files

Logging
Records user actions such as adding or deleting tasks
Captures errors and stores them in a log file
Project Structure
app/
│
├── main.py
├── storage.py
├── logger_config.py
├── task.json
├── expense.json
├── app.log
main.py handles the main program flow and user input
storage.py manages reading and writing data to JSON files
logger_config.py is used to configure logging
task.json and expense.json store application data
app.log stores logs generated during execution
Installation
Clone the repository:
git clone <your-repo-link>
cd app
(Optional) Create a virtual environment:
python -m venv .venv

Activate it:

Windows:

.venv\Scripts\activate

Mac/Linux:

source .venv/bin/activate
Running the Application
python main.py
How It Works
The application starts from main.py
Based on user input, it calls task or expense functions
Data is loaded from JSON files using storage.py
Any updates are saved back to the files
Logging records all actions and errors
Example Data
task.json
[
    {
        "id": 1,
        "name": "Study Python",
        "completed": false,
        "priority": "High",
        "due_date": "2026-03-31"
    }
]
expense.json
[
    {
        "category": "food",
        "amount": 200,
        "date": "2026-03-31"
    }
]
Concepts Used
Functions
JSON file handling
Exception handling
Logging
Modular programming


