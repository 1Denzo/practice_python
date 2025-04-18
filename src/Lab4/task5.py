from flask import Flask, request, jsonify
import subprocess
import shlex

app = Flask(__name__)

@app.route('/ps', methods=['GET'])
def get_ps():
    args = request.args.getlist('arg')
    
    command = 'ps ' + ' '.join(shlex.quote(arg) for arg in args)
    
    try:
        result = subprocess.check_output(command, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

    return f"<pre>{result}</pre>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
