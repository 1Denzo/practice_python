from flask import Flask, request, jsonify
from regform import RegistrationForm

app = Flask(__name__)

@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        return jsonify({'message': 'Регистрация успешна!'}), 200
    else:
        errors = {field: form.errors[field] for field in form.errors}
        return jsonify({'errors': errors}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')