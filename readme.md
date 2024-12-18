# **FlowLance**

## **Description**

FlowLance is an innovative online platform designed to bridge freelancers and clients seeking specialized services. The platform's primary objective is to streamline interactions through features such as detailed freelancer profiles, project management tools, an internal messaging system, and secure payment processing. FlowLance distinguishes itself by offering a user-friendly interface and a range of functionalities that ensure efficient and secure engagements in a competitive marketplace.

---

## **Getting Started**

Follow the guide below to set up the FlowLance project on your local machine.

### **Dependencies**

Ensure the following dependencies are installed:

- Python 3.10 or higher
- Python package manager (`pip`)
- Node.js and npm

### **Project Installation Guide**

#### **0. Prerequisites**

- Ensure Python and Git are installed on your machine.
- Install the virtual environment package (if not installed):

    ```bash
    pip install virtualenv
    ```

#### **1. Clone the Repository**

Clone the project repository to your local environment:

```bash
git clone https://github.com/ronyoz/flowlance
```

#### **2. Navigate to the Project Directory**

Move into the project folder (`src` directory):

```bash
cd flowlance/src
```

#### **3. Set Up the Virtual Environment**

Create and activate a virtual environment:

- **Linux/macOS:**

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

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Install the necessary Node modules for Tailwind CSS:

```bash
npm install
```

### **Running the Project**

#### **1. Apply Database Migrations**

Before running the server, apply the database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### **2. Run the Development Server**

Start the Django development server:

```bash
python manage.py runserver
```

In a separate terminal window, start the Tailwind CSS server:

```bash
python manage.py tailwind start
```

#### **3. Access the Application**

Open your browser and navigate to:

```
http://127.0.0.1:8000
```

---

## **Setting Up Internationalization (i18n)**

### **4. Install `gettext`**

Django uses `gettext` for managing translation files. Install it based on your operating system:

- **Windows (using MSYS2):**
    1. Download MSYS2 from the [MSYS2 website](https://www.msys2.org/).
    2. Run the following in the MSYS2 terminal:

        ```bash
        pacman -S gettext
        ```

- **Linux (Debian/Ubuntu):**

    ```bash
    sudo apt-get install gettext
    ```

- **macOS (using Homebrew):**

    ```bash
    brew install gettext
    brew link --force gettext
    ```

Verify the installation with:

```bash
msguniq --version
```

#### **4.1. Generate Translation Files**

Generate `.po` files for each language:

- **For Spanish**:

    ```bash
    django-admin makemessages -l es
    ```

- **For English**:

    ```bash
    django-admin makemessages -l en
    ```

#### **4.2. Compile Translation Files**

After editing the `.po` files, compile them into `.mo` files:

```bash
django-admin compilemessages
```

---

## **Additional Tips**

- Ensure your virtual environment is activated if you encounter dependency errors.
- Use `python manage.py createsuperuser` to set up an admin account for accessing the Django admin panel.
- If the Google login or some features are not working, it's likely because the `.env` file is missing. Please contact us to get it.

---

## **Authors**

- [Rony Ordoñez](https://github.com/Rony7v7)
- [Juan de la Pava](https://github.com/JuanJDlp)
- [David Artunduaga](https://github.com/David104087)
- [Juan Parra](https://github.com/Juanpapb0401)
- [Pablo Guzmán](https://github.com/Pableis05)
- [Daniel González](https://github.com/danielgrw)
