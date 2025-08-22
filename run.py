from app import create_app

print(">>> run.py: starting app creation")
app = create_app()
print(">>> run.py: app created")

if __name__ == '__main__':
    print(">>> run.py: running app")
    app.run(debug=True, host='0.0.0.0')

