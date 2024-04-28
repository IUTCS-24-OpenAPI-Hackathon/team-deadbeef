from flask import Blueprint, render_template, request, session

security = Blueprint("security", __name__, static_folder="static", template_folder="templates")


@security.route('/change-password')
def change_pass_view():
    return render_template('change_pass.html')


@security.route('/reset-password/initiate')
def reset_pass():
    return render_template('reset_pass_ini.html')


@security.route('/reset-password/confirm')
def reset_pass_con():
    if 'temp_mail' in session:
        email = session['temp_mail']
        return render_template('reset_pass_confirm.html', email=email)


# @security.route('/reset-password/check'):
# def reset_pass_check():
#     data = request.json
#     email = data.get('email')
#     code = data.get('code')
#


@security.route('/reset-password/update')
def reset_pass_update():
    return render_template('reset_pass_confirm2.html')
