from models import Status, db, Projects, Users, Blogs, Contact
from datetime import datetime
from app import app
from werkzeug.security import generate_password_hash

def main():
    with app.app_context():
        db.create_all()

        # Clear tables
        Projects.query.delete()
        Users.query.delete()
        Blogs.query.delete()
        Contact.query.delete()
        db.session.commit()

        # Create users
        users = [
            Users(
                name="Yvonne Mutisya",
                username="Y.Mutisya",
                email="yvonne@jawabuinteriors.co.ke",
                _password=generate_password_hash("password"),
                image="",
                department="Director",
                status=Status.ONLINE,
                super_user=True
            ),
        ]
        db.session.add_all(users)
        db.session.commit()

        yvonne = Users.query.filter_by(email="yvonne@jawabuinteriors.co.ke").first()

        # Create projects
        projects = [
            Projects(
                title="Hospitality Industry",
                project_name="Dream Beam House-Coffee Lounge- Restaurant Interior Fit Outs.",
                before_image="project_pics/Beforedreambean.jpeg",
                after_image="project_pics/Afterdreambean.jpeg",
                description="DreamBean Café underwent a full interior transformation aimed at elevating its atmosphere...",
                location="Town, Nairobi",
                date="",
                user_id=yvonne.id
            )
        ]
        db.session.add_all(projects)
        db.session.commit()

        # Create blogs
        blogs = [
            Blogs(
                title="The Rise of Interior Design",
                content="Interior design has seen a remarkable rise...",
                image="https://images.unsplash.com/photo-1463797221720-6b07e6426c24?q=80...",
                author_id=yvonne.id
            ),
            Blogs(
                title="Top 10 Design Trends of 2024",
                content="As we step into 2024, interior design is shifting...",
                image="https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?q=80...",
                author_id=yvonne.id
            ),
            Blogs(
                title="How to Choose the Right Color Scheme",
                content="Choosing the right color scheme can set the tone...",
                image="https://images.unsplash.com/photo-1662672324132-90d55416a840?q=80...",
                author_id=yvonne.id
            ),
            Blogs(
                title="The Benefits of Minimalist Design",
                content="Minimalist design isn’t just an aesthetic—it’s a lifestyle...",
                image="https://images.unsplash.com/photo-1698674913743-88148adc7b26?q=80...",
                author_id=yvonne.id
            ),
            Blogs(
                title="Maximizing Small Spaces",
                content="Living in a small space doesn’t mean sacrificing comfort...",
                image="https://images.unsplash.com/photo-1653974123177-fe9c05fb79e6?q=80...",
                author_id=yvonne.id
            )
        ]
        db.session.add_all(blogs)
        db.session.commit()

        # Create contact forms
        contacts = [
            Contact(
                first_name="John",
                surname="Doe",
                email="john.doe@example.com",
                phone_number="123-456-7890",
                project_type="Interior Design",
                description="I would like to know more about your services."
            ),
            Contact(
                first_name="Jane",
                surname="Smith",
                email="jane.smith@example.com",
                phone_number="098-765-4321",
                project_type="Office Renovation",
                description="Can you provide a quote for a new project?"
            ),
            Contact(
                first_name="Alice",
                surname="Johnson",
                email="alice.johnson@example.com",
                phone_number="555-555-5555",
                project_type="Home Renovation",
                description="What are your working hours?"
            )
        ]
        db.session.add_all(contacts)
        db.session.commit()

        print("Done seeding!")

if __name__ == "__main__":
    main()
