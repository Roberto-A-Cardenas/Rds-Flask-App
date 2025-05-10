# RDS-Backed Flask App on AWS with Terraform

![Terraform](https://img.shields.io/badge/Terraform-IaC-blue?logo=terraform)
![AWS](https://img.shields.io/badge/AWS-Deployed-orange?logo=amazon-aws)
![Flask](https://img.shields.io/badge/Flask-App-lightgrey?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-RDS-blue?logo=postgresql)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## 📌 Project Overview
This project provisions a secure, scalable web application on AWS using Terraform. It deploys a Flask app on EC2 and connects it to a PostgreSQL RDS instance in private subnets, demonstrating Infrastructure as Code, VPC best practices, and cloud database connectivity.

## 🚀 Technologies Used
- **AWS**: EC2, VPC, Subnets, RDS (PostgreSQL), Security Groups
- **Terraform**: IaC tool for AWS provisioning
- **Flask**: Python web application
- **PostgreSQL**: RDS-managed database

## 📐 Architecture Diagram
![diagram](diagram.png)

## 🗂 Folder Structure
```
rds-flask-app/
├── app/                # Flask app code
│   └── app.py
├── db/                 # SQL scripts
│   └── init.sql
├── terraform/          # Terraform IaC files
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── terraform.tfvars
│   └── user-data.sh.tpl
├── .gitignore
├── LICENSE
├── README.md
└── diagram.png
```

## 🛠 How to Deploy

### 1. Clone the repo:
```bash
git clone https://github.com/yourusername/rds-flask-app.git
cd rds-flask-app/terraform
```

### 2. Initialize Terraform:
```bash
terraform init
```

### 3. Apply the infrastructure:
```bash
terraform apply
```

### 4. SSH into EC2 and start Flask:
```bash
ssh -i terraform-key.pem ec2-user@<ec2_public_ip>
```

### 5. Run Flask with environment variables:
```bash
sudo DB_HOST="<rds_endpoint>" \
DB_NAME="flaskdb" \
DB_USER="flaskadmin" \
DB_PASS="yourpassword" \
python3 /home/ec2-user/app.py &
```

### 6. Test the app:
```bash
curl -X POST http://<ec2_ip>/add \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"YourName\"}"

http://<ec2_ip>/visitors
```

## 🧪 Example API Routes
- `GET /` → Connection test
- `POST /add` → Add visitor `{ "name": "John" }`
- `GET /visitors` → List all visitors

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> Made with ❤️ using AWS, Terraform, and Python Flask
