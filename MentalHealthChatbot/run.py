from ChatbotWebsite import create_app, db

# Create the app
app = create_app()

# Set the secret key
app.secret_key = 'serenity-4-us'

# If you need to create the database tables, you can do it here
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run()
