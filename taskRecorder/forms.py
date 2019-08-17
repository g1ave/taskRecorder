from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    username = fields.StringField('Username',
                                  validators=[DataRequired()],
                                  render_kw={
                                      'class': 'form-control mt-2',
                                      'placeholder': 'Enter your E-mail id',
                                             })
    password = fields.PasswordField('Password',
                                    validators=[DataRequired()],
                                    render_kw={
                                        'class': 'form-control mt-2',
                                        'placeholder': 'Enter your password'
                                               })
    login = fields.SubmitField('Login', render_kw={'class': 'form-control mt-2'})


class RegisterForm(FlaskForm):
    first_name = fields.StringField('first name',
                                    validators=[DataRequired()],
                                    render_kw={
                                        'class': 'form-control mt-2',
                                        'placeholder': 'first name',
                                    })
    last_name = fields.StringField('last name',
                                   validators=[DataRequired()],
                                   render_kw={
                                        'class': 'form-control mt-2',
                                        'placeholder': 'last name',
                                    })
    email = fields.StringField('Email',
                               validators=[DataRequired(), Email("Please input correct E-mail!")],
                               render_kw={
                                        'class': 'form-control mt-2',
                                        'placeholder': 'Email',
                                    })
    password = fields.PasswordField('Password',
                                    validators=[DataRequired(), Length(6, 50, '6-20 characters')],
                                    render_kw={
                                        'class': 'form-control mt-2',
                                        'placeholder': '6 - 20 characters password'
                                    })
    password_confirm = fields.PasswordField('Confirm password',
                                            validators=[DataRequired(), EqualTo('password', 'Password does\'t ,match')],
                                            render_kw={
                                                'class': 'form-control mt-2',
                                                'placeholder': 'Confirm your password',
                                            })
    submit = fields.SubmitField('Sign up',
                                render_kw={
                                    'class': 'form-control mt-2'
                                })


class ProjectForm(FlaskForm):
    project_name = fields.StringField('project name',
                                      validators=[DataRequired()],
                                      render_kw={
                                          'class': 'form-control mt-2',
                                          'placeholder': 'Project name',
                                      })
    start_date = fields.DateField('start date',
                                  validators=[DataRequired("Please check your format.")],
                                  render_kw={
                                      'class': 'form-control mt-2',
                                      'placeholder': 'Start date (yyyy-mm-dd)',
                                  })
    expected_end_date = fields.DateField('expected end date',
                                         validators=[DataRequired("Please check your format.")],
                                         render_kw={
                                            'class': 'form-control mt-2',
                                            'placeholder': 'Expected end date (yyyy-mm-dd)',
                                         })
    project_description = fields.StringField('Description',
                                             render_kw={
                                                 'class': 'form-control mt-2',
                                                 'placeholder': 'Project description',
                                             })
    submit = fields.SubmitField('Create',
                                render_kw={
                                    'class': 'form-control mt-2'
                                })


class TaskFrom(FlaskForm):
    start_date = fields.DateField('Start date',
                                  validators=[DataRequired()],
                                  render_kw={
                                      'class': 'form-control mt-2',
                                      'placeholder': 'Start date',
                                  })
    end_date = fields.DateField('End date',
                                validators=[DataRequired()],
                                render_kw={
                                      'class': 'form-control mt-2',
                                      'placeholder': 'End date',
                                  })
    description = fields.StringField('Description',
                                     render_kw={
                                         'class': 'form-control mt-2',
                                         'placeholder': 'Project description',
                                             })
    submit = fields.SubmitField('Add',
                                render_kw={
                                    'class': 'form-control mt-2'
                                })


class TimeSheetForm(FlaskForm):
    start_time = fields.TimeField('Start time',
                                  validators=[DataRequired()],
                                  render_kw={
                                      'class': 'form-control mt-2',
                                      'placeholder': 'Start time',
                                  })
    end_time = fields.TimeField('End time',
                                validators=[DataRequired()],
                                render_kw={
                                    'class': 'form-control mt-2',
                                    'placeholder': 'End time',
                                })
    comment = fields.StringField('Description',
                                 render_kw={
                                         'class': 'form-control mt-2',
                                         'placeholder': 'Comment',
                                     })
    submit = fields.SubmitField('Add',
                                render_kw={
                                    'class': 'form-control mt-2'
                                })
