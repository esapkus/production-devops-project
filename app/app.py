from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Production DevOps Project</h1>
    <h2>Welcome Sandip!</h2>
    <p>Host: {socket.gethostname()}</p>
    <p>CI/CD Pipeline using Jenkins, Docker, ECR & EKS</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
