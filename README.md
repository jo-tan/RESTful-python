<h1 style="color:darkorange">📔 Personal Recipe Collection App with Flask</h1>

### <code style="color:lightskyblue">Brief background info:</code>
I have notebook, card notes and text files on computer, phone device and paper cards which store my food recipes. These are my cooking journals.

This project is a small practice for RESTful API with Flask without any endgoal at the begining. However, I think it will be more fun to give it a purpose. Perhaps someone who wants to do the similiar things could benefit from this project.

This app will:
* [ ] certralize the recipes in a database
* [ ] Have searching function for specific recipe
* [ ] A weekly meal planner & grocery list (maybe?)
* [ ] image / video alongside the recipes
* [ ] tbd...(one feature at a time C:)
---
### <code style="color:lightskyblue">Why python vertiual environment and not Docker?</code>

I've chosen to use the Python virtual environment rather than Docker containerization for several reasons:

1. **Development Simplicity**: A virtual environment provides sufficient isolation for Python dependencies while maintaining a lightweight development workflow.

2. **Resource Efficiency**: For a simple Flask application with minimal dependencies, Docker adds overhead that isn't necessary during initial development.

While Docker excels at creating consistent environments across different systems and can manage complex microservices, this recipe collection app currently doesn't require that level of containerization. If the application evolves to include multiple services, databases, or needs deployment across various environments, using Docker will be a better choice.

--- 
### <code style="color:lightskyblue">Technologies Used</code>

#### Backend
- **Flask**: Lightweight WSGI web application framework
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library
- **Flask-RESTful**: Extension for building REST APIs with Flask

#### Database
- **SQLite**: File-based database for development

#### Environment & Tools
- **Python**: Core programming language
- **pip**: Package installer for Python
- **venv**: Python's virtual environment for dependency isolation

#### Frontend (planned/in-progress)
- **HTML/CSS**: Basic structure and styling
- **JavaScript**: For interactive elements
- **Bootstrap**: Responsive design framework

---
tbd...