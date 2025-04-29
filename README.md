# 📝 Blog Generation using GenAI (AWS Lambda Deployment)

This project is a serverless blog generation application using **Generative AI** models. It leverages **AWS Lambda** for backend logic, **API Gateway** for exposing the endpoint, and **Postman** for testing the service. The application takes a topic as input and generates a coherent blog post using AI.

---

## 🚀 Features

- Generate blogs dynamically using Generative AI
- AWS Lambda-based backend (serverless)
- REST API deployment via AWS API Gateway
- Postman-tested HTTP POST endpoint
- JSON input and output
- Easily scalable and cost-efficient

---

## 🛠️ Technologies Used

- Python 3.x
- AWS Lambda
- Amazon API Gateway
- Postman
- LLama model (or any GenAI model you want to use)
- AWS IAM (for permissions)

---

## 📦 Project Structure
**Setup & Deployment Steps**
- Write your Lambda function (app.py)
- Create a Lambda function in AWS and upload the code
- Set up API Gateway to trigger the Lambda
- Deploy the API and test with Postman

**Testing with Postman**
- Open Postman
- Select POST method
- Paste the API Gateway URL
- Go to Body → Select raw → choose JSON
- Enter a JSON payload like:
{
  "topic": "Machine Learning"
}
- Click Send and view the generated blog in the response.

