# 🔐 OTP-Based Two-Factor Authentication (2FA) System  
### Secure OTP-based Two-Factor Authentication system built with Flask, PyOTP, and QR code integration

A lightweight and secure **TOTP-based 2FA system** that allows users to register, scan a QR code using Google Authenticator, and verify their identity using time-based one-time passwords.

---

## 📌 Features

- ✔ User Registration with Secret Key Generation  
- ✔ QR Code Generation for Google Authenticator  
- ✔ TOTP-based OTP Verification (PyOTP)  
- ✔ Secure Authentication Flow  
- ✔ Flask-based lightweight backend  
- ✔ HTML/CSS-based simple frontend  
- ✔ Compatible with Google Authenticator / Authy  

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Backend  | Flask(Python) |
| OTP Engine | PyOTP |
| QR Code | qrcode + Pillow |
| Frontend | HTML |
| Environment | Python 3 |

---

## 📁 Project Structure

```
OTP_2FA_Project/
│── app.py
│── requirements.txt
│── Procfile (if deployed)
│
├── templates/
│     ├── register.html
│     └── verify.html
│
└── static/
      └── qrcodes/
            └── (Generated QR codes saved here)
```

---

## 🚀 How to Run Locally

### **1️⃣ Install dependencies**
```
pip install flask pyotp qrcode pillow
```

### **2️⃣ Run the application**
```
python app.py
```

### **3️⃣ Open in browser**
```
http://127.0.0.1:5000
```

---

## 🧪 How It Works (Flow)

### **🔹 Step 1 — User Registers**
A unique secret key is generated.

### **🔹 Step 2 — QR Code Generated**
User scans it with Google Authenticator.

### **🔹 Step 3 — OTP Verification**
User enters a 6-digit OTP from the authenticator.

If valid → login succeeds  
If invalid → access denied

---

## 📸 Screenshots (Add Yours)

> Replace these placeholders with your screenshots.

```
/screenshots/registration_page.png  
/screenshots/qr_code_page.png  
/screenshots/otp_verification.png
```

---

## 📄 Mini-Project Details (For University)

**Name:** Vikram Singh  
**Roll Number:** 22131011610  
**Admission Number:** 22SCSE1011643  
**University:** Galgotias University 
**Department:** B.Tech CSE
**Project Type:** Individual  

---

## 📦 Deployment (Optional)

If deployed, add your live link here:

```
https://your-deployed-app-link.com
```

---

## 📝 License  
This project is for academic and learning purposes.

---

## ⭐ Show Your Support  
If you like this project, consider giving it a **star 🌟 on GitHub**
we consider your small ratings too,help us if you do have suggestions..we would love to hear your suggestions so that we can improve.
