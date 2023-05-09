from flask import Flask, request
import python_cpp_wrapper

app = Flask(__name__)


@app.route('/')
def add():
    # a = int(request.args.get('1'))
   # b = int(request.args.get('2'))
    a = 1
    b = 2
    result = python_cpp_wrapper.add_numbers(a, b)
    return str(result)


if __name__ == "__main__":
    app.run()
