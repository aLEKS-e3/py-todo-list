# Python Just To-Do List

This is a simple Python3 project to help you manage tasks throughout a day or week!

## What can it help with?

- **Create Tasks**: Easily add tasks with optional deadline!
- **Update Tasks**: Something changed? No problem, just update your task!
- **Complete Tasks**: Mark already done tasks as complete (You can even undo them!)
- **Delete Tasks**: Delete all finished tasks in the end of the day!

## How to use?

We need Python3 to be installed on your desktop...

```bash
git clone https://github.com/aLEKS-e3/py-todo-list.git
# open the project in your IDE
python -m venv venv
source venv/bin/activate  # for Windows: venv\scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```
