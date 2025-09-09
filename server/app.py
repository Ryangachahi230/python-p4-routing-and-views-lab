from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Must return an <h1> with the title
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    # Print to console
    print(parameter)
    # Return plain text (no HTML)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    # Create numbers separated by newlines, with trailing newline
    numbers = "\n".join(str(i) for i in range(parameter)) + "\n"
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    # Perform operation based on parameter
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        # Use true division to return floats (e.g., "1.0")
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"
    
    # Return as plain string
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
