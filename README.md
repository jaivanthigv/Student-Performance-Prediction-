# 🎓 Student Performance Prediction Dashboard

A Machine Learning project that predicts student academic performance based on factors like study hours, attendance, assignments, and previous scores.

The project also includes an **interactive data visualization dashboard** to analyze student performance patterns.

---

## 🚀 Project Overview

This project uses **Machine Learning and Data Visualization** to:

* Predict whether a student will **Pass or Fail**
* Analyze factors affecting student performance
* Visualize relationships between study habits and results
* Provide an interactive dashboard for insights

---

## 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* Seaborn

---

## 📂 Project Structure

```
Student-Performance-Prediction
│
├── data
│   └── students.csv
│
├── models
│   └── model.pkl
│
├── src
│   ├── train.py
│   └── predict.py
│
├── dashboard.py
├── webapp.py
└── README.md
```

---

## ⚙️ Installation

1️⃣ Clone the repository

```
git clone https://github.com/yourusername/student-performance-prediction.git
```

2️⃣ Navigate to the project folder

```
cd student-performance-prediction
```

3️⃣ Install required libraries

```
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

---

## ▶️ Run the Project

### Train the Model

```
python src/train.py
```

This will create the trained model file:

```
models/model.pkl
```

---

### Run the Performance Prediction App

```
python -m streamlit run webapp.py
```

---

### Run the Data Visualization Dashboard

```
python -m streamlit run dashboard.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

## 📊 Dashboard Features

The dashboard includes:

* Dataset preview
* Study hours vs performance analysis
* Attendance distribution
* Previous score comparison
* Feature correlation heatmap

---

## 💡 Machine Learning Model

The project uses **Logistic Regression** to classify student performance.

Input Features:

* Study Hours
* Attendance
* Assignments Completed
* Previous Score

Output:

* Pass / Fail prediction

---

## 🔮 Future Improvements

* Add larger real-world datasets
* Implement advanced models (Random Forest, XGBoost)
* Improve dashboard with interactive filters
* Deploy the application online

---

## 👩‍💻 Author

**Jaivanthi Venkatasan**

B.Tech – Artificial Intelligence & Data Science
Interested in Machine Learning, Data Science, and Generative AI.

---

## ⭐ Support

If you like this project, please consider **starring ⭐ the repository on GitHub.**
