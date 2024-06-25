from models import Status, db, Projects, Users
from datetime import datetime
from app import app
from werkzeug.security import generate_password_hash

def main():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()

        # Clear the database (for testing purposes)
        Projects.query.delete()
        Users.query.delete()

        db.session.commit()

        # Create users
        users = [
            Users(
                name="Dave Roy Mutisya",
                username="Mr.Mutisya",
                email="daveroymutisya2@gmail.com",
                _password=generate_password_hash("G0D15L0v3s_U"),
                image="",
                department="IT and Marketing Department",
                status=Status.ONLINE,
                super_user=True
            ),
            Users(
                name="Natasha Wairimu",
                username="E.N.W",
                email="e.n.wairi@gmail.com",
                _password=generate_password_hash("password"),  # Replace with actual password
                image="",
                department="IT and Marketing Department",
                status=Status.ONLINE,
                super_user=False
            ),
            Users(
                name="Yvonne Mutisya",
                username="Y.Mutisya",
                email="yvonne.mutisya@gmail.com",
                _password=generate_password_hash("password"),  # Replace with actual password
                image="",
                department="Executive",
                status=Status.ONLINE,
                super_user=True
            )
        ]

        db.session.add_all(users)
        db.session.commit()

        # Retrieve users to assign them as owners of projects
        dave = Users.query.filter_by(email="daveroymutisya2@gmail.com").first()
        natasha = Users.query.filter_by(email="e.n.wairi@gmail.com").first()
        yvonne = Users.query.filter_by(email="yvonne.mutisya@gmail.com").first()

        # Create projects and assign to users
        projects = [
            Projects(
                title="Corporate and Commercial Clients",
                project_name="German Radio and TV- Interior fit outs and Renovations.",
                image="",
                description="",
                location="",
                date="",
                user_id=dave.id
            ),
            Projects(
                title="Hospitality Industry",
                project_name="Dream Beam House-Coffee Lounge- Restaurant Interior Fit Outs.",
                image="",
                description="",
                location="",
                date="",
                user_id=natasha.id
            ),
            Projects(
                title="Banking Industry",
                project_name="Kenya Post Office Savings Bank – Bank and Office Fit Outs.",
                image="",
                description="",
                location="",
                date="",
                user_id=dave.id
            ),
            Projects(
                title="Institutions",
                project_name="CITAM- Interior Office fitouts, Landscaping and civil works.",
                image="",
                description="",
                location="",
                date="",
                user_id=yvonne.id
            ),
            Projects(
                title="Residential Works",
                project_name="Hon. Julius Kones-Main Builders Works and Interior Fit Outs.",
                image="",
                description="",
                location="",
                date="",
                user_id=dave.id
            ),
            Projects(
                title="Landscaping",
                project_name="CITAM Woodley.",
                image="",
                description="",
                location="",
                date="",
                user_id=yvonne.id
            ),
            Projects(
                title="Hospitality Industry",
                project_name="The Mug Coffee House- Restaurant Interior Fit Outs.",
                image="",
                description="",
                location="",
                date="",
                user_id=natasha.id
            )
        ]

        db.session.add_all(projects)
        db.session.commit()

        print("Done seeding!")

if __name__ == "__main__":
    main()
