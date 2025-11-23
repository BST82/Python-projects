# 🔗 URL Shortener API (Flask + MongoDB)

A simple and powerful **URL Shortener API** built using **Flask** and **MongoDB**.  
It converts long URLs into short codes and also tracks how many times a link was clicked.

---

## 🚀 Features

- 🔁 Shorten long URLs  
- 🔗 Redirect short URL → original URL  
- 📊 Track clicks (views count)  
- 🗄 Uses MongoDB for data storage  
- 🧹 Clean & organized Flask structure  

---

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|----------|
| Python | Programming Language |
| Flask | Web Framework |
| MongoDB | Database |
| PyMongo | MongoDB Connector |
| REST API | API Architecture |

---

## 📌 API Endpoints

### ** Create Short URL**

**POST** `/api/shorten`
{
  "message": "Short URL created!",
  "short_url": "http://localhost:5000/api/Az5Md8"
}


#### Request Body:
```json
{
  "url": "https://example.com"
}
```
#### Example MongoDB Document:
```json
{
  "_id": "6921c3fe...",
  "short_code": "Az5Md8",
  "original_url": "https://en.wikipedia.org/wiki/LinkedIn",
  "clicks": 2
}
```

### Run the Flask app
```json
python app.py
```
