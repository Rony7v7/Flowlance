# **FlowLance**

## **Description**

FlowLance is a cutting-edge online platform designed to connect freelancers with clients seeking specialized services. The primary goal of the project is to streamline interactions between freelancers and clients by offering features such as detailed profiles, project management tools, an internal messaging system, and secure payment processing. FlowLance stands out by providing innovative functionalities that enhance the user experience, ensuring efficient and secure interactions in a competitive marketplace.

## **Getting Started - IMPORTANT TO CHECK LAST FEATURES**

### **Dependencies**

Ensure the following dependencies are installed:

- Python 3.10 or higher
- Python package manager (`pip`)
- Node.js and npm

### **Project Installation Guide**

Follow these steps to set up and run the Django project on your local machine:

#### **0. Prerequisites**

Ensure you have Python and Git installed on your machine. If you haven't installed the virtual environment package, do so by running:

```bash
pip install virtualenv
```

#### **1. Clone the Repository**

Clone the project repository to your local environment:

```bash
git clone https://github.com/2024-2-PI1-G3/202402-proyecto-gecko-team
```

#### **2. Navigate to the Project Directory**

Change into the project folder, specifically the `src` directory:

```bash
cd 202402-proyecto-gecko-team/src
```

#### **3. Set Up the Virtual Environment**

Create and activate a virtual environment to manage your project's dependencies:

- **Linux / macOS:**

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

- **Windows:**

    ```bash
    python -m venv env
    env\Scripts\activate
    ```

#### **4. Install Project Dependencies**

Install the required Python packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Additionally, install the necessary Node modules to ensure Tailwind CSS works correctly:

```bash
npm install
```

### **Running the Project**

To start using the Django project, follow these steps:

#### **1. Apply Database Migrations**

Before running the server, apply database migrations to set up the initial database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### **2. Run the Development Server**

Start the Django development server:

```bash
python manage.py runserver
```

In a separate terminal window, start the Tailwind server:

```bash
python manage.py tailwind start
```

#### **3. Access the Application**

Once the server is running, access the application in your web browser by navigating to:

```
http://127.0.0.1:8000
```

#### **4. Testing the Latest Functionalities**

To test the latest features, first create a superuser:

```bash
python manage.py createsuperuser
```

Login through the `/login` URL using the superuser credentials. However, to access functionalities in the `/profile` section, you must log in with a freelancer user account, which should be created from the `/admin/` panel.

Some functionalities do not have a direct flow, so please refer to **JIRA** and the following URLs to check specific modules:

**Profile Module**

- [Upload Curriculum](http://127.0.0.1:8000/profile/upload_curriculum/):  
  `http://127.0.0.1:8000/profile/upload_curriculum/`

- [Add Experience](http://127.0.0.1:8000/profile/add_experience/):  
  `http://127.0.0.1:8000/profile/add_experience/`

- [Add Skills](http://127.0.0.1:8000/profile/add_skills/):  
  `http://127.0.0.1:8000/profile/add_skills/`

- [Add Project](http://127.0.0.1:8000/profile/add_project/):  
  `http://127.0.0.1:8000/profile/add_project/`

- [Add Course](http://127.0.0.1:8000/profile/add_course/):  
  `http://127.0.0.1:8000/profile/add_course/`

### **Additional Tips**

- If you encounter errors related to missing dependencies, ensure your virtual environment is activated and try re-running `pip install -r requirements.txt`.
- Use `python manage.py createsuperuser` to set up an admin account for accessing the Django admin panel.

## **Authors**

- Rony Farid Ordoñez, Code: A00397968
- Juan José De La Pava, Code: A00381213
- Juan Pablo Parra, Code: A00398004
- David Artunduaga, Code: A00396342
- Pablo Andrés Guzmán, Code: A00399523
