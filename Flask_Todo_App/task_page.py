from flask import Blueprint, Flask, render_template, redirect, url_for, request
import library.pnpdb as pnpdb

tasks = Blueprint(__name__, "tasks")

my_tasks = [{'ID': '0001', 'name': 'Task1', 'status': 'in progress', 'staff': 'Naveen', 'start_time': '2021-10-1', 'end_time': '2021-11-1', 'detail': 'This is task1.'},
            {'ID': '0002', 'name': 'Task2', 'status': 'in progress', 'staff': 'Naveen', 'start_time': '2021-10-10', 'end_time': '2021-11-10', 'detail': 'This is task2.'},
            {'ID': '0004', 'name': 'Task4', 'status': 'finished', 'staff': 'Naveen', 'start_time': '2021-9-1', 'end_time': '2021-10-1', 'detail': 'This is task4.'}]


@tasks.route("/task_page")
def task_page():
    pnpdb.initialize("0001", "admin")
    all_tasks = pnpdb.all_tasks()
    to_do_tasks = pnpdb.to_do_list()
    return render_template("task_page.html", all_tasks=all_tasks, my_tasks=my_tasks, to_do_tasks=to_do_tasks)




@tasks.route("/task_page/modify_name/<id>", methods=["POST"])
def modify_name(id):
    data = request.form.get('modify_name')
    pnpdb.edit_tasks(task_id=id, task_name=data)
    return redirect(url_for('task_page.task_page'))


@tasks.route("/task_page/modify_status/<id>", methods=["POST"])
def modify_status(id):
    data = request.form.get('modify_status')
    pnpdb.edit_tasks(task_id=id, task_status=data)
    return redirect(url_for('task_page.task_page'))


@tasks.route("/task_page/modify_staff/<id>", methods=["POST"])
def modify_staff(id):
    data = request.form.get('modify_staff')
    pnpdb.edit_tasks(task_id=id, emp_assigned=data)
    return redirect(url_for('task_page.task_page'))


@tasks.route("/task_page/modify_start_time/<id>", methods=["POST"])
def modify_start_time(id):
    data = request.form.get('modify_start_time')
    pnpdb.edit_tasks(task_id=id, start_time=data)
    return redirect(url_for('task_page.task_page'))


@tasks.route("/task_page/modify_end_time/<id>", methods=["POST"])
def modify_end_time(id):
    data = request.form.get('modify_end_time')
    pnpdb.edit_tasks(task_id=id, deadline=data)
    return redirect(url_for('task_page.task_page'))

@tasks.route("/task_page/modify_details/<id>", methods=["POST"])
def modify_details(id):
    data = request.form.get('modify_details')
    pnpdb.edit_tasks(task_id=id, details=data)
    return redirect(url_for('task_page.task_page'))
