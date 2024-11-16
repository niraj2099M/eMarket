
# **eMarket**

A Django-based marketplace platform for local communities to buy and sell used and new items.

**Features:**

* **User Authentication:** Users can register, login, and log out.
* **Item Listings:** Users can create, edit, and delete listings for items they want to sell.
* **Item Browsing:** Users can browse listings based on categories and search keywords.
* **Messaging:** Users can send and receive messages to communicate with each other.

<br>

**Tech stack:**

* Django
* MySQL 
* Tailwind 

<hr>


**Getting Started**

1. **Clone the Repository:**
   ```bash
   gh repo clone niraj2099M/eMarket
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database:**
   - Create a MySQL database and update the `DATABASE_URL` setting in `settings.py`.
   - Run migrations:
     ```bash
     python3 manage.py makemigrations
     python3 manage.py migrate
     ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```



**License**

This project is licensed under the MIT License.


