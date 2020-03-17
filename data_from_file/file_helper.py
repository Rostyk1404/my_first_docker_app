from flask import Flask

app = Flask(__name__)


@app.route('/get_data_from_file')
def get_data_from_file():
    path = "/home/ross/myfirst_docker_app/data_from_number_consumer/saved_data"
    with open(path, "r") as file:
        return file.read()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
