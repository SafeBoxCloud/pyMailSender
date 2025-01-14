
# **EmailService API**

The EmailService API provides a solution for sending automated emails based on different notification categories. The solution is secure, easy to integrate, and optimized for efficient email sending.

## **Technologies Used**
- **Python**: Main programming language for backend development.
- **Flask**: Web framework in Python for building fast and efficient APIs.
- **Pydantic**: Library for data validation with data models.
- **SMTP**: Protocol used for sending emails.
- **Dotenv**: Management of environment variables from a `.env` file.
- **Logging**: Library for generating detailed and configurable logs.
- **HTML Templates**: Using HTML templates for the body of emails.

## **Features**
- **Automated Email Sending**: Sends emails based on different categories, such as registration confirmation, plan promotion, account deletion, etc.
- **Email Validation**: Validates the recipient's email format before sending.
- **SMTP Integration**: Robust configuration for sending emails through SMTP servers configured via `.env`.
- **Security**: The API validates the request data before processing and sending the emails.

## **Installation**

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/email-service.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd email-service
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the `.env` file** with the required variables:
    ```
    SMTP_SERVER=<your_smtp_server>
    SMTP_PORT=<smtp_port>
    EMAIL_BOT=<email_bot>
    PASSWORD_BOT=<email_bot_password>
    ```

5. **Start the server**:
    ```bash
    python app.py
    ```

## **Routes**

### **POST /email/send_email**
Sends an automated email to the user based on the provided category.

#### **Request Body**
```json
{
  "user": {
    "name": "John",
    "email": "john@example.com"
  },
  "category": "register confirmation"
}
```

- **user**: Object containing the user's data.
    - **name**: User's name.
    - **email**: User's email (must be valid).
- **category**: Category of the email to be sent (one of the options: "account deletion", "full storage", "plan promotion", "register confirmation").

#### **Responses**
- **200 OK**: Email sent successfully.
    ```json
    {
      "msg": "Valid request",
      "data": {
        "user": {
          "name": "John",
          "email": "john@example.com"
        },
        "category": "register confirmation"
      }
    }
    ```
- **400 Bad Request**: Invalid request body.
    ```json
    {
      "error": "Invalid request body"
    }
    ```

### **Email Validation**
The system checks if the provided email is valid before attempting to send the email. The validation is done using a regular expression.

### **Sending the Email**
The API selects the appropriate template for each email category and sends the content using the SMTP configuration defined in the `.env`.

## **Contributing**
Contributions are welcome! To contribute, follow these steps:

1. **Fork the repository**.
2. **Create a branch for your feature**:
    ```bash
    git checkout -b feature/feature-name
    ```
3. **Commit your changes**:
    ```bash
    git commit -am 'Add new feature'
    ```
4. **Push to the branch**:
    ```bash
    git push origin feature/feature-name
    ```
5. **Open a Pull Request** detailing the changes made.

## **License**
This project is licensed under the MIT License - see the LICENSE file for more details.

## **Contact**
For questions or more information, contact us via email: your.email@example.com.

For more details about the project, visit the GitHub repository: https://github.com/yourusername/email-service
