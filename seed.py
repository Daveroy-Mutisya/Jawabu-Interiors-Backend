from models import Status, db,Projects,Users
from datetime import datetime
from app import app

def main():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()

        # Clear the database (for testing purposes)
        Projects.query.delete()

        db.session.commit()

        users = [
            Users(
                name="Dave Roy Mutisya",
                username="Mr.Mutisya",
                email="daveroymutisya2@gmail.com",
                _password="G0D15L0v3s_U",
                image="",
                department="IT and Marketing Department",
                status=Status.ONLINE,
                director_id=1  # Assuming director ID 1 exists
            ),
            Users(
                name="Natasha Wairimu",
                username="E.N.W",
                email="e.n.wairi@gmail.com",
                _password="",
                image="",
                department="IT and Marketing Department",
                status=Status.ONLINE
            ),
            Users(
                name="Yvonne Mutisya",
                username="",
                email="yvonne.mutisya@gmail.com",
                _password="",
                image="",
                role="Director and C.E.O of Jawabu Interiors",
                status=Status.ONLINE
            )
        ]

        db.session.add_all(users)
        db.session.commit()

        projects = [
            Projects(
                title="Corporate and Commercial Clients",
                project_name="German Radio and TV- Interior fit outs and Renovations.",
                image="",
                description="",
                location="",
                created_at=datetime.utcnow()
            ),
            Projects(
                title="Hospitality Industry",
                project_name="Dream Beam House-Coffee Lounge- Restaurant Interior Fit Outs.",
                image="",
                description="",
                location="",
                created_at=datetime.utcnow()
            ),
            Projects(
                title="Banking Industry",
                project_name="Kenya Post Office Savings Bank – Bank and Office Fit Outs.",
                image="",
                description="",
                location="",
                created_at=datetime.utcnow()
            ),
            Projects(
                title="Institutions",
                project_name="CITAM- Interior Office fitouts, Landscaping and civil works.",
                image="",
                description="",
                location="",
                created_at=datetime.utcnow()
            ),
            Projects(
                title="Residential Works",
                project_name="Hon. Julius Kones-Main Builders Works and Interior Fit Outs.",
                image="",
                description="",
                location="",
                created_at=datetime.utcnow()
            ),
            Projects(
                title="Landscaping",
                project_name="CITAM Woodley.",
                image="",
                description="",
                location="",
                created_at=datetime.utcnow()
            ),
            Projects(
                title="Hospitality Industry",
                project_name="The Mug Coffee House- Restaurant Interior Fit Outs.",
                image="",
                description="",
                location="",
                created_at=datetime.utcnow()
            )
        ]

        db.session.add_all(projects)
        db.session.commit()

        print("Done seeding!")

if __name__ == "__main__":
    main()
