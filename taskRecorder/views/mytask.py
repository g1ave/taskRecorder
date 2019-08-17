from flask import Blueprint, render_template, redirect, url_for, flash, g
from taskRecorder.models import TimeSheet, db, Project, Task
from flask_login import login_required, current_user
from taskRecorder.forms import ProjectForm, TaskFrom, TimeSheetForm
from pyecharts.charts import Bar, Page, Pie

import datetime

task = Blueprint('task', __name__, template_folder='../templates', url_prefix='/')


@login_required
@task.route('/mytask', methods=['post', 'get'])
def show_task():
    project_form = ProjectForm()
    projects = Project.query.all()
    if project_form.is_submitted():
        if project_form.validate():
            new_project = Project(
                project_name=project_form.project_name.data,
                start_date=project_form.start_date.data,
                expected_end_date=project_form.expected_end_date.data,
                project_description=project_form.project_description.data,
                user_id=current_user.user_id
            )
            db.session.add(new_project)
            db.session.commit()
            return redirect('/mytask')
        else:
            flash("Failed. Wrong form data.")
    return render_template('taskList.html', projects=projects, project_form=project_form)


@login_required
@task.route('/project_detail/<project_id>', methods=['post', 'get'])
def view_project_detail(project_id):
    if project_id is None:
        return redirect('/mytask')
    else:
        task_form = TaskFrom()
        project = Project.query.filter_by(project_id=project_id).first()
        tasks = Task.query.filter_by(project_id=project_id).all()
        if not project:
            return "Bad request"
        if task_form.is_submitted():
            if task_form.validate():
                new_task = Task(start_date=task_form.start_date.data,
                                end_date=task_form.end_date.data,
                                project_id=project_id,
                                description=task_form.description.data)
                db.session.add(new_task)
                db.session.commit()
                return redirect('/project_detail/' + project_id)
            else:
                flash('Failed. Please try again.')
        return render_template('projectDetail.html', project=project, task_form=task_form, tasks=tasks)


@login_required
@task.route('/task/<task_id>', methods=['post', 'get'])
def add_time_sheet(task_id):
    timeSheet_form = TimeSheetForm()
    task = Task.query.filter_by(task_id=task_id).first()
    timesheets = TimeSheet.query.all()
    if timeSheet_form.is_submitted():
        if timeSheet_form.validate():
            # print(current_user)
            new_time_sheet = TimeSheet(start_time=timeSheet_form.start_time.data,
                                       end_time=timeSheet_form.end_time.data,
                                       comment=timeSheet_form.comment.data,
                                       user_id=current_user.user_id,
                                       date_submitted=datetime.date.today(),
                                       task_id=task_id)
            db.session.add(new_time_sheet)
            db.session.commit()
            return redirect('/task/' + task_id)
        else:
            flash('Wrong data post. Try again.')
    return render_template('timeSheet.html', task=task, timeSheet_form=timeSheet_form, timesheets=timesheets)


@task.route('/data_visualized/<user_id>')
def data_visualized(user_id):
    project = Project.query.filter_by(user_id=user_id).first()
    duration = (project.expected_end_date - project.start_date).days
    tasks = Task.query.filter_by(project_id=project.project_id).all()
    task_name = []
    task_duration = []
    for task in tasks:
        task_name.append("task " + str(task.task_id))
        # start_date = datetime.datetime(task.start_date)
        # end_date = datetime.datetime(task.end_date)
        interval = (task.end_date - task.start_date).days
        duration -= interval
        task_duration.append(interval)
    task_name.append('Unused time')
    task_duration.append(duration)
    time_usage_chart = Pie({'width': '400px', 'height': '400px', 'chart_id': project.project_name + '_usage_chart'})
    # time_usage_chart.add_xaxis(task_name)
    # time_usage_chart.add_yaxis('duration', task_duration)
    time_usage_chart.add(project.project_name, [list(z) for z in zip(task_name, task_duration)], radius=["30%", "55%"],)
    return render_template('data_visualized.html', time_usage=time_usage_chart.render_embed())


@task.route('/view_other_project')
def view_other_project():
    pass