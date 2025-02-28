# Import the necessary modules
from models import Status, db, Projects, Users, Blogs, Contact  # Ensure you import the required models
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
        Blogs.query.delete()
        Contact.query.delete()
        
        

        db.session.commit()

        # Create users
        users = [
            Users(
                name="Yvonne Mutisya",
                username="Y.Mutisya",
                email="yvonne@jawabuinteriors.co.ke",
                _password=generate_password_hash("password"),  # Replace with actual password
                image="",
                department="Director",
                status=Status.ONLINE,
                super_user=True
            ),
        ]

        db.session.add_all(users)
        db.session.commit()

        # Retrieve users to assign them as owners of projects and blogs
        dave = Users.query.filter_by(email="daveroymutisya2@gmail.com").first()
        natasha = Users.query.filter_by(email="e.n.wairi@gmail.com").first()
        yvonne = Users.query.filter_by(email="yvonne@jawabuinteriors.co.ke").first()

        # Create projects and assign to users
        projects = [
            Projects(
                title="Corporate and Commercial Clients",
                project_name="German Radio and TV- Interior fit outs and Renovations.",
                image="",
                description="This project involves the complete interior fit-out and renovation of a German radio and television facility. The scope of work includes designing and upgrading studios, control rooms, and office spaces to meet modern broadcasting standards. High-quality acoustic treatments, ergonomic workspaces, and state-of-the-art lighting and audiovisual installations are key aspects of the renovation. The project aims to create a functional, aesthetically pleasing, and technologically advanced environment that enhances workflow efficiency and supports high-quality media production.",
                location="Nairobi",
                date="",
                user_id=yvonne.id
            ),
             Projects(
                title="Corporate and Commercial Clients",
                project_name="Kenya Red Cross – (prequalified as supplier 2019-2020).",
                image="",
                description="",
                location="",
                date="",
                user_id=yvonne.id
            ),
            Projects(
                title="Corporate and Commercial Clients",
                project_name="Juba Airways, Panari Plaza-Office Fit Outs",
                image="",
                description="",
                location="",
                date="",
                user_id=yvonne.id
            ),
            Projects(
                title="Hospitality Industry",
                project_name="Dream Beam House-Coffee Lounge- Restaurant Interior Fit Outs.",
                image="",
                description="",
                location="",
                date="",
                user_id=yvonne.id
            ),
            Projects(
                title="Hospitality Industry",
                project_name="Kapital Coffee Lounge, Lonrho House – Restaurant Interior Fit Outs.",
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
                user_id=yvonne.id
            ),
            Projects(
                title="Banking Industry",
                project_name="Kenya Post Office Savings Bank – Bank and Office Fit Outs.",
                image="",
                description="",
                location="",
                date="",
                user_id=yvonne.id
            ),
            Projects(
                title="Banking Industry",
                project_name="Family Bank (prequalified for construction major civil works 2019-2020).",
                image="",
                description="",
                location="",
                date="",
                user_id=yvonne.id
            ),
            Projects(
                title="Banking Industry",
                project_name="COOP Bank (prequalified for construction major civil works 2018-2020).",
                image="",
                description="",
                location="",
                date="",
                user_id=yvonne.id
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
                title="Institutions",
                project_name="IVC Medical Clinic, Eldoret – Main Building Works.",
                image="",
                description="",
                location="",
                date="",
                user_id=yvonne.id
            ),
            Projects(
                title="Institutions",
                project_name="Machakos University –Civil and Mechanical works, Interior Fit Outs and Finishes",
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
                user_id=yvonne.id
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
                project_name="Restaurant Interior Fit Outs.",
                image="",
                description="",
                location="",
                date="",
                user_id=yvonne.id
            )
        ]

        db.session.add_all(projects)
        db.session.commit()

        # Create blogs and assign to users
        blogs = [
            Blogs(
                title="The Rise of Interior Design",
                content="Interior design is becoming more popular as people understand the importance of a well-decorated space...",
                image="https://images.unsplash.com/photo-1463797221720-6b07e6426c24?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                author_id=yvonne.id
            ),
            Blogs(
                title="Top 10 Design Trends of 2024",
                content="As we move into 2024, here are the top 10 design trends that are making waves...",
                image="https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                author_id=yvonne.id
            ),
            Blogs(
                title="How to Choose the Right Color Scheme",
                content="Choosing the right color scheme for your space can be daunting. Here are some tips to help you get started...",
                image="https://images.unsplash.com/photo-1662672324132-90d55416a840?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                author_id=yvonne.id
            ),
            Blogs(
                title="The Benefits of Minimalist Design",
                content="Minimalist design is not just about having less. It's about making space for what truly matters...",
                image="https://images.unsplash.com/photo-1698674913743-88148adc7b26?q=80&w=1856&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                author_id=yvonne.id
            ),
            Blogs(
                title="Maximizing Small Spaces",
                content="Living in a small space doesn't mean you have to sacrifice style. Here are some tips to make the most of your space...",
                image="https://images.unsplash.com/photo-1653974123177-fe9c05fb79e6?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
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
