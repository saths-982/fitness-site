🏋️‍♂️ Sports & Fitness Coaching Website
📌 Project Description
This project is a web-based Sports & Fitness Coaching platform that allows users to register, log in, and explore various training programs. It includes a homepage, user authentication, and an exit page with a farewell message.

🚀 Features
✅ Home Page – Introduction, resume download, logout option
✅ Registration Page – User sign-up (stored in MySQL)
✅ Login Page – User authentication (verifies credentials from database)
✅ Exit Page – Displays “Thanks for visiting my website”

📂 Folder Structure
plaintext
Copy
Edit
sports_fitness_website/  
│── app.py              # Backend (Flask)  
│── requirements.txt    # Python dependencies  
│── venv/               # Virtual environment  
│── static/             # Contains CSS, JavaScript, images  
│── templates/          # HTML files  
│   ├── index.html  
│   ├── register.html  
│   ├── login.html  
│── .gitignore          # Ignored files  
│── README.md           # Project documentation  
🛠 Installation & Setup
1️⃣ Clone the repository
sh
Copy
Edit
git clone https://github.com/yourusername/sports-fitness-coaching.git
cd sports-fitness-coaching
2️⃣ Set up Virtual Environment & Install Dependencies
sh
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux  
venv\Scripts\activate      # Windows  
pip install -r requirements.txt
3️⃣ Database Setup
Install MySQL and create a database named fitness_db.
Update database credentials inside app.py.
4️⃣ Run the Flask Server
sh
Copy
Edit
python app.py
The website will be available at http://127.0.0.1:5000.
🌍 Deployment Instructions
Frontend Deployment
Upload static and templates to Vercel or Netlify.
Backend Deployment
Deploy Flask backend on Render or Railway.
Update API URLs
If frontend and backend are hosted separately, update API calls in frontend to use the deployed backend URL.
🏗 Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
Database: MySQL
Hosting: Render (Backend), Vercel/Netlify (Frontend)
📜 License
This project is open-source under the MIT License.

📩 Contact
For any queries or improvements:
📧 Email: ssangara@gitam.in