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
                description="Initially, the space appeared plain and lacked distinctive character, with minimal furnishings and a neutral palette that felt underwhelming. Through thoughtful interior design, the room was transformed into a warm and inviting living area. Rich textures, contemporary furniture, and layered lighting introduced depth and comfort. Elegant accents such as a patterned rug, stylish wall art, and lush greenery added visual interest and personality. The overall composition now reflects a well-balanced blend of style and function, creating a welcoming atmosphere ideal for relaxation or hosting. This project highlights the power of intentional design in redefining everyday spaces.",
                location="Town, Nairobi",
                date="",
                user_id=yvonne.id
            ),
            Projects(
                title="Residential Industry",
                project_name="Lunawood Gazebo Fit Outs.",
                before_image="project_pics/LunaWoodGazeboBefore.jpeg",
                after_image="project_pics/LunaWoodGazeboAfter.jpeg",
                description="This rooftop underwent a dramatic transformation, evolving from a plain, exposed concrete surface into a vibrant, inviting outdoor retreat. Using LunaWood, we introduced a sleek pergola structure that brings warmth and architectural interest to the space. The addition of high-quality artificial turf infuses the area with a natural, green aesthetic while enhancing comfort and usability. Together, these elements create a functional and stylish rooftop environment—perfect for relaxing, hosting, or simply enjoying the view. This project showcases how sustainable materials and smart design can elevate any underutilized space into a standout feature.",
                location="Lavington, Nairobi",
                date="",
                user_id=yvonne.id
            ),
            Projects(
                title="Commercial Office Industry",
                project_name="Letshego Renovations",
                before_image="project_pics/LetsgoBefore.jpeg",
                after_image="project_pics/LetsgoAfter.jpeg",
                description="The Letshego project was one of our most transformative and rewarding undertakings, where we reimagined a deteriorating space plagued by persistent roofing issues and uninspiring, lackluster interiors. The original environment suffered from years of water damage, leaving the structure vulnerable and visually uninviting. Our design team approached the project with a vision to breathe life into the space, introducing bold colors, creative finishes, and carefully curated materials that not only addressed the structural challenges but also elevated the overall ambiance. The result was a vibrant, welcoming environment that reflected both functionality and aesthetic harmony, turning what was once a neglected interior into a dynamic and uplifting space.",
                location="316 Second Ngong Avenue, Nairobi, Nairobi County ",
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
                content="In recent decades, interior design has transitioned from a niche interest to a global phenomenon, influencing everything from how we arrange our homes to how businesses present themselves to the world. As the world becomes increasingly connected and visual storytelling grows in importance, the role of interior design in shaping our everyday experiences has become more prominent than ever. Whether it’s through Instagram-worthy spaces, stylish coworking hubs, or wellness-focused environments, interior design is no longer reserved for luxury properties—it has become a key player in lifestyle and culture.One of the primary reasons for the rise of interior design is the growing emphasis on personal well-being and comfort. People now recognize that the environments they inhabit significantly impact their mood, productivity, and health. This realization has led to a surge in demand for well-designed spaces that cater not just to aesthetics, but also to functionality and emotional well-being. For instance, biophilic design—which incorporates natural elements like plants, light, and organic textures—has become increasingly popular as more individuals seek tranquility and balance in their homes. Designers are prioritizing layouts that allow for relaxation and mindfulness, turning living rooms into sanctuaries and bedrooms into peaceful retreats.Moreover, the digital era has amplified the influence of interior design through social media platforms like Pinterest, Instagram, and TikTok. Users are exposed daily to stunning interiors from around the world, inspiring them to transform their own spaces with creativity and intention. This access to global design trends has not only democratized interior design but also encouraged a rise in DIY culture. Now, with online tutorials, virtual consultations, and budget-friendly decor hacks, almost anyone can embrace design thinking and improve their living space. Brands and influencers have capitalized on this trend, offering inspiration and accessible products to a wide audience eager to curate homes that reflect their identities.Businesses and organizations, too, have recognized the power of interior design in shaping brand perception and enhancing user experience. Modern offices are no longer rows of cubicles—they are vibrant, open-plan environments that promote collaboration, creativity, and well-being. Restaurants, hotels, and retail spaces increasingly invest in unique interior designs to attract and retain customers. In a competitive market, the ambiance of a space can be just as important as the service or product offered. As such, interior designers are becoming essential partners in creating memorable and engaging environments that resonate with people emotionally.In conclusion, the rise of interior design marks a cultural shift toward intentional living and working. As people become more attuned to the impact of their surroundings, design will continue to evolve in ways that enrich everyday life. With innovation in materials, technology, and human-centered thinking, the future of interior design looks both exciting and empowering. It’s more than decorating—it’s about creating spaces that tell stories, support well-being, and connect us more deeply to the world around us.",
                image="https://images.unsplash.com/photo-1463797221720-6b07e6426c24?q=80...",
                author_id=yvonne.id
            ),
            Blogs(
                title="Top 10 Design Trends of 2024",
                content="As we step into 2024, the interior design world is brimming with creativity, innovation, and a deeper appreciation for personal expression. The trends of this year are not just about what’s fashionable—they’re a response to the evolving ways we live, work, and connect with our environments. Sustainability, individuality, and functionality are at the heart of the design movement, pushing boundaries and inviting people to reimagine their spaces with intention and flair. Whether you’re updating a room or redesigning your entire home, the top design trends of 2024 are sure to inspire a space that feels both modern and meaningful.One standout trend in 2024 is the resurgence of bold colors and patterns. After years of muted tones and minimalist palettes, designers are embracing rich hues like emerald green, terracotta, navy, and mustard yellow. These colors are being used on walls, furnishings, and decor pieces to bring warmth, personality, and a sense of drama into interiors. Pairing these bold shades with playful patterns—such as geometric shapes, organic prints, and retro motifs—creates spaces that feel dynamic and full of life. This trend encourages homeowners to express themselves without fear, mixing and matching colors and textures to craft unique and energized environments.Sustainability continues to drive innovation in the design world, and in 2024, eco-conscious materials and practices are more important than ever. Reclaimed wood, recycled metal, bamboo, and cork are being used in furniture and finishes to minimize environmental impact while maintaining beauty and durability. Designers are also prioritizing energy-efficient lighting, non-toxic paints, and upcycled decor. In addition, there is a growing interest in vintage and second-hand furniture, not only as a way to reduce waste but also to add character and history to a space. This movement toward sustainable design reflects a collective awareness of our responsibility to the planet, proving that style and sustainability can go hand in hand.Another major theme for 2024 is the fusion of technology with comfort and aesthetics. Smart home integrations are being thoughtfully embedded into design—from voice-controlled lighting and thermostats to hidden charging stations and automated window treatments. However, rather than making homes feel sterile or futuristic, designers are blending technology seamlessly with soft materials and cozy elements. Think soft textiles, curved furniture, warm lighting, and tactile surfaces combined with tech-driven functionality. This balance creates spaces that feel both innovative and inviting, meeting modern needs without sacrificing warmth or authenticity.In conclusion, the top design trends of 2024 reflect a broader cultural shift toward individuality, environmental responsibility, and the harmony of form and function. This year, it’s all about crafting interiors that tell a story—your story—while also respecting the world around us. Whether you’re drawn to bold statements, sustainable choices, or tech-enhanced comfort, 2024 offers a diverse palette of ideas to make your space truly your own. Embrace the trends that resonate with you and create a home that not only looks great but also feels right.",
                image="https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?q=80...",
                author_id=yvonne.id
            ),
            Blogs(
                title="How to Choose the Right Color Scheme",
                content="Choosing the right color scheme is one of the most powerful decisions you can make in interior design. Colors influence how we feel, how we think, and even how we behave. They can energize a room or calm it down, make a space feel larger or more intimate, and reflect your personal style. But with countless shades and combinations available, finding the right palette can feel overwhelming. Fortunately, with a bit of guidance and inspiration, creating a cohesive and beautiful color scheme becomes an enjoyable and rewarding part of the design process.Start by considering the purpose and mood of each room. Are you designing a peaceful bedroom, a productive home office, or a lively living room? Cool colors like blues, greens, and purples tend to evoke calmness and serenity—making them ideal for bedrooms and bathrooms. Warm colors like reds, oranges, and yellows, on the other hand, bring energy and warmth, which work well in dining rooms, kitchens, and entertainment spaces. Neutrals such as whites, beiges, and grays offer versatility and balance, and they can serve as the perfect backdrop to accentuate bolder hues through furniture, textiles, and art.Another essential factor to consider is lighting—both natural and artificial. A color that looks soft and subtle in daylight might appear darker or more saturated under artificial lighting. South-facing rooms receive more warm light, enhancing warmer tones, while north-facing rooms have cooler light that complements cool tones. Before committing to a palette, test your chosen colors on different walls and observe how they change throughout the day. Additionally, think about how the colors will flow between adjoining rooms to maintain visual harmony throughout the home. Color continuity doesn't mean every room must look the same, but rather that the transitions feel natural and cohesive.Don’t shy away from using the color wheel as a practical tool. Complementary colors (those opposite each other on the wheel) like blue and orange create high contrast and energy, while analogous colors (next to each other, like green, blue, and teal) offer a more subtle and soothing effect. Monochromatic schemes, using various shades of one color, can feel elegant and minimalist. Accent colors add personality—whether it’s a bold piece of furniture, a feature wall, or vibrant accessories. Ultimately, the best color scheme is one that resonates with your personality and lifestyle, making your space feel truly yours.In conclusion, selecting the perfect color scheme involves more than picking your favorite colors—it’s about creating a harmonious atmosphere that enhances your daily life. By understanding the emotional impact of colors, evaluating lighting conditions, and using basic design principles, you can confidently craft a palette that brings out the best in your space. Let your creativity lead, test freely, and trust that the right colors will speak to you. A thoughtfully chosen color scheme doesn’t just decorate a room—it transforms it into a place that feels like home.",
                image="https://images.unsplash.com/photo-1662672324132-90d55416a840?q=80...",
                author_id=yvonne.id
            ),
            Blogs(
                title="The Benefits of Minimalist Design",
                content="Minimalist design has evolved from a modern aesthetic trend into a meaningful lifestyle choice for many homeowners and interior designers. Rooted in simplicity, clarity, and intentionality, minimalist interiors focus on eliminating excess and embracing functionality without sacrificing beauty. It’s more than just an aesthetic—it’s a philosophy that promotes mindful living, where every item has a purpose, and every space invites calm and clarity. As our lives become more cluttered and fast-paced, the appeal of minimalist design continues to grow.One of the most compelling benefits of minimalist design is its ability to create a serene, clutter-free environment. By removing unnecessary objects and focusing on essential elements, minimalist interiors provide a mental and visual break from the chaos of everyday life. Clean lines, neutral color palettes, and open spaces encourage relaxation and reduce stress. Whether you’re working from home or unwinding after a long day, a minimalist space can offer the calm and clarity needed to recharge and stay focused. This design approach allows your home to become a sanctuary where simplicity fosters peace.Functionality is another core strength of minimalist interiors. Every piece of furniture and décor is chosen with intention, contributing to both the look and utility of a room. This means investing in high-quality, versatile pieces that serve multiple purposes—like a sleek storage bench or a modular sofa. Minimalism promotes the idea that less is more, encouraging homeowners to prioritize quality over quantity. The result is a space that’s not only beautiful but also practical and efficient. This thoughtful approach to design helps reduce waste, save money, and streamline daily routines.Minimalist design also offers timeless appeal and adaptability. Unlike trends that come and go, minimalist spaces age gracefully because they rely on classic design principles rather than flashy details. A minimalist room can easily be updated with a few new accents or color shifts, allowing it to evolve with your personal style without requiring a complete overhaul. Additionally, the minimalist ethos often aligns with sustainable living, as it discourages overconsumption and promotes mindful purchasing habits. By focusing on what truly matters, minimalist interiors contribute to both personal well-being and environmental responsibility.In conclusion, minimalist design is more than a visual style—it’s a way of living that promotes peace, purpose, and practicality. Through simplicity, it offers clarity; through intention, it offers function; and through restraint, it offers beauty. Whether you're designing a new home or reimagining your current space, embracing minimalism can help you create a living environment that reflects your values and supports your lifestyle. In a world full of distractions, minimalism reminds us that we don’t need more—we just need what matters.",
                image="https://images.unsplash.com/photo-1698674913743-88148adc7b26?q=80...",
                author_id=yvonne.id
            ),
            Blogs(
                title="Maximizing Small Spaces",
                content="Minimalist design has evolved from a modern aesthetic trend into a meaningful lifestyle choice for many homeowners and interior designers. Rooted in simplicity, clarity, and intentionality, minimalist interiors focus on eliminating excess and embracing functionality without sacrificing beauty. It’s more than just an aesthetic—it’s a philosophy that promotes mindful living, where every item has a purpose, and every space invites calm and clarity. As our lives become more cluttered and fast-paced, the appeal of minimalist design continues to grow.One of the most compelling benefits of minimalist design is its ability to create a serene, clutter-free environment. By removing unnecessary objects and focusing on essential elements, minimalist interiors provide a mental and visual break from the chaos of everyday life. Clean lines, neutral color palettes, and open spaces encourage relaxation and reduce stress. Whether you’re working from home or unwinding after a long day, a minimalist space can offer the calm and clarity needed to recharge and stay focused. This design approach allows your home to become a sanctuary where simplicity fosters peace.Functionality is another core strength of minimalist interiors. Every piece of furniture and décor is chosen with intention, contributing to both the look and utility of a room. This means investing in high-quality, versatile pieces that serve multiple purposes—like a sleek storage bench or a modular sofa. Minimalism promotes the idea that less is more, encouraging homeowners to prioritize quality over quantity. The result is a space that’s not only beautiful but also practical and efficient. This thoughtful approach to design helps reduce waste, save money, and streamline daily routines.Minimalist design also offers timeless appeal and adaptability. Unlike trends that come and go, minimalist spaces age gracefully because they rely on classic design principles rather than flashy details. A minimalist room can easily be updated with a few new accents or color shifts, allowing it to evolve with your personal style without requiring a complete overhaul. Additionally, the minimalist ethos often aligns with sustainable living, as it discourages overconsumption and promotes mindful purchasing habits. By focusing on what truly matters, minimalist interiors contribute to both personal well-being and environmental responsibility.In conclusion, minimalist design is more than a visual style—it’s a way of living that promotes peace, purpose, and practicality. Through simplicity, it offers clarity; through intention, it offers function; and through restraint, it offers beauty. Whether you're designing a new home or reimagining your current space, embracing minimalism can help you create a living environment that reflects your values and supports your lifestyle. In a world full of distractions, minimalism reminds us that we don’t need more—we just need what matters.",
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
