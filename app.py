from flask import Flask, render_template

app = Flask(__name__)

# Data sementara dalam list Python untuk Dashboard Admin
statistik_admin = [
    {"label": "Total Mata Kuliah", "nilai": 14, "warna": "danger"},
    {"label": "Total SKS Lulus", "nilai": 35, "warna": "dark"},
    {"label": "IPK Kumulatif", "nilai": "3.55", "warna": "success"},
]

daftar_matkul_admin = [
    {"kode": "14823372", "nama": "STATISTIKA DAN PROBABILITAS", "sks": 2, "nilai": "AB", "status": "Lulus"},
    {"kode": "14823393", "nama": "INTERAKSI MANUSIA KOMPUTER", "sks": 3, "nilai": "AB", "status": "Lulus"},
    {"kode": "14823313", "nama": "SISTEM BASIS DATA", "sks": 3, "nilai": "AB", "status": "Lulus"},
    {"kode": "14823274", "nama": "PEMROGRAMAN BERORIENTASI OBJEK", "sks": 4, "nilai": "A", "status": "Lulus"},
    {"kode": "14823192", "nama": "ARSITEKTUR DAN ORGANISASI KOMPUTER", "sks": 2, "nilai": "B", "status": "Lulus"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/matkul")
def matkul():
    return render_template("matkul.html")

@app.route("/nilai")
def nilai():
    return render_template("nilai.html")

@app.route("/admin")
def admin_dashboard():
    return render_template(
        "admin/dashboard.html",
        statistik=statistik_admin,
        matkul=daftar_matkul_admin
    )

if __name__ == "__main__":
    app.run(debug=True)