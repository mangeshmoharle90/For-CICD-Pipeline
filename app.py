from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a+b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
